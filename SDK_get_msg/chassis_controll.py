import SDK_
import Message_Delivery
import MSG_Solve
import Chassis_Solve
import Chassis_Move

SDK_.connect_enter_SDK()
Message_Delivery.connect_UDP()
SDK_.IN_OUT("game_msg on;")

for i in range(1,500):
    game_msg = Message_Delivery.try_get(timeout = 1)
    game_msg = MSG_Solve.solve_game(game_msg)
    print(game_msg)
    key_list = MSG_Solve.solve_key(game_msg)
    key_name_list = MSG_Solve.solve_key_name(key_list)
    print(key_name_list)
    wheel_spin = Chassis_Solve.Stright_Solve(key_name_list)
    print(wheel_spin)
    Chassis_Move.move(wheel_spin)


SDK_.IN_OUT("game_msg off;")
Message_Delivery.disconnect()
SDK_.disconnect()