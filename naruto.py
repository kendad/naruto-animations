import pygame
import os
import player


#1-->Rashen Shuriken
rashen_shuriken_frame_info=[
    [12,22,75,59],#init1
    [95,22,76,59],#init2
    [182,23,77,59],#init3
    [261,23,77,59],#init4

    [261,23,77,59],#init4
    [182,23,77,59],#init3
    [95,22,76,59],#init2
    [12,22,75,59],#init1

    [12,22,75,59],#init1
    [95,22,76,59],#init2
    [182,23,77,59],#init3
    [261,23,77,59],#init4

    [261,23,77,59],#init4
    [182,23,77,59],#init3
    [95,22,76,59],#init2
    [12,22,75,59],#init1

    [16,156,77,59],#shurikenStarted-1
    [96,156,77,59],#shurikenStarted-2
    [183,155,77,59],#shurikenStarted-3
    [264,155,77,59],#shurikenStarted-4
    [347,155,77,59],#shurikenStarted-5
    [430,155,80,59],#shurikenStarted-6

    [16,156,77,59],#shurikenStarted-1
    [96,156,77,59],#shurikenStarted-2
    [183,155,77,59],#shurikenStarted-3
    [264,155,77,59],#shurikenStarted-4
    [347,155,77,59],#shurikenStarted-5
    [430,155,80,59],#shurikenStarted-6

    [16,156,77,59],#shurikenStarted-1
    [96,156,77,59],#shurikenStarted-2
    [183,155,77,59],#shurikenStarted-3
    [264,155,77,59],#shurikenStarted-4
    [347,155,77,59],#shurikenStarted-5
    [430,155,80,59],#shurikenStarted-6
    
    [16,156,77,59],#shurikenStarted-1
    [96,156,77,59],#shurikenStarted-2
    [183,155,77,59],#shurikenStarted-3
    [264,155,77,59],#shurikenStarted-4
    [347,155,77,59],#shurikenStarted-5
    [430,155,80,59],#shurikenStarted-6

    

    #[532,105,131,109],#shukrikenReady-1
    [680,106,112,105],#shukrikenReady-2
    [812,108,100,105],#shukrikenReady-3

    [680,106,112,105],#shukrikenReady-2
    [812,108,100,105],#shukrikenReady-3

    [680,106,112,105],#shukrikenReady-2
    [812,108,100,105],#shukrikenReady-3
    
    [680,106,112,105],#shukrikenReady-2
    [812,108,100,105],#shukrikenReady-3

    [680,106,112,105],#shukrikenReady-2
    [812,108,100,105],#shukrikenReady-3

    [680,106,112,105],#shukrikenReady-2
    [812,108,100,105],#shukrikenReady-3

    [680,106,112,105],#shukrikenReady-2
    [812,108,100,105],#shukrikenReady-3

    [680,106,112,105],#shukrikenReady-2
    [812,108,100,105],#shukrikenReady-3

    [680,106,112,105],#shukrikenReady-2
    [812,108,100,105],#shukrikenReady-3

    [680,106,112,105],#shukrikenReady-2
    [812,108,100,105],#shukrikenReady-3

    [680,106,112,105],#shukrikenReady-2
    [812,108,100,105],#shukrikenReady-3
    
    
    
    [642,317,60,52],#throwShuriken-1
    [709,318,60,51],#throwShuriken-2
    [781,317,60,52],#throwShuriken-3
]

#2->Effect--Shurikens Path
shuriken_path_frame_info=[
    [30,456,41,102],
    [81,468,50,75],
    [142,458,50,85],
    [198,473,58,68],
    [269,467,55,69],
    [333,469,50,72],
    [388,467,62,68],
    [464,471,56,64],
]

#3->Effect--Shuriken Blast
shuriken_blast_frame_info=[
    [22,1450,287,245],
    [369,1458,649,240],
    [37,1737,261,245],
    [348,1737,292,250],
]

#4->Effect--Ground Effect
shuriken_blast_ground_effect_frame_info=[
    [10,2703,182,194],
    [213,2716,193,163],
    [439,2703,184,176],
    [7,2937,192,132],
]


class Naruto():
    def __init__(self):
        self.naruto_shuriken_sprite_sheet=pygame.image.load(os.path.join('assets','naruto_rashen_shuriken.png'))
        self.naruto_sprite_sheet=pygame.image.load(os.path.join('assets','naruto.png'))
        self.SPRITE_BG_COLOR=(0,128,0)#sprite sheet background Color
    
    def rashen_shuriken(self):
        rashen_shuriken=player.Player(self.naruto_shuriken_sprite_sheet,rashen_shuriken_frame_info,self.SPRITE_BG_COLOR,2)
        return rashen_shuriken
    
    def shuriken_path(self):
        shuriken_path=player.Player(self.naruto_shuriken_sprite_sheet,shuriken_path_frame_info,self.SPRITE_BG_COLOR,2)
        return shuriken_path
    
    def shuriken_blast(self,scale):
        shuriken_blast=player.Player(self.naruto_shuriken_sprite_sheet,shuriken_blast_frame_info,self.SPRITE_BG_COLOR,scale)
        return shuriken_blast
    
    def shuriken_blast_ground_effect(self):
        shuriken_blast_ground_=player.Player(self.naruto_sprite_sheet,shuriken_blast_ground_effect_frame_info,self.SPRITE_BG_COLOR,2)
        return shuriken_blast_ground_