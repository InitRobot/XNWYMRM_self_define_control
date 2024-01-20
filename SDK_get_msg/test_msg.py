import SDK_

SDK_.connect_enter_SDK()
SDK_.IN("game_msg on;")
for i in range(1,9):
    SDK_.OUT()
SDK_.IN_OUT("game msg push [0, 6, 1, 0, 0, 255, 1, 199];")
SDK_.disconnect()