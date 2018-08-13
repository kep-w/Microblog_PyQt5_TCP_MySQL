服务端

服务器后台运行server.py
sudo nohup python -u server.py start > runmicroblog.log 2>&1 &

pip3 install pipreqs
pipreqs /path



pip --- Python2的标准第三方库管理工具
pip3 --- Python3的标准第三方库管理工具

安装软件
pip3 install Package
升级软件
pip3 install --upgrade Package
卸载软件
pip3 uninstall Package
查看软件包清单
pip3 list

查找软件包
pip3 search Package

查看软件包信息
pip3 show Package

记录软件环境
pip3 freeze >requirement.txt

根据环境文件进行环境安装
pip3 install -r requirement.txt


