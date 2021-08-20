# This a geme to find write number
import random
def level_choose():
    level=0
    print("Choose the level difficulty:\n 1-Easy(1-10)\n 2-Normal(1-100)\n 3-Hard (1-1000)")
    level = input()
    level=level.lower()
    print(level)
    if (level == '1' or level == 'easy'):
        return 10
    elif (level == '2' or level == 'normal'):
        return 100
    if (level == '3' or level == 'hard'):
        return 1000
    else:
        return 1
print ("Hello")
level=1
while(level==1):
    level = int(level_choose())
print ("level=",level)
target= random.randint(0, level)
number= None
i=0
div=[]
while number != target:
    print("Enter your number from 0 to", level, ": ")
    input_value=input()
    try:
        number=int(input_value)
    except:
        print("Wrong!!\n",input_value , "-not a integer number")
        continue
    if(number>level or number<0):
        print("Wrong range\n")
    div.append(target-number)
    if(div[i]>0):
        print('More')
    elif(div[i]<0):
        print('Less')
    if(i>0 and (abs(div[i])-abs(div[i-1]))<0 and number!=target):
        print("Hot")
    if(i>0 and (abs(div[i])-abs(div[i-1]))>0 and number!=target):
        print("Cold")
    if (i > 0 and (abs(div[i]) - abs(div[i - 1])) == 0 and number != target):
        print("You are between")
    if(abs(div[i]<(level/10))):
        print("You're very close.")
    if(number==target):
        print('You are Winner')
    i +=1
    print("Try=",i)
