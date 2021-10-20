import time
import random
import simpleaudio as sa
import wave

wave_read = wave.open('CSD2a/Kick.wav', 'rb')
kick = sa.WaveObject.from_wave_read(wave_read)

wave_read = wave.open('CSD2a/Snare.wav', 'rb')
snare = sa.WaveObject.from_wave_read(wave_read)

wave_read = wave.open('CSD2a/Hat.wav', 'rb')
hat = sa.WaveObject.from_wave_read(wave_read)


randomlist1 = []
randomlist2 = []
randomlist3 = []
amount1=1
amount2=1
amount3=1
interval1 = 1
interval2 = 1
interval3 = 1
count1 = 0
count2 = 0
count3 = 0
tijdtoen1 =time.time()
tijdtoen2 =time.time()
tijdtoen3 =time.time()







bpm = input('BPM:')
beat = 60/int(bpm)
lengtevol = (beat* 16)
print('Voledige lengte',lengtevol,)





bpmaat1 = input('Beats per maat(kick):')
interval1 = (lengtevol/int(bpmaat1))
bpmaat2 = input('Beats per maat(snare):')
interval2 = (lengtevol/int(bpmaat2))
bpmaat3 = input('Beats per maat(hat):')
interval3 = (lengtevol/int(bpmaat3))

for i in range(0,int(bpmaat1)):
    randomlist1.append(random.random()*amount1)
for i in range(0,int(bpmaat2)):
    randomlist2.append(random.random()*amount2)
for i in range(0,int(bpmaat3)):
    randomlist3.append(random.random()*amount3)



print(randomlist1)

#looks for element in a list
def checklist(list ,value) :
    if(value in list):
        return True




#input list
#input_string = input('gooi nummers in de lijst(met spaties ertussen):')
print("\n")
#user_list = input_string.split()
#print('input: ', user_list)

#convert string to int
#for i in range(0, len(user_list)):
#    user_list[i] = int(user_list[i])



#if(checklist(user_list, 1)):
    #print('very nice')

tijdtoen0 = time.time()
while True:
    tijdnu = time.time()
    #timer bas
    if (tijdnu - tijdtoen1) >= interval1:
        tijdtoen1 = tijdnu
        #print('kick',count1)
        kick.play()
        if randomlist1[count1]<= 0.5:
            
            print("kick",count1,randomlist1[count1])
        count1 += 1
        if count1 >= int(bpmaat1):
            count1=0


    #timer snare
    if (tijdnu - tijdtoen2) >= interval2:
        tijdtoen2 = tijdnu
        #print('snare',count2)
        snare.play()
        #print("snare",count2,randomlist2[count2])
        count2 += 1 
        if count2 >= int(bpmaat2):
            count2=0

        
    #timer hat
    if (tijdnu - tijdtoen3) >= interval3:
        tijdtoen3 = tijdnu
        print('Hat',count3)
        hat.play()
        #print("hat",count3,randomlist3[count3])
        count3 += 1 
        if count3 >= int(bpmaat3):
            count3=0

        
    #als voltijd is geweest reset ik alles teglijkertijd
        

        


    time.sleep(0.01)
        


