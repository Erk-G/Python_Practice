import re
def main():
    f=open("Trials.txt","r")
    g=open("Dungeons.txt","r")
    lines=f.read()
    line=g.read()
    x=re.findall("Main\sQuest.*",lines)
    z=re.findall("[|]Main\sScenario\sQuest.*",lines)
    x1=re.findall("[|]Main\sScenario\sQuest.*",line)
    pretrials=""
    for i in x:
        pretrials=pretrials+i[13:]
    for i in z:
        pretrials=pretrials+i[23:]
    trials=re.findall("\[\[(.*?)\]",pretrials)
    predungeons=""
    for i in x1:
        predungeons=predungeons+i
    dungeons=re.findall("\[\[(.*?)\]",predungeons)
    f.close
    g.close
    h=open("NTrials.txt","w+")
    j=open("NDungeons.txt","w+")
    for i in trials:
        astring=re.sub(r'\([^)]*\)','', i)
        astring=re.sub('[^A-Za-z0-9]+', '', astring)
        astring=astring.lower()
        h.write(astring+"\n")
    for i in dungeons:
        astring=re.sub(r'\([^)]*\)','', i)
        astring=re.sub('[^A-Za-z0-9]+','', astring)
        astring=astring.lower()
        j.write(astring+"\n")
    f=open("Quest.txt","r")
    lines=f.read()
    questsName=re.findall("row[|](.*?)\}",lines)
    f.close
    f=open("NQuestList.txt","w+")
    for i in questsName:
        astring=re.sub(r'\([^)]*\)','', i)
        astring=re.sub('[^A-Za-z0-9]+', '', astring)
        astring=astring.lower()
        f.write(astring+"\n")
    f.close
    h.close
    j.close
    #Had to close and reopen NQuests because I guess it doesn't save
    f=open("NQuestList.txt","r")
    h=open("NTrials.txt","r")
    j=open("NDungeons.txt","r")
    quests=f.read().splitlines()
    trials=h.read().splitlines()
    dungeons=j.read().splitlines()
    f.close
    #trials has a list of all of the trials
    #dungeons has a list of all of the dungeons
    Dictionary=open("Dictionary.txt","w")
    Multi=''
    #TIL seek(0) resets read and I could probably fix up code previously
    h.seek(0)
    j.seek(0)
    TrialLine=h.read()
    DungeonLine=j.read()
    h.close
    j.close
    NextTrial=0
    NextDungeon=0
    NextEvent=-1
    test=True
    for i in range(len(quests)):
        QuestsSearch=quests[i]+"\n"

        TrialSearch=re.search(QuestsSearch,TrialLine)
        DungeonSearch=re.search(QuestsSearch,DungeonLine)
        if(TrialSearch!=None):
            Multi="T"
        elif(DungeonSearch!=None):
            Multi="D"
        else:
            Multi="N"
        trackDungeon=0
        trackTrial=0
        if(NextEvent==-1):
            while((trackTrial+i)!=len(quests)-1 and quests[trackTrial+i]!=trials[NextTrial]):
                trackTrial+=1
            while((trackDungeon+i)!=len(quests) and quests[trackDungeon+i]!=dungeons[NextDungeon]):
                trackDungeon+=1
            if(trackDungeon<trackTrial):
                NextDungeon+=1
                NextEvent=trackDungeon
            elif(trackTrial<trackDungeon):
                NextTrial+=1
                NextEvent=trackTrial
            elif(trackTrial==trackDungeon):
                NextDungeon+=1
                NextTrial+=1
                NextEvent=trackDungeon
            else:
                NextEvent=-1
        Dictionary.write('"'+quests[i]+'"'+':''['+'"'+questsName[i]+'"'+','+'"'+str(i+1)+'"'+','+'"'+str(NextEvent)+'"'+','+'"'+Multi+'"'+'],\n')
        NextEvent=NextEvent-1





    Dictionary.close
main()