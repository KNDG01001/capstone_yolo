import cv2
        
class Camera :
    def __init__(self) :
        self.cap = cv2.VideoCapture(0)
    
    def get_frame(self) :
        try :
            _, frame = self.cap.read()
            return frame 
        except Exception as e :
            print(f"{e}")

    def show_frame(self, frame) :
        cv2.imshow('a',frame)

# if __name__ == "__main__" :
#     cam = Camera()
#     while True :
#         frame = cam.get_frame()
#         cam.show_frame(frame)    
#         if cv2.waitKey(25) & 0xFF == ord("q"):
#             cv2.destroyAllWindows()
#             break