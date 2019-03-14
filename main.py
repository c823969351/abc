from urllib import request
import time

while True:
    cmd = request.urlopen("http://api.itmojun.com/pc/cmd/get?id=djb").read()
    cmd = cmd.decode("gbk")

    if cmd !="":
        print(cmd)
        time.sleep(3)
    else:
        time.sleep(1)