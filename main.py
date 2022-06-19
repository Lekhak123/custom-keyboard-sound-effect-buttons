from pynput.keyboard import Key, Listener
from pygame import mixer
import pygame
mixer.pre_init()
mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
pygame.init()
music_list ={}
channel={}
k=0
while k <9:   
   music_list[k]= mixer.Sound("./audio\\"+str(k)+".mp3") 
   k +=1

keycodes = ["<103>","<104>","<105>","<100>","<101>","<102>","<97>","<98>","<99>"]


def on_press(key):
    keyy = str(key)
    if keyy in keycodes:  
        if mixer.get_busy():
            mixer.stop()
            return
        key_index = keycodes.index(keyy)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(music_list[key_index]))
 
       

with Listener(
        on_press=on_press,
        ) as listener:
    listener.join()







