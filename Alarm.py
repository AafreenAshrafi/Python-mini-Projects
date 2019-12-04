#Alarm
import string
import pygame
pygame.mixer.init()
pygame.init()
from time import sleep
option = 0
##test
def wu():
 musically = pygame.mixer.Sound("C:/Users/aafreen.ashrafi/Desktop/python/analog-watch-alarm_daniel-simion.wav")
 musically.play()
 global option
 option = input('''
    select:  1) to snooze
             OR
             any key to diable alarm
           ''')


print('welcome to Alarm')
m = int(input('enter the no of minutes after which the alarm has to run '))

if (m >= 0):
    s = 60* m
    print('no of seconds it has to sleep ' +str(s))
    sleep (s)
    # Call function horn sound
    wu()
    
    #horn sound
    while True:
     if( option == '1'):
        pygame.mixer.stop()
        print('Alarm Snoozed after 5 seconds it will play again')
        sleep (5)
        wu()
        #Call function horn sound OR print('Wake up')
     else :
        print('user interupted so Alarm Disabled')
        pygame.mixer.stop()
        break;
      
    
    
else:
  print('input is invalid')

