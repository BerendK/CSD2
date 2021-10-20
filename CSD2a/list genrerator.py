import random
import time

randval1=[]
randval2=[]
randval3=[]

timestamp1=[]
timestamp2=[]
timestamp3=[]

def genratetimestamps(bpm,maat1,maat2,maat3):
    for i in range(0,maat1):
        timestamp1.append()

def genratelists(amount,maat1,maat2,maat3):
    
    for i in range(0,maat1):
        thing = random.random()*amount
        randval1.append(thing)
    for i in range(0,maat2):
        thing = random.random()*amount
        randval2.append(thing)
    for i in range(0, maat3):
        thing= random.random()*amount
        randval3.append(thing)




bpm = input('BPM: ')
bpm=int(bpm)




genratelists(1,int(input('maat1: ')),int(input('maat2: ')),int(input('maat3: ')))

print("\n")
print(randval1)
print("\n")
print(randval2)
print("\n")
print(randval3)
print("\n")
loopsave=input('loop=l save=s: ')
if loopsave=='l':
    print('loop')
elif loopsave=='s':
    print('save')
else:
    print('invalid response')

