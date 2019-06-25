import serial
import time
import struct

class STM32_Message(object):
    x_vel       =0
    y_vel       =0
    ang_vel     =0
    wind_left   =0
    wind_right  =0
    unwind_left =0
    unwind_right=0
    left_prop   =0
    right_prop  =0
    roller      =0

    def __init__(self,port,baudrate):
        self.port=port
        self.baudrate=baudrate
        self.__init_command()
    def __clear_Command(self):
        self.x_vel       =0
        self.y_vel       =0
        self.ang_vel     =0
        self.wind_left   =0
        self.wind_right  =0
        self.unwind_left =0
        self.unwind_right=0
        self.left_prop   =0
        self.right_prop  =0
        self.roller      =0
    def __init_command(self):
        self.__clear_Command()
    def convert_rxbytes_to_int16(self,offset,datalist):
        """
        :param offset:     the data shift
        :param datalist:   is a list of command
        :return:
        """
        (receivce,)=struct.unpack("h",''.join(datalist[offset:offset+2]))
        return receivce
    def convert_rxbytes_to_int(self,offset,datalist):
        """

        :param offset:
        :param datalist:
        :return:
        """
        (receive,)=struct.unpack("i",''.join(datalist[offset:offset+4]))
        return receive
    def convert_rxbytes_to_float(self,offset,datalist):
        """

        :param offset:
        :param datalist:
        :return:
        """
        (receive,)=struct.unpack("f",''.join(datalist[offset:offset+4]))
        return receive



    def convert_int16_to_txbytes(self, send):
        """
        return bytesarray
        """
        print(struct.pack("h", send))
        return struct.pack("h", send)


    def convert_int_to_txbytes(self, send):
        """
        return bytesarray
        """
        print((struct.pack("i", send)).encode('hex'))
        return struct.pack("i", send)



if __name__=='__main__':
    stm32=STM32_Message('com1',115200)
    stm32.convert_int_to_txbytes(12345678)
