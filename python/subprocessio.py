import subprocess
import time
import os
import threading
import uuid

def func(proc,filename):
    n = 0
    with open(filename, "r") as f:
        while proc.poll() is None:
            where = f.tell()
            to_read = os.stat(filename).st_size - n
            print(os.stat(filename))
            data = f.read(to_read)
            print(data)
            n += to_read
            time.sleep(10)
        to_read = os.stat(filename).st_size - n
        data = f.read(to_read)
        print(data)
    os.remove(filename)

def main(cmd):
    filename = str(uuid.uuid1())
    with open(filename,"w") as f:
        with subprocess.Popen(cmd,stdout=f,shell=True) as proc:
            thread = threading.Thread(target=func,args=(proc,filename))
            thread.start()
            thread.join()




if __name__ == '__main__':
    cmd = "cd /; ls -alR"
    main(cmd)