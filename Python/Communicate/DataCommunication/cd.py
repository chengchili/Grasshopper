def ghdataread():
    import time
    time.sleep(0.01)
    try:
        f = open("data_from_gh")
        dataread = f.read().replace("gh:", "")
        f.close()
    except:
        dataread = "Duration"
    return dataread
def ghdatawrite(data):
    import os
    import time
    time.sleep(0.01)
    try:
        f = open("data_from_py")
        f.close()
        data="Duration"
    except:
        f = open("data_from_py","w")
        f.write(data)
        f.close()
        try:
            os.remove("data_from_gh")
        except:
            pass
    return data