import re
def main():
    content=input("Enter String:")
    target=input("Enter What Needs To Be Removed (or leave blank for whitespace):")
    RegStrip(target,content)
def RegStrip(target,content):
    newTarget=""
    if(target==""):
        newTarget+="\s*"
    else:
        target=re.escape(target)
        for i in target:
            if(i!="\\"):
                newTarget=newTarget+i+"*"
            else:
                newTarget+=i
    
    print(newTarget)
    startR=re.compile(rf'^{newTarget}')
    endR=re.compile(rf'{newTarget}$')
    x=startR.sub("",content)
    Result=endR.sub("",x)
    print("Here is your string:"+Result)

main()