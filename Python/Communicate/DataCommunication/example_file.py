import cd
import time
ghdataread=cd.ghdataread
ghdatawrite=cd.ghdatawrite

c=0
while True:
    c=c+1
    print("iteration: "+ str(c))
    data = ghdataread()
    if data != "Duration":
        #print(data)
        #process data here~
        time.sleep(0.01)



        # process data here~
        ghdatawrite(data+str(c))



