import urllib2
text="https://portal.opentopography.org/API/globaldem?demtype=SRTMGL3&south={s}&north={n}&west={w}&east={e}&outputFormat=AAIGrid"
coordinate=[s,n,w,e]
colist=["{s}","{n}","{w}","{e}"]

for i in range(len(colist)):
    if colist[i] in text:
        text=text.replace(colist[i],coordinate[i])

print text
response = urllib2.urlopen(text)

data = response.read()
data = data.split("\n")