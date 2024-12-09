import os

try: os.mkfifo("invoke")
except FileExistsError: pass

while True:
    with open("invoke") as f:
        print("recv", f.read())
