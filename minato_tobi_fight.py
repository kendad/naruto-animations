import pygame
import minato
import tobi

import os

SCREEN_WIDTH=1000
SCREEN_HEIGHT=1000

pygame.init()
clock=pygame.time.Clock()

#music
pygame.mixer.init()
pygame.mixer.music.load(os.path.join('assets','minato_updated.mp3'))
pygame.mixer.music.play(-1,0.0)
blast_sound=pygame.mixer.Sound(os.path.join('assets','m_t_fight_wav.wav'))

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('NarutoTrial')

isGameRunning=True

BG=(50,50,50)
BG=(0,0,0)


################################################################################
#MINATO
minato_obj=minato.Minato()
minato_posX=20
minato_posY=300
minato_velocity=15

#minato_intro
minato_intro=minato_obj.minato_intro()
minato_frame=0
minato_last_update=pygame.time.get_ticks()
minato_animation_cooldown=80
MINATO_INTRO_ANIMATION_ACTIVE=True

#minato standing
minato_standing=minato_obj.minato_standing()
minato_standing_frame=0
minato_standing_last_update=pygame.time.get_ticks()
minato_standing_animation_cooldown=80
MINATIO_STANDING_ANIMATION_ACTIVE=False


#minato running
minato_running=minato_obj.minato_running()
minato_running_frame=0
minato_running_last_update=pygame.time.get_ticks()
minato_running_animation_cooldown=80
MINATO_RUNNING_ANIMATION_ACTIVE=False

#blast
blast=minato_obj.blast()
blast_frame=0
blast_last_update=pygame.time.get_ticks()
blast_animation_cooldown=80
blast_scale=1
BLAST_ANIMATION_ACTIVE=False

#ground effect
ground=minato_obj.ground_effect()
ground_frame=0
ground_last_update=pygame.time.get_ticks()
ground_animation_cooldown=80
ground_scale=1
GROUND_ANIMATION_ACTIVE=False
###############################################################################################

######################################################################
#TOBI
tobi_obj=tobi.Tobi()
tobi_posX=950
tobi_posY=310
tobi_velocity=20

#tobi standing
tobi_standing=tobi_obj.tobi_standing()
tobi_standing_frame=0
tobi_standing_last_update=pygame.time.get_ticks()
tobi_standing_animation_cooldown=80
TOBI_STANDING_ANIMATION_ACTIVE=True

#########################################################################################


while isGameRunning:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isGameRunning=False
    screen.fill(BG)

    #1-->Minato Intro
    if MINATO_INTRO_ANIMATION_ACTIVE==True:
        minato_current_time=pygame.time.get_ticks()
        if minato_current_time-minato_last_update>=minato_animation_cooldown:
            minato_frame+=1
            minato_last_update=minato_current_time
            if minato_frame >=len(minato.minatio_intro_frame_info):
                MINATO_INTRO_ANIMATION_ACTIVE=False
                MINATIO_STANDING_ANIMATION_ACTIVE=True
                minato_frame=len(minato.minatio_intro_frame_info)-1
        minato_intro_animation=minato_intro.get_image(minato_frame)
        screen.blit(minato_intro_animation,(minato_posX,minato_posY))


    #2-->Minato Standing
    if MINATIO_STANDING_ANIMATION_ACTIVE==True:
        minato_standing_current_time=pygame.time.get_ticks()
        if minato_standing_current_time-minato_standing_last_update>=minato_standing_animation_cooldown:
            minato_standing_frame+=1
            minato_standing_last_update=minato_standing_current_time
            if minato_standing_frame >=len(minato.minato_standing_frame_info):
                minato_standing_frame=0
        minato_standing_animation=minato_standing.get_image(minato_standing_frame)
        screen.blit(minato_standing_animation,(minato_posX,minato_posY))

    #Minato Running
    if tobi_standing_frame>=17:
        MINATO_RUNNING_ANIMATION_ACTIVE=True
        MINATIO_STANDING_ANIMATION_ACTIVE=False

    if MINATO_RUNNING_ANIMATION_ACTIVE==True:
        minato_posX+=minato_velocity
        minato_running_current_time=pygame.time.get_ticks()
        if minato_running_current_time-minato_running_last_update>=minato_running_animation_cooldown:
            minato_running_frame+=1
            minato_running_last_update=minato_running_current_time
            if minato_running_frame >=len(minato.minato_running_frame_info):
                minato_running_frame=0
            
            if minato_running_frame>=8:
                minato_posY=100
                minato_velocity=0
            if minato_running_frame>=15:
                BLAST_ANIMATION_ACTIVE=True
        minato_running_animation=minato_running.get_image(minato_running_frame)
        screen.blit(minato_running_animation,(minato_posX,minato_posY))

    
    #Blast
    if BLAST_ANIMATION_ACTIVE==True:
        blast_sound.play()
        GROUND_ANIMATION_ACTIVE=True
        blast_current_time=pygame.time.get_ticks()
        if blast_current_time-blast_last_update>=blast_animation_cooldown:
            blast_frame+=1
            blast_last_update=blast_current_time
            if blast_frame >=len(minato.blast_frame_info):
                blast_frame=0
            blast_scale+=1
            if blast_scale>=3:
                blast_scale=3
        blast_animation=blast.get_image(blast_frame,blast_scale)
        screen.blit(blast_animation,(minato_posX-200,minato_posY-50))
    
    #Ground Effect
    if GROUND_ANIMATION_ACTIVE==True:
        ground_current_time=pygame.time.get_ticks()
        if ground_current_time-ground_last_update>=ground_animation_cooldown:
            ground_frame+=1
            ground_last_update=ground_current_time
            if ground_frame >=len(minato.ground_frame_info):
                ground_frame=0
        ground_animation=ground.get_image(ground_frame,2)
        screen.blit(ground_animation,(minato_posX-130,minato_posY+200))

    
    #Tobi Standing
    if TOBI_STANDING_ANIMATION_ACTIVE==True:
        tobi_standing_current_time=pygame.time.get_ticks()
        if tobi_standing_current_time-tobi_standing_last_update>=tobi_standing_animation_cooldown:
            tobi_standing_frame+=1
            tobi_standing_last_update=tobi_standing_current_time
            if tobi_standing_frame >=len(tobi.tobi_standing_frame_info):
                tobi_standing_frame=0
            if tobi_standing_frame>=17:
                tobi_posX-=tobi_velocity
            if tobi_standing_frame>=34:
                tobi_velocity=0
            if minato_running_frame>=17:
                tobi_posY=minato_posY+200
                tobi_posX=minato_posX+50
        tobi_standing_animation=tobi_standing.get_image(tobi_standing_frame)
        screen.blit(tobi_standing_animation,(tobi_posX,tobi_posY))

    pygame.display.update()
    clock.tick(60)