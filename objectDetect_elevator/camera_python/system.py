from camera import *
from db import ResidentInfo
from detect import Detector
from serial_ard import Sercom

class System(Camera, ResidentInfo, Detector, Sercom) :
    def __init__(self):
        Camera.__init__(self)
        ResidentInfo.__init__(self,user = 'root', passwd='12345', host='localhost', db='resident')
        Detector.__init__(self,'./models/best.pt')
        Sercom.__init__(self, 'COM4',9600)

    def run(self) :
        try :
            while True :
                frame = self.get_frame()
                
                result = self.modeling(frame)
                self.show_frame(result.plot())

                id_list = self.get_classId(result)            
                
                if len(id_list) != 0 :

                    self.write('u'.encode())
                    break

                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break

        except Exception as e :
            print(f'{e}')

if __name__ == "__main__" :
    sys = System()
    sys.run()     

