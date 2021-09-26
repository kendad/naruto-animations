import pygame
import os
import kakashi

SCREEN_WIDTH=500
SCREEN_HEIGHT=500

pygame.init()
clock=pygame.time.Clock()

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('NarutoTrial')

isGameRunning=True

sprite_sheet_image=pygame.image.load(os.path.join('assets','kakashi.png')).convert_alpha()


BG=(50,50,50)
#animation-setUp-values
frame=0
last_update=pygame.time.get_ticks()
animation_cooldown=80

#Kakashi
kakashi_obj=kakashi.Kakashi()
kakashi_kunaie_slash=kakashi_obj.kunaie_slash()
kakashi_transmission_into_tree=kakashi_obj.transmission_into_tree()
kakashi_chidori=kakashi_obj.chidori()
chidori_text=kakashi_obj.chidori_text()
chidori_spark=kakashi_obj.chidori_spark()

while isGameRunning:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isGameRunning=False
    screen.fill(BG)

    #update animation
    #1-->Kunaie Slash Animation
    # current_time=pygame.time.get_ticks()
    # if current_time-last_update>=animation_cooldown:
    #     frame+=1
    #     last_update=current_time
    #     if frame >=len(kakashi.kunai_slash_frame_info):
    #         frame=0
    # kunaie_slash=kakashi_kunaie_slash.get_image(frame)
    # screen.blit(kunaie_slash,(20,20))


    #2-->kakashi_transmission_into_tree
    # current_time=pygame.time.get_ticks()
    # if current_time-last_update>=animation_cooldown:
    #     frame+=1
    #     last_update=current_time
    #     if frame >=len(kakashi.transmission_frame_info):
    #         frame=0
    # tree_transformation=kakashi_transmission_into_tree.get_image(frame)
    # screen.blit(tree_transformation,(20,20))

    #3-->kakashi_chidori
    current_time=pygame.time.get_ticks()
    if current_time-last_update>=animation_cooldown:
        frame+=1
        last_update=current_time
        if frame >=len(kakashi.chidori_frame_info):
            frame=0
    chidori=kakashi_chidori.get_image(frame)
    screen.blit(chidori,(500/2,500/2))

    if frame>=11 and frame<=22:
        xPos=0
        chidori_text_effect=chidori_text.get_image(0)
        if frame%2==0:
            xPos=170
        else:
            xPos=165

        screen.blit(chidori_text_effect,(xPos,330))
    
    if frame==26:
        chidori_spark_effect=chidori_spark.get_image(0)
        screen.blit(chidori_spark_effect,(350,250))
    if frame==27:
        chidori_spark_effect=chidori_spark.get_image(1)
        screen.blit(chidori_spark_effect,(350,250))

    pygame.display.update()
    clock.tick(60)