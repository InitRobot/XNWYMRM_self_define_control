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

def Disk_solve():
    pass
