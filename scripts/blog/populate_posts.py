#
# read bram stoker dracula and make a blog post
# from every chapters first 20 lines
#
import sys, string

sys.path.append("./models/")

import Post

if __name__=="__main__":
    """
    This one is just for fun.
    It processes Bram Stoker's Dracula, extracts all chapters and makes a blog post 
    from the first 20 lines of each chapter.
    Dracula is for free on the web: see: http://www.gutenberg.org/ebooks/345
    To use this:
    1. copy it to the main directory of you application
    2. make sure you created a post model, controller, scaffold and migration 
    3. run this (dracula.txt should be in your apps public/doc/ directory by default. 
       Otherwise get it from the URL above)
    4. enjoy.
    """
    
    f = open("./public/doc/dracula.txt","r")
    counter = 0
    found = False
    postlist = []
    l = [l for l in f.readlines() if l.strip()]
    #print l
    skip = 0
    for line in l:
        counter += 1
        if line.lower().find("chapter") != -1 and skip <= counter:
            print line
            p = Post.Post()
            p.title = l[counter]
            p.content = ""
            content = l[counter+1:counter+20]
            #print content
            for elem in content:
                elem = elem.replace("\n","<br>")
                elem = elem.replace("\r\n","<br>")
                p.content += elem
                #print elem
            skip = counter+3
            p.create()
            print p
    sys.exit(0)