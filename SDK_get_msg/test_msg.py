import SDK_
import Message_Delivery
import MSG_Solve
#import time


SDK_.connect_enter_SDK()
Message_Delivery.connect_UDP()
#SDK_.IN_OUT("chassis status ?;")
SDK_.IN_OUT("game_msg on;")
#SDK_.IN_OUT("chassis push freq 10;")
#time.sleep(1)
for i in range(1,500):
    #print("try TCP")
    #SDK_.OUT(timeout = 1)
    #print("try UDP")
    game_msg = Message_Delivery.try_get(timeout = 1)
    print(game_msg)
    game_msg = MSG_Solve.solve_game(game_msg)
    print(game_msg)
#SDK_.IN_OUT("game msg push [0, 6, 1, 0, 0, 255, 1, 199];")
SDK_.IN_OUT("game_msg off;")
Message_Delivery.disconnect()
SDK_.disconnect()