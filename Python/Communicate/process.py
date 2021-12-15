import time
import DataCommunication as dc

ghdata=dc.ghdata

test=11
print(ghdata(test))


filepath =r'c:\Users\User\Desktop\github\Grasshopper\Python\Communicate\mediation'
filepath = filepath.replace("\\","/")

f=open(filepath,"r")
data=f.read()
f.close()
print(data)
gh= "saved_by_gh:"
print("current data:" + data)
if gh in data:
    print ("let's modify it~!!")
    f = open(filepath, "w")
    data=data.replace(gh,"")
    data=float(data)+1
    data=str(data)
    f.write(data)
    f.close()
print("current data:" + data)

while True:
    time.sleep(0.1)
    f = open(filepath, "r")
    data = f.read()
    f.close()
    if gh in data:
        print("let's modify it~!!")
        f = open(filepath, "w")
        data = data.replace(gh, "")
        data = float(data) + 1
        data = str(data)
        f.write(data)
        f.close()
    print("current data:" + data)



