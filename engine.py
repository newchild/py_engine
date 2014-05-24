#MiyuSoft License v1.3 
#Copyright Â©2014 MiyuSoft 
#http://miyusoft.tk/?page/license/ for more info. 
#All files on http://dl.miyusoft.tk are also covered by this license 

#-MIYUSOFT LICENSE TERMS AND CONDITIONS- 

#All software, code and content covered by this license comes with 
#absolutely NO WARRANTY. MiyuSoft is not liable for any damage or other 
#issues caused by the software, code or other content 
#1. Software, code and other content by MiyuSoft may only be distributed or modified 
#if permission is given to do so. If permission is not 
#given then any MiyuSoft content may not be distributed or modified. MiyuSoft may state 
#permission to do so on open source projects. 
#By default, MiyuSoft content may not be distributed or modified. 
#If MiyuSoft gives permission then YOU MUST give FULL credit to MiyuSoft and supply full source 
#code(if original source code available from MiyuSoft). YOU MUST also 
#link to the original source code from MiyuSoft (if available) as well as your
#own version. Also YOU MUST provide proof that 
#that you are allowed to distribute and modify 
#MiyuSoft content. 

#2. If you are allowed to distribute or modify MiyuSoft code, software or other content 
#YOU MUST include a copy of this License COMPLETELY UNMODIFIED 
#and the MiyuSoft copyright (Copyright Â©MiyuSoft). 
#Also YOU MUST NOT obfuscate code in any way. 

#3. YOU MUST NOT claim any code or software or content by MiyuSoft as 
#your own. All code, software and content from the MiyuSoft team is
#Copyright Â©MiyuSoft. 

#4. YOU MUST NOT sell code, software or content by MiyuSoft. All 
#Miyusoft code and software MUST be completely free. MiyuSoft reserves 
#the right to sell content. 

#Failure to comply with any and/ or all of these will automaticaly
#TERMINATE YOUR RIGHTS TO THIS LICENSE. YOU MUST NOT
#modify and/ or circumvent this license in any way. 

#-END OF TERMS AND CONDITIONS- 

#Copyright ©MiyuSoft 2014


class Entity(object):
    def __init__(self,Name,Damage,Defense,Health,Level=1):
        self.Name=Name
        self.Damage=Damage
        self.Defense=Defense
        self.Health=Health
        self.deathstate=False
        self.xp=0
        self.Level=Level
        self.maxHealth=Health
    def getInfo(self):
        print('Name =', self.Name,'Health =', self.Health,'Defense =',self.Defense,'Damage =', self.Damage,'Dead?', self.deathstate)
        print('Name =', self.Name,'Level =',self.Level,'xp =',self.xp,'Xp left =', ((self.Level*10)-self.xp),'Health =', self.Health, 'Max Health =', self.maxHealth)
    def Attack(self,ziel):
        if self.deathstate:
            print('already dead. Cannot Attack')
        elif ziel.Health<=0:
                ziel.die()
        elif (self.Damage-ziel.Defense)>=0:
            ziel.Health=ziel.Health-(self.Damage-ziel.Defense)
        else:
            ziel.Health=ziel.Health
    def die(self):
        print(self.Name,'died')
        self.deathstate=True
    def getState(self):
        return self.deathstate
    def getXP(self):
        return self.xp
    def heal(self):
        from random import randint
        if self.Health<self.maxHealth:
                x=1
                st=int(1+(self.Level*0.6))
                en=int(10+(self.Level*0.6))
                while x < randint(st,en) and self.Health<self.maxHealth:
                    self.Health+=1
                    x+=1
                    print('Healed', x)
        else:
            print('already fully healed')
    def ki(self,target,mode='easy'):
        from random import randint
        if mode=='easy':
            helper=randint(1,100)
            if helper <= 20:
                self.heal()
                state='healed'
            elif helper > 20:
                self.Attack(target)
                state='attacked'
            print(self.Name, state)
    def Level_Up(self):
            self.Level+=1
            self.xp=0
            self.Damage+=(randint(1,5)+(ent1.Level*1.2))
            self.Defense+=(randint(1,3)+(ent1.Level*1.2))
            self.maxHealth+=(randint(10,30)+(ent1.Level*1.2))
