import socket
import sys
import select

# USB 模式下，机器人默认 IP 地址为 192.168.42.2, 控制命令端口号为 40923
host = "192.168.42.2"
port = 40923

def connect_TCP():# 与机器人控制命令端口建立 TCP 连接
        global TCP_socket
        address = (host, int(port))

        # 与机器人控制命令端口建立 TCP 连接
        TCP_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("Connecting_TCP...")

        TCP_socket.connect(address)

        print("TCP_Connected!")

def disconnect():# 关闭端口连接
        global TCP_socket
        # 关闭端口连接
        print("TCP disconnecting...")
        TCP_socket.shutdown(socket.SHUT_WR)
        TCP_socket.close()
        print("TCP disconnected!")

def try_get(timeout=5):#这个函数默认等待5秒钟，如果在这个时间内没有收到机器人的返回结果，就会立即返回空字符串。如果收到了机器人的返回结果，就会解码并返回结果字符串。
    result = ''
    try:
        # 设置超时时间
        ready = select.select([TCP_socket], [], [], timeout)
        if ready[0]:
            # 如果有可读数据，接收并解码
            buf = TCP_socket.recv(1024)
            result = buf.decode('utf-8')
        else:
                result = 'no_OUT'
    except socket.error as e:
        print("Error receiving :", e)
        sys.exit(1)
    return result

def IN(message):#检测并向机器发送message，并输出
        # in_message为要发送的指令
        if ( str(type(message)) == "<class 'str'>" ) and (message[-1] == ';') :
                print('IN:' , message)
                TCP_socket.send(message.encode('utf-8'))
        else:
                print('please input str that ends with ";"')

def OUT(timeout=5):#检测机器回复，并输出
        result = ''
        result = try_get(timeout)
        print("OUT:", result)
        return result

def IN_OUT(message, timeout=5):#检测并向机器发送message，检测机器回复，并输出
        result = ''
        IN(message)
        result = OUT(timeout)
        return result

def connect_enter_SDK(timeout=5):# 与机器人控制命令端口建立 TCP 连接，并进入SDK模式控制
        connect_TCP()
        IN_OUT("command;", timeout)
        IN_OUT("quit;", timeout)#DJI的小BUG，以免图传卡住
        IN_OUT("command;", timeout)