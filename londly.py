#coding:utf-8
import os
import time
import argparse
import shutil

def biaoti():
    splash1 = """


 __                                __  __           
|  \                              |  \|  \          
| $$      ______   _______    ____| $$| $$ __    __ 
| $$     /      \ |       \  /      $$| $$|  \  |  \
| $$    |  $$$$$$\| $$$$$$$\|  $$$$$$$| $$| $$  | $$
| $$    | $$  | $$| $$  | $$| $$  | $$| $$| $$  | $$
| $$____| $$__/ $$| $$  | $$| $$__| $$| $$| $$__/ $$
| $$     \$$    $$| $$  | $$ \$$    $$| $$ \$$    $$
 \$$$$$$$$\$$$$$$  \$$   \$$  \$$$$$$$ \$$ _\$$$$$$$
                                          |  \__| $$
                                           \$$    $$
                                            \$$$$$$ 

                                                                 
    """
    print(splash1)

def args():
    parser = argparse.ArgumentParser(description='Masscan2Httpx2Nuclei')
    #help换行
    parser.add_argument('-i', '--input', help='参考masscan -iL', required=True)
    parser.add_argument('-p', '--port',help='参考masscan -p', required=True)
    parser.add_argument('-rate','--rate', help='参考masscan速率rate', required=True)
    args = parser.parse_args()
    return args

def update():
    splash00 = """
        +----------------------------------+
        | 正在更新nuclei&xray       
        +----------------------------------+
    """
    print(splash00)
    os.system('./nuclei -update')
    os.system('./xray_linux_amd64 upgrade')
    splash03 = """
        +----------------------------------+
        | 检查完毕,解放双手!!
        +----------------------------------+
    """
    print(splash03)



def check_args(args):
    if not os.path.exists(args.input):
        print('ip文件不存在')
        exit()
    if not args.port:
        print('请输入端口参数')
        exit()
    if not args.rate:
        print('请输入扫描速率(例：-rate 2000)')
        exit()
    return args

def masscan2httpx2nuclei(args):
    args = check_args(args)
    input_file = args.input
    port = args.port
    rate = args.rate
    os.system('masscan -iL ' + input_file + ' -p' + port + ' -oL masscan.txt --rate ' + rate)
def cdn():
    os.system('python3 cdn.py list.txt')
def masscan2httpx2nuclei_main():
    while True:
        if os.path.exists("masscan.txt"):
            break
        else:
            time.sleep(1)
    if os.path.getsize("masscan.txt") == 0:
        splash3 = """
            +----------------------------------+
            | 无端口开放，程序已退出!          
            +----------------------------------+
        """
        print(splash3)
        exit()
    else :
        splash4 = """
            +----------------------------------------+
            | Masscan扫描结果解析并调用httpx   
            +----------------------------------------+
        """
        print(splash4)
        masscanfile = open("masscan.txt", "r")
        masscanfile.seek(0)
        for line in masscanfile:
            if line.startswith("#"):
                continue
            if line.startswith("open"):
                line = line.split(" ")
                with open("masscanconvert.txt", "a") as f:
                    f.write(line[3]+":"+line[2]+"\n")
                    f.close()
        masscanfile.close()
    if os.path.exists("masscan.txt"):
        os.system('./httpx -l masscanconvert.txt -nc -o httpxresult.txt')
        os.remove("masscan.txt")
        splash2 = """
            +----------------------------------+
            | Httpx is done !                  
            +----------------------------------+
        """
        print(splash2)
    else:
        splash5 = """
            +----------------------------------+
            | 未发现解析后的masscan端口结果    
            +----------------------------------+
        """
        print(splash5)
        exit()
def observer():
    os.system('./observer -f masscanconvert.txt -c observer.txt')
def Finger():
    path=os.getcwd()
    os.system('python3 Finger/Finger.py -f ' + path + r"/masscanconvert.txt")
    files = path + r"/Finger/output/"
    b = os.listdir(files)
    new = path
    for f in b:
        shutil.move(files + f, new)
def fscan():
    os.system('./fscan64 -hf ip.txt -o fscan.txt')
def nu():
    if os.path.exists("httpxresult.txt"):
        os.system('./nuclei -l httpxresult.txt -s medium,high,critical -o nucleiresult.txt')
        os.system('./xray_linux_amd64 webscan -url-file httpxresult.txt --html-output xray.html')
        os.remove("httpxresult.txt")
        os.remove("masscanconvert.txt")
    else:
        print("扫描结果未发现http协议")
        exit()
    if os.path.exists("nucleiresult.txt"):
        splash6 = """
            +----------------------------------+
            | 扫描完成,请查看nucleiresult.txt 
            +----------------------------------+
        """
        print(splash6)
    else:
        splash7 = """
            +----------------------------------+
            | nuclei未发现中高危漏洞                
            +----------------------------------+
        """
        print(splash7)
    if os.path.exists("xray.html"):
        splash8 = """
            +----------------------------------+
            | 扫描完成,请查看xray.html        
            +----------------------------------+
        """
        print(splash8)
    else:
        splash9 = """
            +----------------------------------+
            | xray未发现漏洞                    
            +----------------------------------+
        """
        print(splash9)
    exit()


def main():
    biaoti()
    update()
    cdn()
    masscan2httpx2nuclei(args())
    masscan2httpx2nuclei_main()
    observer()
    Finger()
    fscan()
    nu()


if __name__ == '__main__':
    main()
    exit()
