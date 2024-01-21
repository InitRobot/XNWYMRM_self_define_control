import SDK_
import Message_Delivery
import time


SDK_.connect_enter_SDK()

SDK_.IN_OUT("chassis push attitude on;")
SDK_.IN_OUT("chassis push freq 10;")
SDK_.disconnect()
time.sleep(1)
Message_Delivery.connect_UDP()
for i in range(1,5):
    #print("try TCP")
    #SDK_.OUT(timeout = 1)
    print("try UDP")
    print(Message_Delivery.try_get(timeout = 1))
#SDK_.IN_OUT("game msg push [0, 6, 1, 0, 0, 255, 1, 199];")
Message_Delivery.disconnect()
