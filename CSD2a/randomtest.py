import random
import simpleaudio as sa
import wave
import time



wave_read = wave.open('CSD2a/Kick.wav', 'rb')
kick = sa.WaveObject.from_wave_read(wave_read)

wave_read = wave.open('CSD2a/Snare.wav', 'rb')
snare = sa.WaveObject.from_wave_read(wave_read)

wave_read = wave.open('CSD2a/Hat.wav', 'rb')
hat = sa.WaveObject.from_wave_read(wave_read)


timestamp1=[]
timestamp2=[]
timestamp3=[]
randval1=[]
randval2=[]
randval3=[]



bpm = int(input('BPM: '))
if bpm < 0 :
    bpm = bpm* (-1)
interval16 = 60/bpm
lengthall=interval16*16
print(interval16)
print(lengthall)

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
    if  randomness< 0.3:

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
    randomness=(random.random())
    if  randomness< 0.4:

        randval3.append(0)
    else:
        randval3.append(1)




tijdtoen=time.time()

i1=0
i2=0
i3=0


kickdone = 0
snaredone = 0
hatdone = 0
loopcount = 0

print('lengte',len(timestamp2))

print("\n")
for i in range(0,len(randval1)):
    print(randval1[i])
print(randval1)
print(timestamp1)
print("\n")
print(randval2)
print(timestamp2)
print("\n")
print(randval3)
print(timestamp3)
print("\n")



while True:

    tijdnu = time.time()

 

    # kick
    if (tijdnu - tijdtoen) >= timestamp1[i1] and (kickdone==0):

        if randval1[i1]==1:
            print('kick',i1)
            kick.play()
        
        if i1 == (len(timestamp1)-1):
            kickdone = 1
            print('nice')
        else:
            i1 = i1 + 1
            
    
    # snare
    if (tijdnu - tijdtoen) >= timestamp2[i2] and (snaredone==0) :
        
        if randval2[i2]==1:
            print('snare',i2)
            snare.play()
        
        if i2 == (len(timestamp2)-1):
            snaredone = 1
            print('nice1')
            

        else:
            i2 = i2 + 1

    # hat
    if (tijdnu - tijdtoen) >= timestamp3[i3] and (hatdone==0) :
        
        if randval3[i3]==1:
            print('hat',i3)
            hat.play()
        
        if i3 == (len(timestamp3)-1):
            hatdone = 1
            print('nice2')
            

        else:
            i3 = i3 + 1


    if (tijdnu - tijdtoen) >= lengthall:
        tijdtoen=tijdnu
        print('zeerlekker')
        kickdone=0
        snaredone=0
        hatdone=0
        i1=0
        i2=0
        i3=0
        loopcount += 1
        print('loopcount= ',loopcount)
        if loopcount>1:
            loopcount=0
            input("Loop=l Save=s")
            tijdtoen=time.time()
        



    time.sleep(0.001)

print('epic')

time.sleep(1)
