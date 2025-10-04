from multiprocessing import Process, Queue
from threading import Thread
import cv2
from ultralytics import YOLO

model = YOLO("best.pt")

def detect(frame, detect_data) :
    detect_data.put(model(frame)[0].plot)
    
def yoloDetect(frames_data, detect_data) :
    while True :
        if frames_data.qsize() > 0 :
            image_data = frames_data.get()            
            result = model(image_data)
            detect_data.put(result[0].plot())

def showImage(detect_data, show) :
    while True :
        if detect_data.qsize() > 0 :
            frm = detect_data.get()
            # final_frame.put(frm)
            if show :
                cv2.imshow('output',frm)
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break

def takeFrame(show = True) :
    cap = cv2.VideoCapture(0)

    frames_data = Queue()
    detect_data = Queue()
    # final_frame = Queue()

    p1 = Process(target=yoloDetect, args=(frames_data, detect_data))
    p2 = Process(target=showImage, args=(detect_data,show)) 
    
    p1.start()
    p2.start()

    while True :
        ret, frame = cap.read()
        if not ret :
            break

        frames_data.put(frame)

    while True :
        if frames_data.qsize() == 0 and detect_data.qsize() == 0 :
            p1.terminate()
            p2.terminate()
            break
        # elif final_frame.qsize()>0:
        #     image = final_frame.get()

    cv2.destroyAllWindows()

if __name__ == "__main__" :
    takeFrame()







