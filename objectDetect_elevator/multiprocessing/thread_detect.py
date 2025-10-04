from ultralytics import YOLO
from queue import Queue
from threading import Thread
import cv2
from multiprocessing import Process

model = YOLO("best.pt")

cap = cv2.VideoCapture(0)

ths = []

def takeFrame(frames_data) :
    while True :
        ret, frame = cap.read()
        if not ret :
            break
        frames_data.put(frame)

def detect(frame, result_data) :
    result_data.put(model(frame)[0].plot())

def multi_detect(frames_data,result_data) :
    while True :
        for _ in range(frames_data.qsize()) :
            frame = frames_data.get()
            th = Thread(target=detect, args=(frame, result_data))
            th.start()
            ths.append(th)
        for th in ths :
            th.join()

def showImage(result_data) :
    while True :
        if result_data.qsize() > 0 :
            frm = result_data.get()
            cv2.imshow('output',frm)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

if __name__ == "__main__" :
    frames_data = Queue()
    result_data = Queue()

    tf_th = Thread(target=takeFrame, args=(frames_data,))
    dt_th = Thread(target=multi_detect, args=(frames_data,result_data))
    sh_th = Thread(target=showImage, args=(result_data,))

    tf_th.start()
    dt_th.start()
    sh_th.start()

