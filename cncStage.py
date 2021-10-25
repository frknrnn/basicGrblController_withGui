import time
import serial
from serial.tools import list_ports
from ui_main import Ui_MainWindow
from PySide2.QtCore import *
class cncPort(QThread):
    change_pixmap_signal = Signal(str)
    cncFlag = True

    def connectCnc(self,port):
        print(port)
        self.serial_port = serial.Serial(str(port), baudrate=115200,writeTimeout=0)
        #if not self.serial_port.isOpen():
        #    self.serial_port.open()


    def home(self):
        self.serial_port.write(b"1\x18")
        time.sleep(0.001)
        self.serial_port.write(b"~\n")
        time.sleep(0.001)
        self.serial_port.write(b"$H\n")
        time.sleep(0.001)

    def hold(self):
        self.serial_port.write(b"!\n")

    def resume(self):
        self.serial_port.write(b"1\x18")
        self.serial_port.write(b"~\n")

    def goZp(self,zFeedRate):
        target = "G91G01Z15.000F{0}\n".format(zFeedRate)
        self.serial_port.write(target.encode("utf-8"))


    def goZn(self,zFeedRate):
        target = "G91G01Z-15.000F{0}\n".format(zFeedRate)
        self.serial_port.write(target.encode("utf-8"))

    def goZp_stepMode(self):
        target = "G91G01Z0.001F1\n"
        self.serial_port.write(target.encode("utf-8"))

    def goZn_stepMode(self):
        target = "G91G01Z-0.001F1\n"
        self.serial_port.write(target.encode("utf-8"))


    def goXp(self,zFeedRate):
        target = "G91G01X-60.000F{0}\n".format(zFeedRate)
        self.serial_port.write(target.encode("utf-8"))

    def goXn(self,zFeedRate):
        target = "G91G01X60.000F{0}\n".format(zFeedRate)
        self.serial_port.write(target.encode("utf-8"))

    def goXp_stepMode(self):
        target = "G91G01X-0.001F1\n"
        self.serial_port.write(target.encode("utf-8"))

    def goXn_stepMode(self):
        target = "G91G01X0.001F1\n"
        self.serial_port.write(target.encode("utf-8"))

    def goYp(self,zFeedRate):
        target = "G91G01Y-60.000F{0}\n".format(zFeedRate)
        self.serial_port.write(target.encode("utf-8"))

    def goYn(self,zFeedRate):
        target = "G91G01Y60.000F{0}\n".format(zFeedRate)
        self.serial_port.write(target.encode("utf-8"))
    def goYp_stepMode(self):
        target = "G91G01Y-0.001F1\n"
        self.serial_port.write(target.encode("utf-8"))

    def goYn_stepMode(self):
        target = "G91G01Y0.001F1\n"
        self.serial_port.write(target.encode("utf-8"))


    def close_alarm(self):
        self.serial_port.write(b"$X\n")

    def goAbsulutePosition(self,x_loc,y_loc,z_loc):
        target = "G90G01X{0}Y{1}Z{2}F500\n".format(x_loc,y_loc,z_loc)
        self.serial_port.write(target.encode("utf-8"))


    def run(self):
        while self.cncFlag:
            self.serial_port.write(b"?\n")
            if (self.serial_port.inWaiting() > 0):
                position = self.serial_port.readline().decode()
                if (position.find("Alarm") != -1):
                    self.close_alarm()
                self.change_pixmap_signal.emit(position)
            else:
                time.sleep(0.001)


    def terminate(self):
        self.cncFlag = False
