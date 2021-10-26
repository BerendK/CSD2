import random
import simpleaudio as sa
import wave
import time
import math
from midiutil import MIDIFile

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
    print('length of your loop will be set by BPM')
    bpm = int(input('BPM: ')or 360)
    if bpm < 0 :
        bpm = bpm* (-1)
    
    # calculating length of loop
    lengthall=(60/bpm)*32
    print('loop lengte:',lengthall,' Seconden')
    print('you can get diffrent time signatures if you fill in all 7,s for 7/8')
    print('(or optionally all whole multiples of 7) ')
    print('so any timesignature you want!')
# you can get diffrent time signature's if you fill in all 7's for 7/8 (or optionally all whole multiples of 7).so any timesignature you want
# it deafaults to a grid of 32 so thats 4/4.')
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
    loopamount = int(input('hoevaak wil je loopen: ')or 2)
    if loopamount < 0 :
        loopamount = loopamount* (-1)


    print('\n\n\n\n\n\n\n\n\n\n')
    print('lets play')



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
        randomness=(random.random()/(((i) % (hatgrid/8))+1))
        if  randomness< 0.2:

            randval3.append(0)
        else:
            randval3.append(1)


    #----------------- play! -------------------
    # setting/resetting a bunch of things
    # varible with time to eliminate sync isues 
    tijdtoen=time.time()+1

    # index variables
    i1=0
    i2=0
    i3=0
    
    # done?
    kickdone = 0
    snaredone = 0
    hatdone = 0
    # current loop amount
    loopcount = 0

    # lets play
    play=1
    while (play == 1):
        # current time in variable for better sync
        tijdnu = time.time()

    

        # KICK Runs every time a grid position passes
        if (tijdnu - tijdtoen) >= timestamp1[i1] and (kickdone==0):
            # play it when the algoritm thinks its right
            if randval1[i1]==1:
               
                kick.play()
            # stop if this was the last index
            if i1 == (len(timestamp1)-1):
                kickdone = 1
            
            else:
                # just iterate normaly
                i1 = i1 + 1
                
        
        # SNARE Runs every time a grid position passes
        if (tijdnu - tijdtoen) >= timestamp2[i2] and (snaredone==0) :
            # play it when the algoritm thinks its right
            if randval2[i2]==1:
                snare.play()

            # stop if this was the last index
            if i2 == (len(timestamp2)-1):
                snaredone = 1
                
                

            else:
                # just iterate normaly
                i2 = i2 + 1

        # HIHAT Runs every time a grid position passes
        if (tijdnu - tijdtoen) >= timestamp3[i3] and (hatdone==0) :
             # play it when the algoritm thinks its right
            if randval3[i3]==1:
                
                hat.play()
             # stop if this was the last index
            if i3 == (len(timestamp3)-1):
                hatdone = 1
            else:
                # just iterate normaly
                i3 = i3 + 1

        # reset things after everything has been played
        if (tijdnu - tijdtoen) >= lengthall:
            tijdtoen=tijdnu
            kickdone=0
            snaredone=0
            hatdone=0
            i1=0
            i2=0
            i3=0

            loopcount += 1

            # this runs if all the loops have been played
            if loopcount>=loopamount:
                loopcount=0
                # asking what to do
                print('\n\n\n\n\n\n\n\n\n\n')
                print('maak een keuze:')
                loopsavenew = input("Loop=l Save=s New=n :")
                # checking input
                if (loopsavenew=='l'):
                    print('speciaal voor jouw')
                    # resume playing same loop
                elif (loopsavenew=='s'):
                    # midifile generation
                    # begin time at 0 and turn the volume up
                    mf = MIDIFile(1)
                    tim = 0
                    volume = 127
                    # add name and tempo
                    mf.addTrackName(0, tim, "beats voor eindopdracht")
                    mf.addTempo(0, tim, bpm)

                    # note length based on grid spacing
                    dur1 = 32/kickgrid
                    dur2 = 32/snaregrid
                    dur3 = 32/hatgrid

                    # generate all notes
                    for i in range(0,len(timestamp1)):
                        # checks if the note should've been played
                        if randval1[i]==1:
                            # then add it
                            mf.addNote(0,0,60,tim, dur1,volume)
                        # increase the timeline
                        tim = tim + dur1
                    # reset before next list
                    tim=0

                    # same thing difrent lists
                    for i in range(0,len(timestamp2)):
                        if randval2[i]==1:
                            
                            mf.addNote(0,0,61,tim, dur2,volume)
                        tim = tim + dur2
                    tim=0
                    # same thing difrent lists
                    for i in range(0,len(timestamp3)):
                        if randval3[i]==1:
                            
                            mf.addNote(0,0,62,tim, dur3,volume)
                        tim = tim + dur3
                    

                    # write to file

                    with open("randommidi.mid",'wb') as outf:
                        mf.writeFile(outf)
                    # indicate user
                    print('hijs opgeslagen')
                    # make another one
                    play = 0
                
                elif (loopsavenew== 'n'):

                    print ('ok rustig, ik probeer opnieuw')
                    # make another one
                    play = 0
                else:
                    # if you cant type you may as wel leave
                    print('gabber typ normaal')
                    quit()
                    
                # finally reset the second time variable
                tijdtoen=time.time()
               
            


        # i like my computing box so i let it rest sometimes
        time.sleep(0.001)

# i realize now that i din't use any functions because i din't use any peace of code more than 3 times.
# i did begin with multiple but deleted them because i found it to be just as messy.
# also i used lists instead of a dictionary, because i think those are faster and easyer to spot.

# length of your loop will be set by BPM
# you can get diffrent time signature's if you fill in all 7's for 7/8 (or optionally all whole multiples of 7).so any timesignature you want
# it deafaults to a grid of 32 so thats 4/4.

# i left this out becouse i want the option to do weird things and see what happens



