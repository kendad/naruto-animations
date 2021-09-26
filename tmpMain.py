import pygame
import os
import kakashi
import naruto
import os

SCREEN_WIDTH=1000
SCREEN_HEIGHT=1000

pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()

#Sound
rashen_shuriken_sound=pygame.mixer.Sound(os.path.join('assets','rashen_shuriken.mp3'))
rasengan_sound=pygame.mixer.Sound(os.path.join('assets','rasengan_3.wav'))

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('NarutoTrial')

isGameRunning=True

sprite_sheet_image=pygame.image.load(os.path.join('assets','kakashi.png')).convert_alpha()


BG=(0,0,0)
#animation-setUp-values
frame=0
last_update=pygame.time.get_ticks()
animation_cooldown=80

#Naruto
naruto_obj=naruto.Naruto()
naruto_rashen_shuriken=naruto_obj.rashen_shuriken()
naruto_rashen_shuriken_animation_end=False
naruto_xPos=100

#ShurikenPathEffect
shuriken_path=naruto_obj.shuriken_path()
shuriken_path_xPos=150
frame_shuriken_effect=0
last_update_shuriken_effect=pygame.time.get_ticks()
animation_cooldown_shuriken_effect=80
shuriken_path_animation_end=False

#ShurikenBlastEffect
shuriken_blast=naruto_obj.shuriken_blast(1)
frame_shuriken_blast=0
last_update_shuriken_blast=pygame.time.get_ticks()
animation_cooldown_shuriken_blast=80
shuriken_blast_scale=10
shuriken_blast_timing=pygame.time.get_ticks()

#shurikenBlastGroundEffect
shuriken_blast_ground=naruto_obj.shuriken_blast_ground_effect()


while isGameRunning:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isGameRunning=False
    screen.fill(BG)

    #1->Rashen Shuriken
    if naruto_rashen_shuriken_animation_end==False:
        current_time=pygame.time.get_ticks()
        if current_time-last_update>=animation_cooldown:
            frame+=1
            last_update=current_time
            if frame >=len(naruto.rashen_shuriken_frame_info):
                frame=0
        #if frame>=16:
        pygame.mixer.Sound.play(rashen_shuriken_sound)
        rashen_shuriken=naruto_rashen_shuriken.get_image(frame)
        screen.blit(rashen_shuriken,(100,250))
    else:
        naruto_xPos-=50
        rashen_shuriken=naruto_rashen_shuriken.get_image(44)
        screen.blit(rashen_shuriken,(naruto_xPos,250))
    
    #2->Shuriken_Path
    if frame==58 and shuriken_path_animation_end==False:
        naruto_rashen_shuriken_animation_end=True
        current_time_shuriken_effect=pygame.time.get_ticks()
        if current_time_shuriken_effect-last_update_shuriken_effect>=animation_cooldown_shuriken_effect:
            shuriken_path_xPos+=50
            if shuriken_path_xPos>=650:
                shuriken_path_animation_end=True
            frame_shuriken_effect+=1
            last_update_shuriken_effect=current_time_shuriken_effect
            if frame_shuriken_effect >=len(naruto.shuriken_path_frame_info):
                frame_shuriken_effect=0
        shuriken_path_effect=shuriken_path.get_image(frame_shuriken_effect)
        screen.blit(shuriken_path_effect,(shuriken_path_xPos,250))
    
    #3->Shuriken  blast
    if shuriken_path_xPos>=650:
        #pygame.mixer.Sound.play(rasengan_sound)
        rashen_shuriken_sound.stop()
        rasengan_sound.play()
        current_time_shuriken_blast=pygame.time.get_ticks()
        shuriken_blast_scale+=1
        if current_time_shuriken_blast-last_update_shuriken_blast>=animation_cooldown_shuriken_blast:
            frame_shuriken_blast+=1
            last_update_shuriken_blast=current_time_shuriken_blast
        if frame_shuriken_blast >=len(naruto.shuriken_blast_frame_info):
                frame_shuriken_blast=0
        shuriken_blast_effect=shuriken_blast.get_image(frame_shuriken_blast)
        shuriken_blast_ground_effect=shuriken_blast_ground.get_image(frame_shuriken_blast)
        screen.blit(shuriken_blast_effect,(600,200))
        screen.blit(shuriken_blast_ground_effect,(650,300))#550,150



    pygame.display.update()
    clock.tick(60)