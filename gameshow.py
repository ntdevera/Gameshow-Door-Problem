import random

counter1=0
counter2=0
counter3=0
stay=0
oldswitch=0
switch=0
staycounter=0
switchcounter=0
k=1000

   

for i in range(k):
    goatdoor=random.randint(1,3)
    stay=random.randint(1,3)
    switch=random.randint(1,3)
    gameclue=random.randint(1,3)
    if goatdoor==1:
        counter1+=1
    if goatdoor==2:
        counter2+=1
    if goatdoor==3:
        counter3+=1

    stay=random.randint(1,3)
    switch=random.randint(1,3)
    if stay==goatdoor:
        staycounter+=1

    while gameclue==switch or gameclue==goatdoor: 
        gameclue=random.randint(1,3)

    oldswitch=switch

    while switch==oldswitch or switch==gameclue:
        switch=random.randint(1,3)
    print(oldswitch,gameclue,switch,goatdoor) 

    if switch==goatdoor:
        switchcounter+=1


print("counter1 = ", counter1,"counter2 = ", counter2,"counter3 = ", counter3)
print("switch points = ", switchcounter,"stay points = ", staycounter)



if(switchcounter>staycounter):
    print("switch is better by ",switchcounter/staycounter*100, "percent")
if(staycounter>switchcounter):
    print("stay is better by ",staycounter/switchcounter*100, "percent")