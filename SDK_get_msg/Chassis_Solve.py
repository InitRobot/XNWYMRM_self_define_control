import math

forward_speed = 90
backward_speed = 50
side_speed = 50


def Stright_Solve(keys):
    result = []
    #对应    左右
    wheel = [0,0,#前(head)
             0,0]#后(tail)
    if 'W' in keys:
        wheel = [(i + 1) for i in wheel]
    if 'A' in keys:
        wheel[0] -= 1
        wheel[1] += 1
        wheel[2] += 1
        wheel[3] -= 1
    if 'S' in keys:
        wheel = [(i - 1) for i in wheel]
    if 'D' in keys:
        wheel[0] += 1
        wheel[1] -= 1
        wheel[2] -= 1
        wheel[3] += 1
    for i in range(len(wheel)):
        if wheel[i] > 0:
            wheel[i] = 1
        elif wheel[i] < 0:
            wheel[i] = -1
    print(wheel)
    result = wheel
    return result

def Disk_solve(keys, degree, spin = 1):
        #对应    左右
    wheel_stright = [0,0,#前(head)
                     0,0]#后(tail)
    if 'W' in keys:
        wheel_stright = [(i + 1) for i in wheel_stright]
    if 'A' in keys:
        wheel_stright[0] -= 1
        wheel_stright[1] += 1
        wheel_stright[2] += 1
        wheel_stright[3] -= 1
    if 'S' in keys:
        wheel_stright = [(i - 1) for i in wheel_stright]
    if 'D' in keys:
        wheel_stright[0] += 1
        wheel_stright[1] -= 1
        wheel_stright[2] -= 1
        wheel_stright[3] += 1
    for i in range(len(wheel_stright)):
        if wheel_stright[i] > 0:
            wheel_stright[i] = 1
        elif wheel_stright[i] < 0:
            wheel_stright[i] = -1
    print(wheel_stright)
    wheel_spin = wheel_stright
    wheel_spin[0] *= math.sin((degree / 180 - 0.25)* math.pi)
    wheel_spin[1] *= math.sin((degree / 180 + 0.25)* math.pi)
    wheel_spin[2] *= math.sin((degree / 180 + 0.25)* math.pi)
    wheel_spin[3] *= math.sin((degree / 180 - 0.25)* math.pi)

    wheel_spin[0] = (wheel_spin[0] + 1) / 2
    wheel_spin[1] = (wheel_spin[1] - 1) / 2
    wheel_spin[2] = (wheel_spin[2] + 1) / 2
    wheel_spin[3] = (wheel_spin[3] - 1) / 2
    return wheel_spin

    