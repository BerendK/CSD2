import random
import time

randval1=[]
randval2=[]
randval3=[]

timestamp1=[]
timestamp2=[]
timestamp3=[]






# def genratelists(amount,maat1,maat2,maat3)   
#     for i in range(0,maat1):
#         thing = random.random()*amount
#         randval1.append(thing)
#     for i in range(0,maat2):
#         thing = random.random()*amount
#         randval2.append(thing)
#     for i in range(0, maat3):
#         thing= random.random()*amount
#         randval3.append(thing)




bpm = int(input('BPM: '))
if bpm < 0 :
    bpm = bpm* (-1)
interval16 = 60/bpm
lengthall=interval16*16
print(interval16)
print(lengthall)

# loopamount=int(input('hoevaak loopen?: '))
# if loopamount < 0 :
#     loopamount = loopamount* (-1)
# print(loopamount)


kickgrid=int(input('Kick grid: '))
if kickgrid < 0 :
    kickgrid = kickgrid* (-1)
snaregrid=int(input('Snare grid: '))
if snaregrid < 0 :
    snaregrid = snaregrid* (-1)
hatgrid=int(input('Hat grid: '))
if snaregrid < 0 :
    snaregrid = snaregrid* (-1)




for i in range(0,kickgrid):
    kickinterval = lengthall/kickgrid
    timestamp1.append(kickinterval*i)
    randomness=(random.random()/(((i) % (kickgrid/4))+1))
    if  randomness< 0.4:

        randval1.append(0)
    else:
        randval1.append(1)


for i in range(0,snaregrid):
    snareinterval = lengthall/snaregrid
    timestamp2.append(snareinterval*i)
    randomness=(random.random()/(((i) % (snaregrid/2))+1))
    if  randomness< 0.2:

        randval2.append(0)
    else:
        randval2.append(1)


for i in range(0,hatgrid):
    hatinterval = lengthall/hatgrid
    timestamp3.append(hatinterval*i)
    randomness=(random.random()/(((i) % (hatgrid/8))+1))
    if  randomness< 0.2:

        randval3.append(0)
    else:
        randval3.append(1)
    





# genratelists(1,int(input('maat1: ')),int(input('maat2: ')),int(input('maat3: ')))

print("\n")
print(randval1)
print(timestamp1)
print("\n")
print(randval2)
print(timestamp2)
print("\n")
print(randval3)
print(timestamp3)
print("\n")
# loopsave=input('loop=l save=s: ')
# if loopsave=='l':
#     print('loop')
# elif loopsave=='s':
#     print('saved')
# else:
#     print('invalid response')

