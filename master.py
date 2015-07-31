import sys
import os
def trim(postnum,source,target,prevf,indexf,nextf):
    filein = file(source,"r")
    fileout = file(target,"w")
    if prevf != "-":
        fileout.write('<a href='+prevf+'>&lt;&lt;</a>  ')
    fileout.write('<a href='+indexf+'>Index</a>  ')
    if nextf != "-":
        fileout.write('<a href='+nextf+'>&gt;&gt;</a>')
    fileout.write('<br><br>\n')
    curstring = ""
    while not curstring.find('<li id="post-'+str(postnum))!=-1:
        curstring = filein.next()
    while not curstring.find("<article>")!=-1:
        curstring = filein.next()
    while not curstring.find("</article>")!=-1:
        curstring = filein.next()
        if not curstring.find("</article>")!=-1:
            fileout.write(curstring)
    fileout.write('\n<br>\n')
    if prevf != "-":
        fileout.write('<a href='+prevf+'>&lt;&lt;</a>  ')
    fileout.write('<a href='+indexf+'>Index</a>  ')
    if nextf != "-":
        fileout.write('<a href='+nextf+'>&gt;&gt;</a>')
    filein.close()
    fileout.close()

datafname = sys.argv[1]
# This is the file we are getting our data from.
dataf = file(datafname,"r")
maindata = dataf.next().strip().split(',')
dirname = maindata[2]+"/"
try:
    os.mkdir(maindata[2])
except:
    print "Warning! Directory already exists!"
    print "Proceed anyway? (Y/N)"
maindata[1] = int(maindata[1])
fulldata = [0]*maindata[1]
fullchdata = [0]*maindata[1]
for i in range(maindata[1]):
    fullchdata[i] = dataf.next().strip().split(',')
    fullchdata[i][1] = int(fullchdata[i][1])
    fulldata[i] = [0]*fullchdata[i][1]
    for j in range(fullchdata[i][1]):
        fulldata[i][j] = dataf.next().strip().split(',')
        fulldata[i][j][2] = fullchdata[i][2]+"_"+fulldata[i][j][2]+".html"
indexfname = 'index.html'
indexf = file(dirname+indexfname,"w")
indexf.write('<b><u>'+maindata[0]+'</u></b><br>\n<br>\n')
for i in range(maindata[1]):
    indexf.write('<u>'+fullchdata[i][0]+'</u><br>')
    for j in range(fullchdata[i][1]):
        #os.system('wget -O temp.html -- http://forums.spacebattles.com/posts/'+fulldata[i][j][1])
        if j == 0:
            if i == 0:
                prevf = "-"
            else:
                prevf = fulldata[i-1][-1][2]
        else:
            prevf = fulldata[i][j-1][2]
        if j == fullchdata[i][1]-1:
            if i == maindata[1]-1:
                nextf = "-"
            else:
                nextf = fulldata[i+1][0][2]
        else:
            nextf = fulldata[i][j+1][2]
        #trim(fulldata[i][j][1],"temp.html",dirname+fulldata[i][j][2],prevf,indexfname,nextf)
        indexf.write('<a href='+fulldata[i][j][2]+'>'+fulldata[i][j][0]+'</a><br>')
    indexf.write('<br>')
#os.remove('temp.html')
indexf.close()
