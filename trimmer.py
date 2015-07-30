infof = file("temp.txt","r")
# temp.txt stores the data that is needed to process this post.
# It's 6 lines: Post Number, Source File, Target File,
# Previous File (Blank if none), Index File, Next File (Blank if none)
postnum = int(infof.next())
source = infof.next().strip()
target = infof.next().strip()
infof.close()
filein = file(source,"r")
fileout = file(target,"w")
curstring = ""
while not curstring.find('<li id="post-'+str(postnum))!=-1:
    curstring = filein.next()
while not curstring.find("<article>")!=-1:
    curstring = filein.next()
while not curstring.find("</article>")!=-1:
    curstring = filein.next()
    if not curstring.find("</article>")!=-1:
        fileout.write(curstring)
filein.close()
fileout.close()
