
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
