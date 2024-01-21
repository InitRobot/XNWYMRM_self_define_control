# XNWYMRM_self_define_control
此内容用于对RM机器人的控制方式经行自定义

## README
SDK_.py 包含有基本的函数封装

connect_direct.py 为开发者文档中直连的内容
connect_wifi.py 为开发者文档中wifi连接的内容
connect_USB.py 为开发者文档中USB连接的内容
connect_USB_fire.py 测试发射一次
get_msg.py 为直连模式，用于测试赛事引擎数据
get_IP.py 为wifi模式获取机器IP地址
get_mode.py 用于测试wifi模式


## 工程日志
20240119
    开始编写

- 13：03 抄了connect
- 16：07 完成IP地址获取
- 16:10 完成WiFi连接
- 16:53 发现数据有时直接在控制时获得

20240120
    修改wifi为USB
- 14:49 成功连接USB
- 16:13 编写connect_USB_fire.py，发现***一定要写try(用于接收OUT)***
- 16:49 完成connect_USB_fire.py封装
- 17:06 完成SDK_.py对于函数的封装
- 17:39 补充SDK_.py(/SDK_get_msg)对于等待回复的函数，开始研究数据推送
- 17:57 发现接收消息推送要在UDP中，下班

20240121
    开始研究UDP
- 11:14 研究UDP
- 11:35 无法理解为什么UDP没有收到信息
- 12:56 尝试并放弃了RMSDK


## SDK_.py说明
- connect_TCP():      与机器人控制命令端口建立 TCP 连接
- disconnect():       关闭端口连接
- try_get(timeout=5):     这个函数默认等待5秒钟，如果在这个时间内没有收到机器人的返回结果，就会立即返回'no_OUT'。如果收到了机器人的返回结果，就会解码并返回结果字符串。
- IN(message):检测并向机器发送message，并输出
- OUT():检测机器回复，并输出
- IN_OUT(message):检测并向机器发送message，检测机器回复，并输出
- connect_enter_SDK(): 与机器人控制命令端口建立 TCP 连接，并进入SDK模式控制

## 参考资料
- RM开发者文档：https://robomaster-dev.readthedocs.io/zh-cn/latest/
- UDP:https://blog.csdn.net/weixin_51570574/article/details/132503864?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522170580572816800211557416%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=170580572816800211557416&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-132503864-null-null.142^v99^pc_search_result_base8&utm_term=UDP&spm=1018.2226.3001.4187