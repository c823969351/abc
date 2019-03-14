from urllib import request
import time
import os

while True:
    cmd = request.urlopen("http://api.itmojun.com/pc/cmd/get?id=djb").read()
    cmd = cmd.decode("gbk")

    if cmd !="":
        print(cmd)

        if"关机"in cmd:
            # os.system("shutdown -s -t 0")
            pass
        elif"重启"in cmd:
            # os.system("shutdown -r -t 0")
            pass
        elif"网站" in cmd:
            os.system("explorer https://www.baidu.com")
        elif"播放" in cmd:
            os.system('c.mp3')


        time.sleep(3)
    else:
        time.sleep(1)