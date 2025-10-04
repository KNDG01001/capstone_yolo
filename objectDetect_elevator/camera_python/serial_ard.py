
from serial import Serial 

class Sercom(Serial) :
    def __init__(self,prt,br) :
        super().__init__(port = prt,baudrate = br)
        
    def write_int(self, num) :
        self.write(str(num).encode())
        self.write('\n'.encode())

    def write_end(self) :
        self.write('-1'.encode())
        self.write('\n'.encode())

    def readln(self) :
        return self.readline().decode().rstrip('\r\n')


