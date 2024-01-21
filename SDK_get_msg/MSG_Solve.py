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

def solve_key(msg):#用于从赛事数据推送中获得键位
    result = []
    key_n = msg[6]
    #print(key_n)
    if key_n != 0:
        keys = msg[0 - key_n: ]
        #print(keys)
        #print(type(keys))
        result = keys
    return result

def solve_key_name(keys):#将获得键位转换为真实名称
    result = []
    key_name_list = []
    for key in keys:
        if key >= 48 and key <= 90:
            key_name_list.append(chr(key))
        elif key == 8:
            key_name_list.append("Space")
        elif key == 9:
            key_name_list.append("Tab")
        elif key == 16:
            key_name_list.append("Shift")
        elif key == 17:
            key_name_list.append("Ctrl")
        elif key == 18:
            key_name_list.append("Alt")
        elif key == 20:
            key_name_list.append("Caps")
    result = key_name_list
    return result
