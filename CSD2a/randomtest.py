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


timestamp1=[1,2,3,4,5,6,7,8,9,10]
timestamp2=[2,4,6,8,10]
timestamp3=[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

tijdtoen=time.time()+timestamp1[0]
kick.play()

i1=0
i2=0
i3=0
count=0
tijdtoen2 = time.time()
kickdone = 0
snaredone = 0
hatdone = 0
print('lengte',len(timestamp2))
while True:
    #test counter
    # if (time.time()-tijdtoen2) >= 1:
    #     tijdtoen2 = time.time()
    #     count = count + 1
    #     print(count)
        


    tijdnu = time.time()

 

    # kick
    if (tijdnu - tijdtoen) >= timestamp1[i1] and (kickdone==0) :
        print('kick',i1,(tijdnu - tijdtoen),kickdone)
        kick.play()
        
        if i1 == (len(timestamp1)-1):
            kickdone = 1
            print('nice')
            

        else:
            i1 = i1 + 1
    
    # snare
    if (tijdnu - tijdtoen) >= timestamp2[i2] and (snaredone==0) :
        print('snare',i2,(tijdnu - tijdtoen),snaredone)
        snare.play()
        
        if i2 == (len(timestamp2)-1):
            snaredone = 1
            print('nice1')
            

        else:
            i2 = i2 + 1

    # hat
    if (tijdnu - tijdtoen) >= timestamp3[i3] and (hatdone==0) :
        print('hat',i3,(tijdnu - tijdtoen),hatdone)
        hat.play()
        
        if i3 == (len(timestamp3)-1):
            hatdone = 1
            print('nice2')
            

        else:
            i3 = i3 + 1




        



    
    if (kickdone==1)and(snaredone==1):
        tijdtoen=tijdnu
        print('zeerlekker')
        kickdone=0
        snaredone=0
        hatdone=0
        i1=0
        i2=0
        i3=0

    time.sleep(0.01)
