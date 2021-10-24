import random
import simpleaudio as sa
import wave
import time
import math

# Load all samples to be played whenever

wave_read = wave.open('CSD2a/Kick.wav', 'rb')
kick = sa.WaveObject.from_wave_read(wave_read)

wave_read = wave.open('CSD2a/Snare.wav', 'rb')
snare = sa.WaveObject.from_wave_read(wave_read)

wave_read = wave.open('CSD2a/Hat.wav', 'rb')
hat = sa.WaveObject.from_wave_read(wave_read)



# generating and playing evrything

while(True):
    
    # making/resetting some lists to store grid positions of each instrument
    timestamp1=[]
    timestamp2=[]
    timestamp3=[]

    # making/resetting lists to hold data about if a note should be played
    randval1=[]
    randval2=[]
    randval3=[]

        #didn't use dictionary's cause i found it less cluthered this way
    # --------------------------- Input ------------------------------

    # input positive integer BPM
    bpm = int(input('BPM: ')or 360)
    if bpm < 0 :
        bpm = bpm* (-1)
    
    # calculating length of loop
    lengthall=(60/bpm)*16
    print('Bar lengte: ',lengthall,' Seconden')

    # input positive integer Kickgrid, (how many posible kicks in a loop)
    kickgrid=int(input('Kick grid: ')or 32)
    if kickgrid < 0 : kickgrid = kickgrid* (-1)
        
    # input positive integer Snaregrid, (how many posible snares in a loop)
    snaregrid=int(input('Snare grid: ')or 32)
    if snaregrid < 0 : snaregrid = snaregrid* (-1)
        
    # input positive integer Hatgrid, (how many posible hi-hats in a loop)
    hatgrid=int(input('Hat grid: ')or 32)
    if snaregrid < 0 : snaregrid = snaregrid* (-1)
        
    # input positive integer loopamount, (the amount you want your loop looped)
    loopamount = int(input('hoevaak wil je loopen: ')or 4)
    if loopamount < 0 :
        loopamount = loopamount* (-1)


    #------------------- Beat list generator code ---------------------

    # kick generation
    for i in range(0,kickgrid):


        # calculate all timestamps for a possible kick
        kickinterval = lengthall/kickgrid
        timestamp1.append(kickinterval*i)


        # a weird formula for generating repetitive ish chances
        # specifically tuned towards kicks
        randomness= random.random()*(math.cos((2 * math.pi)*(i/(kickgrid/4)))+1)/2
        if  randomness< 0.4:

            randval1.append(0)
        else:
            randval1.append(1)


    for i in range(0,snaregrid):


        # calculate all timestamps for a possible snare
        snareinterval = lengthall/snaregrid
        timestamp2.append(snareinterval*i)


        # a weird formula for generating repetitive ish chances
        # specifically tuned towards snares
        randomness=(random.random()/(((i) % (snaregrid/4))+1))
        if  randomness< 0.2:

            randval2.append(0)
        else:
            randval2.append(1)


    for i in range(0,hatgrid):

        # calculate all timestamps for a possible hat
        hatinterval = lengthall/hatgrid
        timestamp3.append(hatinterval*i)


        # a weird formula for generating repetitive ish chances
        # specifically tuned towards hats        
        randomness=(random.random()/(((i) % (hatgrid/2))+1))
        if  randomness< 0.2:

            randval3.append(0)
        else:
            randval3.append(1)




    

    # print all lists for debugging

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

    # setting/resetting a bunch of things
    # varible with time to eliminate sync isues 
    tijdtoen=time.time()+2


    i1=0
    i2=0
    i3=0


    kickdone = 0
    snaredone = 0
    hatdone = 0

    loopcount = 0

    play=1


    while (play == 1):

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
            if loopcount>=loopamount:
                loopcount=0
                
                
                loopsavenew = input("Loop=l Save=s New=n ")
                if (loopsavenew=='l'):
                    print('ait nice')
                elif (loopsavenew=='s'):
                    print('hijs opgeslagen')
                    play = 0
                elif (loopsavenew== 'n'):
                    print ('ok rustig, ik probeer opnieuw')
                    play = 0
                else:
                    print('gabber typ normaal')

                tijdtoen=time.time()
            



        time.sleep(0.001)

