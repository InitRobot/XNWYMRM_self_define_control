import SDK_
import Message_Delivery
import MSG_Solve
import Chassis_Solve
import Chassis_Move

SDK_.connect_enter_SDK()
SDK_.IN_OUT("robot mode free;")

for i in range(1,500):
    gimbal_msg = SDK_.IN_OUT("gimbal attitude ?;")
    gimbal = MSG_Solve.solve_gimbal(gimbal_msg)

SDK_.disconnect()