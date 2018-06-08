#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#-*-title:helper ww-*-

# Parser of pipboy message from 
# telegramm Wastelend Wars game
def parsepip(pipboy):
    d = {}
    count = 0
    # For every strings
    for s in pipboy.split('\n'):
        # Counter for set string number
        count += 1
        
        # add username
        if count == 4:
            key0="uname"
            value0=s
            d[key0]=value0
            
        # line is have ':'
        if s.find(':') != -1:
            
            # find a plase of first delimeter simbol
            f1=s.find(":") 
            key0=s[:f1]
            value0=s[f1+2:]
            
            if s.count(":") == 2:
                # find a plase space simbol.
                # it is a start second key:value pairs
                f2=s[f1+2:].find(" ")
            
                value0=s[f1+2:f1+2+f2]
            
                key1=s[f1+2+f2+1:].split(":")[0]
                value1=s[f1+2+f2+1:].split(":")[1][1:]
            
                d[key1]=value1
                
            d[key0]=value0
        else:
            continue
    return d

#test:
# input message:
pipboy='''
:pager:Пип-бой 3000 v2.01

🛠Технолог Нации
:busts_in_silhouette:Фракция: :bomb:Мегатонна
:heart:Здоровье: 477/438
:poultry_leg:Голод: 17%
⚔Урон: 585 🛡Броня: 211 (+24)

:muscle:Сила: 253 :gun:Меткость: 123
🗣Харизма: 369 🤸🏽♂Ловкость: 194

:battery:Выносливость: 6/9
:fire:Локация: Склады
:footprints:Расстояние: 16

🕳Крышки: 9926
:package:Материалы: 497
:barber:Пупсы: 6

:pager:Подробности /me
🛰Дрон /mydrone
'''
# Example of use of parsepip(message):
test=parsepip(pipboy)

count=0
for i in test:
    print(count,":",i,":",test[i])
    count+=1
    
print(test[":heart:Здоровье"])