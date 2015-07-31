import sys
# 6 Arguments: Post Number, Source File, Target File,
# Previous File ("-" if none), Index File, Next File (Blank if none)
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
trim(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
