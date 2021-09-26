import pygame
import os
import player

#1-->KunaieSlash
kunai_slash_frame_info=[
    [534,3447,34,44],
    [582,3441,32,50],
    [633,3448,42,43],
    [687,3423,43,68],
    [753,3427,48,64],
    [821,3435,54,56],
    [891,3436,46,53],
    [955,3444,36,47]
]


#2-->Effect-->PuFF
puff_animation_frame_info=[
    [33,3755,25,30],
    [77,3740,45,53],
    [142,3741,44,50],
    [201,3740,40,46],
    [259,3739,25,30],
    [305,3738,24,20]
]

#3-->TreeTransformationEvasion
transmission_frame_info=[
    [14,2535,34,44],#repeat0
    [14,2535,34,44],#repeat0
    [63,2529,33,50],
    [112,2528,34,51],#repeat1
    [162,2528,34,51],#repeat2
    [112,2528,34,51],#repeat1
    [162,2528,34,51],#repeat2
    [112,2528,34,51],#repeat1
    [162,2528,34,51],#repeat2
    [210,2529,33,50],
    [260,2535,34,44],
    #puff smoke effect--start
    [33,3755,25,30],
    [77,3740,45,53],
    [142,3741,44,50],
    [201,3740,40,46],
    [259,3739,25,30],
    [305,3738,24,20],
    #puff smoke effect--end
    [311,2542,28,35],#treeBig
    [311,2542,28,35],#treeBig
    [311,2542,28,35],#treeBig
    [311,2542,28,35],#treeBig
    [311,2542,28,35],#treeBig
    [311,2542,28,35],#treeBig
    [311,2542,28,35],#treeBig
    [311,2542,28,35],#treeBig
]

#4->Chidori
chidori_frame_info=[
    [44,6396,34,44],#init
    [97,6389,32,51],#handsign1
    [151,6390,32,50],#handsign2
    [203,6390,33,50],#handsign3
    [97,6389,32,51],#handsign1
    [151,6390,32,50],#handsign2
    [203,6390,33,50],#handsign3
    [97,6389,32,51],#handsign1
    [151,6390,32,50],#handsign2
    [203,6390,33,50],#handsign3
    [255,6396,41,44],
    [304,6396,54,54],#repeat1
    [369,6396,58,56],#repeat2
    [436,6395,64,56],#repeat3
    [510,6396,60,55],#repeat4
    [304,6396,54,54],#repeat1
    [369,6396,58,56],#repeat2
    [436,6395,64,56],#repeat3
    [510,6396,60,55],#repeat4
    [304,6396,54,54],#repeat1
    [369,6396,58,56],#repeat2
    [436,6395,64,56],#repeat3
    [510,6396,60,55],#repeat4
    [590,6390,62,48],
    [667,6390,62,48],
    [769,6399,66,40],
    [844,6400,66,39],#hit1
    [924,6399,66,40],#hit2
    [1009,6389,43,50]#hit3
]

#5->Effect---chidori Text
chidori_text_frame_info=[
    [364,6463,117,61]
]

#6->Effect---chidori spark
chidori_spark_frame_info=[
    [222,6583,27,23],
    [267,6580,27,31]
]

class Kakashi():
    def __init__(self):
        self.kakashi_sprite_sheet=pygame.image.load(os.path.join('assets','kakashi.png'))
        self.SPRITE_BG_COLOR=(0,128,0)#sprite sheet background Color
    
    def kunaie_slash(self):
        kunaie_slash=player.Player(self.kakashi_sprite_sheet,kunai_slash_frame_info,self.SPRITE_BG_COLOR,3)
        return kunaie_slash
    
    def transmission_into_tree(self):
        transmission_into_tree=player.Player(self.kakashi_sprite_sheet,transmission_frame_info,self.SPRITE_BG_COLOR,3)
        return transmission_into_tree
    
    def chidori(self):
        chidori=player.Player(self.kakashi_sprite_sheet,chidori_frame_info,self.SPRITE_BG_COLOR,2)
        return chidori
    
    def chidori_text(self):
        chidori_text=player.Player(self.kakashi_sprite_sheet,chidori_text_frame_info,self.SPRITE_BG_COLOR,2)
        return chidori_text
    
    def chidori_spark(self):
        chidori_spark=player.Player(self.kakashi_sprite_sheet,chidori_spark_frame_info,self.SPRITE_BG_COLOR,2)
        return chidori_spark