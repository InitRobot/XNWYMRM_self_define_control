def solve_game(msg):#用于解析赛事数据推送
    result = ''
    if msg[0:14] == 'game msg push ' and msg[-1] == ';':
        #print('right_start')
        info = msg[15:-2]
        #print(info)
        info_list = info.split(', ')
        #print(info_list)
        info_list_int = [ int(i) for i in info_list ]
        #print(info_list_int)
        result = info_list_int
    else:
        print('please give a game msg push')
    return result

def solve_key(msg):
    result = []
    key_n = msg[6]
    print(key_n)
    if key_n != 0:
        keys = msg[0 - key_n: ]
        print(keys)
        print(type(keys))
        result = keys
    return result
