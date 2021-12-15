def ghdataread():
    import time
    time.sleep(0.01)

    try:
        f = open("data_from_gh")
        dataread = f.read().replace("gh:", "")
        #print("data_from_gh exists")
        #print("dataread: " + dataread)
        f.close()

    except:
        dataread = "Duration"
        #print("data_from_gh doesn't exist")

    return dataread

def ghdatawrite(data):

    import os
    import time
    time.sleep(0.01)
    #print(data + " is waiting to write")
    try:
        f = open("data_from_py")
        f.close()
        #print("data_from_py havn't written")
        data="Duration"
    except:
        #print("ok to write")
        f = open("data_from_py","w")
        f.write(data)
        f.close()
        #print("writing finished: " +  data)
        try:
            os.remove("data_from_gh")
        except:
            pass
    return data


