import subprocess,os,math


# data=subprocess.check_output(['netsh', 'wlan','show','profiles']).decode('utf-8')
# data = subprocess.check_output(['netsh','wlan','show','profiles']).decode(get_encoding).split('\n')

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('latin1').split("\n")
wifi=[i.split(":")[1][1:-1]for i in data if "All User Profile" in i]
for i in wifi:
	result=subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('latin1').split("\n")
	result=[i.split(":")[1][1:-1]for i in result if "Key Content" in i]
	password="".join(result)
	print(f"{i}: {password}")
# isse bachne ke liye ap apna wifi ,hotstop ka name  (kãyêl Ãßçêô) aise special character use kr skte hn
['netsh', 'wlan', 'show', 'profile', '\x80ool', 'key=clear']

# inthis case it not read characters

n = int(input())
temp = list(map(int, input().split(' ')[:n]))
for j in range(len(temp)-1,-1,-1):
    print(temp[j])





