import copy

try:
    print namelist_py[0]
    print data_py[0]
except:
    namelist_py=[]
    data_py=[]

if x.split(";")[0] in namelist_py:
    print("it's existing")
else:
    namelist_py.append(x.split(";")[0])
    data_py=copy.deepcopy(namelist_py)

for i in range(len(data_py)):
    if namelist_py[i] in x:
        data_py[i]=x


if reset:
    namelist_py=[]
    data_py=[]


namelist=namelist_py
data=data_py
