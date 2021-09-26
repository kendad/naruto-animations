import pygame
import os

SCREEN_WIDTH=300
SCREEN_HEIGHT=240

pygame.init()
clock=pygame.time.Clock()

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('NarutoTrial')


sprite_sheet_image=pygame.image.load(os.path.join('assets','kakashi.png')).convert_alpha()

isGameRunning=True

BG=(50,50,50)
SPRITE_BG_COLOR=(0,128,0)#sprite sheet background Color

#kakashi-kunaieAttack1
kakashi_kunai_attack_frame_info=[
    [534,3447,34,44],
    [582,3441,32,50],
    [633,3448,42,43],
    [687,3423,43,68],
    [753,3427,48,64],
    [821,3435,54,56],
    [891,3436,46,53],
    [955,3444,36,47]
]

def get_image(sheet,frame,scale,color):

    starting_X=kakashi_kunai_attack_frame_info[frame][0]
    starting_Y=kakashi_kunai_attack_frame_info[frame][1]
    width=kakashi_kunai_attack_frame_info[frame][2]
    height=kakashi_kunai_attack_frame_info[frame][3]

    image=pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet,(0,0),(starting_X,starting_Y,width,height))
    image=pygame.transform.scale(image,(scale*width,scale*height))
    image.set_colorkey(color)
    return image


frame=0
last_update=pygame.time.get_ticks()
animation_cooldown=80


while isGameRunning:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isGameRunning=False
    screen.fill(BG)
    #update animation
    current_time=pygame.time.get_ticks()
    if current_time-last_update>=animation_cooldown:
        frame+=1
        last_update=current_time
        if frame >=len(kakashi_kunai_attack_frame_info):
            frame=0

    kunaie_attack=get_image(sprite_sheet_image,frame,2,SPRITE_BG_COLOR)

    screen.blit(kunaie_attack,(20,20))
    pygame.display.update()
    clock.tick(60)