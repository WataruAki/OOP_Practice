import math

class TuLanh:
    def __init__(self, nhanhieu, maso, nuocsx, tkdien, dungtich, gia):
        self.__nhanhieu = nhanhieu
        self.__maso = maso
        self.__nuocsx = nuocsx
        self.__tkdien = tkdien
        self.__dungtich = dungtich
        self.__gia = gia

        
        
    def read(self):
        parts = input().split('|')
        nhanhieu = int(parts[0])
        maso = int(parts[1])
        nuocsx = str(parts[2])
        tkdien = str(parts[3])
        dungtich = int(parts[4])
        gia = int(parts[5])
        super().__init__(nhanhieu, maso, nuocsx, tkdien, dungtich, gia)


    
    def print(self):
        print(f"Nhãn hiệu: {self.__nhanhieu}")
        print(f"Mã số: {self.__maso}")
        print(f"Nước SX: {self.__nuocsx}")
        print(f"T/K điện: {'Có'if self.__tkdien else 'Không'}")
        print(f"Dung tích: {self.__dungtich}L")
        print(f"Giá: {self.__gia}VNĐ")

