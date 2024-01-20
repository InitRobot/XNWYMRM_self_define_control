# XNWYMRM_self_define_control
此内容用于对RM机器人的控制方式经行自定义

## README
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


## 参考资料
- RM开发者文档：https://robomaster-dev.readthedocs.io/zh-cn/latest/