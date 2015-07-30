import sys
# 6 Arguments: Post Number, Source File, Target File,
# Previous File (Blank if none), Index File, Next File (Blank if none)
def trim(postnum,source,target,prevf,indexf,nextf):
    filein = file(source,"r")
    fileout = file(target,"w")
    fileout.write('<a href='+prevf+'>&lt;&lt;</a>  ')
    fileout.write('<a href='+indexf+'>Index</a>  ')
    fileout.write('<a href='+nextf+'>&gt;&gt;</a><br><br>\n')
    curstring = ""
    while not curstring.find('<li id="post-'+str(postnum))!=-1:
        curstring = filein.next()
    while not curstring.find("<article>")!=-1:
        curstring = filein.next()
    while not curstring.find("</article>")!=-1:
        curstring = filein.next()
        if not curstring.find("</article>")!=-1:
            fileout.write(curstring)
    fileout.write('\n<br>\n<a href='+prevf+'>&lt;&lt;</a>  <a href='+indexf+'>Index</a>  <a href='+nextf+'>&gt;&gt;</a>')
    filein.close()
    fileout.close()
trim(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
