import pygame

class Player():
    def __init__(self,image,frame_info,color,scale):
        self.sheet=image
        self.frame_info=frame_info
        self.color=color
        self.scale=scale
    
    def get_image(self,frame,scale=1):

        starting_X=self.frame_info[frame][0]
        starting_Y=self.frame_info[frame][1]
        width=self.frame_info[frame][2]
        height=self.frame_info[frame][3]

        image=pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet,(0,0),(starting_X,starting_Y,width,height))
        image=pygame.transform.scale(image,(scale*width,scale*height))
        image.set_colorkey(self.color)
        return image