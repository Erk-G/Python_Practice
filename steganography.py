import cImage
#Stringatize takes a list of strings and combines them all into a string 
def Stringatize(alist):
    astring=""
    for i in range(len(alist)):
        astring=astring+alist[i]
    return astring
#Pixelize takes a character string turns it into an ASCII value and replaces the first digit of the R, G and B value with the third, second and first digit of the ASCII value respectively. If the ASCII value is 93, the code makes it equal too 093, and if the final value of R,G or B is over 255 it subtracts 10 because a color cannot be over 255.
def Pixelize(astring,r,g,b):
    f=str(ord(astring))
    if(len(f)<3):
        f="0"+f
    r=str(r)
    if(len(r)<3):
        r="0"+r
    g=str(g)
    if(len(g)<3):
        g="0"+g
    b=str(b)
    if(len(b)<3):
        b="0"+b
    r=r[:2]+f[0]
    g=g[:2]+f[1]
    b=b[:2]+f[2]
    r=int(r)
    if(r>255):
        r=r-10
    g=int(g)
    if(g>255):
        g=g-10
    b=int(b)
    if(b>255):
        b=b-10
    p=cImage.Pixel(r,g,b)
    return p
#dePixelize reverses what pixelize does. It takes in the RGB values, puts them into strings in order too remove their first digits and put them into a string together then takes the character of the ASCII equivilant.
def dePixelize(r,g,b):
    astring=""
    r=str(r)
    g=str(g)
    b=str(b)
    astring=astring+r[-1]+g[-1]+b[-1]
    astring=chr(int(astring))
    return astring
#Hide takes an image and makes a new image pixel by pixel, by using the text file given to replace specific colors of the original image. The result being a aastring being hidden in an image file very similar to the original. When the text is finished the function will use a space character as reference for the rest of the pixels.
def Hide(img,txt):
    rows=img.getHeight()
    cols=img.getWidth()
    newimg=cImage.EmptyImage(cols,rows)
    lines=txt.readlines()
    line=Stringatize(lines)
    i=0
    for c in range(cols):
        for r in range(rows):
            if(i<len(line)):
                f=img.getPixel(c,r)
                j=f.getRed()
                k=f.getBlue()
                l=f.getGreen()
                h=line[i]
                P=Pixelize(h,j,l,k)
                newimg.setPixel(c,r,P)
                i=i+1
            else:
                f=img.getPixel(c,r)
                j=f.getRed()
                k=f.getBlue()
                l=f.getGreen()
                P=Pixelize(" ",j,l,k)
                newimg.setPixel(c,r,P)
    return newimg
#Decode takes an image and does the reverse of what hide does and returns a string. The biggest difference being if there are more than 4 spaces in a row nothing more is added to the returned string as hide adds in a lot of unnecessary spaces.
def Decode(img):
    astring = ""
    rows = img.getHeight()
    cols = img.getWidth()
    i=0
    for c in range(cols):
        for r in range(rows):
            q = img.getPixel(c,r)
            r = q.getRed()
            s = q.getGreen()
            t = q.getBlue()
            h=dePixelize(r,s,t)
            if(h==" "):
                i=i+1
            else:
                i=0
            if(i<5):
                astring = astring + h

    return astring
#Main asks the user if they want ot hide or decode, if neither returns an error. Hide asks for an image and a text file to hide in the image then calls the hide funtion. The Hide function returns a new image called new.png. Decode only asks for an image and calls Decode, which returns a string that is put into a .txt titled Decoded.
def main():
    command=input("Enter 'Decode' or 'Hide': ")
    if(command=="Hide"):
        
        fname=input("What is the image you want to hide the message in?: ")
        fimg=cImage.FileImage(fname)

        nfname=input("What is the text file you want to hide: ")
        nfile=open(nfname,"r")
        nimg=Hide(fimg,nfile)
        w=nimg.getWidth()
        h=nimg.getHeight()
        
        nwindow=cImage.ImageWin("New",w,h)
        nimg.draw(nwindow)
        nimg.save("new.png")
        nwindow.exitOnClick()
    elif(command=="Decode"):
        gname=input("What is the image file  you want decode?: ")
        fimg=cImage.FileImage(gname)
        nfile=open("Decoded.txt","w")
        nfile.write(Decode(fimg))
        nfile.close
    else:
        print("Invalid Command")
main()
