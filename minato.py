import pygame
import os
import player

#1-->Minato Introduction
minatio_intro_frame_info=[
    [10,4596,25,42],#kunaie-1
    [60,4590,22,22],#kunaie-2
    [60,4590,22,22],#kunaie-2
    [60,4590,22,22],#kunaie-2
    [105,4572,33,40],#kunaie-3
    [151,4560,67,61],
    [228,4555,74,61],
    [310,4553,76,65],
    [393,4560,65,56],
    [470,4559,62,58],
    [552,4533,22,83],
]

#2-->Minato Stading Stance
minato_standing_frame_info=[
    [10,245,34,83],
    [61,245,42,83],
    [118,245,48,83],
    [180,245,53,83],
]

#3->Minato Running
minato_running_frame_info=[
    [4,354,74,64],
    [88,355,71,63],
    [181,352,61,66],
    [253,355,70,64],
    [330,353,76,65],
    [425,351,64,67],

    #flying ryjin effect--disappearing
    [9,2275,74,65],
    [96,2274,75,57],
    [183,2272,66,62],
    [264,2273,61,59],
    [348,2277,60,58],
    [426,2276,65,64],
    [512,2275,65,65],

    #flying ryjin effect--sappearing
    [14,2368,33,38],
    [11,3404,65,76],
    [92,3402,70,79],
    [172,3386,71,95],

    [92,3402,70,79],
    [172,3386,71,95],
    [92,3402,70,79],
    [172,3386,71,95], 
    [92,3402,70,79],
    [172,3386,71,95], 
    [92,3402,70,79],
    [172,3386,71,95],
    [92,3402,70,79],
    [172,3386,71,95],
    [92,3402,70,79],
    [172,3386,71,95], 
    [92,3402,70,79],
    [172,3386,71,95], 
    [92,3402,70,79],
    [172,3386,71,95],
    [92,3402,70,79],
    [172,3386,71,95],
    [92,3402,70,79],
    [172,3386,71,95], 
    [92,3402,70,79],
    [172,3386,71,95], 
    [92,3402,70,79],
    [172,3386,71,95],
    [92,3402,70,79],
    [172,3386,71,95],
    [92,3402,70,79],
    [172,3386,71,95],
    [92,3402,70,79],
    [172,3386,71,95],
    [92,3402,70,79],
    [172,3386,71,95],
    [92,3402,70,79],
    [172,3386,71,95],
    [92,3402,70,79],
    [172,3386,71,95],  
]

#4-> Minato Flying Thunder Disappearing
minato_flying_thunder_effect_disappearing=[
    [9,2275,74,65],
    [96,2274,75,57],
    [183,2272,66,62],
    [264,2273,61,59],
    [348,2277,60,58],
    [426,2276,65,64],
    [512,2275,65,65],
]

#5->Minato Flying Thunder Appearing
minato_flying_thunder_effect_appearing=[
    [14,2368,33,38],
    [11,3404,65,76],
    [92,3402,70,79],
    [172,3386,71,95],
]

#Effect-blast
blast_frame_info=[
    [7,2530,149,154],
    [170,2512,178,178],
    [368,2506,175,179],
    [565,2512,168,177],
]

#Effect-ground
ground_frame_info=[
    [10,2703,182,194],
    [213,2716,193,163],
    [439,2703,184,176],
    [7,2937,192,132],
]


class Minato():
    def __init__(self):
        self.minato_sprite_sheet=pygame.image.load(os.path.join('assets','minato.png')).convert_alpha()
        self.SPRITE_BG_COLOR=(0,64,128)#sprite sheet background Color
    
    def minato_intro(self):
        minato_intro=player.Player(self.minato_sprite_sheet,minatio_intro_frame_info,self.SPRITE_BG_COLOR,1)
        return minato_intro
    
    def minato_standing(self):
        minatio_standing=player.Player(self.minato_sprite_sheet,minato_standing_frame_info,self.SPRITE_BG_COLOR,1)
        return minatio_standing
    
    def minato_running(self):
        minatio_running=player.Player(self.minato_sprite_sheet,minato_running_frame_info,self.SPRITE_BG_COLOR,1)
        return minatio_running
    
    def blast(self):
        naruto_sprite_sheet=pygame.image.load(os.path.join('assets','naruto.png')).convert_alpha()
        SPRITE_BG_COLOR=(0,128,0)#sprite sheet background Color
        blast=player.Player(naruto_sprite_sheet,blast_frame_info,SPRITE_BG_COLOR,1)
        return blast
    
    def ground_effect(self):
        naruto_sprite_sheet=pygame.image.load(os.path.join('assets','naruto.png')).convert_alpha()
        SPRITE_BG_COLOR=(0,128,0)#sprite sheet background Color
        ground_effect=player.Player(naruto_sprite_sheet,ground_frame_info,SPRITE_BG_COLOR,1)
        return ground_effect