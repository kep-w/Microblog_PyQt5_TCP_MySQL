### 使用pyqt5实现微博基础功能(发布微博, 点赞, 转发, 评论)

- 页面实现使用pyqt5

- 通信连接是基于TCP的短连接

   通信采用xml格式化报文

- 用户密码采用哈希散列中的MD5算法转换

- 数据库使用MySQL

### 项目所需的环境在requirements.txt中

- client 文件夹内为客户端内容, server文件夹下为服务端内容

- 运行项目需要修改包内每一个__init__.py中的路径为当前工作路径

### 一些可能用到的命令:

- 记录软件环境，可以使用下面的命令

   pip3 freeze >requirement.txt

- 本项目使用以下pipreqs收集第三方的依赖库信息

   pip3 install pipreqs

- 在项目目录下执行以下命令，自动生成写入到requirements.txt文件中

   pipreqs .

- 根据环境文件进行环境安装

   pip3 install -r requirements.txt
