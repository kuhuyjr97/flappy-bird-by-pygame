import pygame ; import os ; import random ; pygame.font.init()
POINT_FONT= pygame.font.SysFont('comicsans', 120)
WIDTH,HEIGHT=450,800
pygame.display.set_caption("FLAPPY BIRD")
WIN= pygame.display.set_mode((WIDTH,HEIGHT))
#variable (color, local variables) 
BLUE= 0,140,150   ; BLACK= 0,0,0 ; GREEN= 0,255,100
bird_width, bird_height= 33,30  ; pipeGap=180  ; pipe_width,pipe_height=70, 550 ;pipe_vel=5
def draw():
    WIN.fill(BLUE) 
# Import Image
bg_image=pygame.image.load(os.path.join('imgs','bg.png'))  ;bg=pygame.transform.scale(bg_image,(WIDTH,HEIGHT))
bird1_im=pygame.image.load(os.path.join('imgs','bird1.png')) ; bird1= pygame.transform.scale(bird1_im,(bird_width,bird_height))
bird2_im=pygame.image.load(os.path.join('imgs','bird2.png')) ; bird2= pygame.transform.scale(bird2_im,(bird_width,bird_height))
bird3_im=pygame.image.load(os.path.join('imgs','bird3.png')) ; bird3= pygame.transform.scale(bird3_im,(bird_width,bird_height))
birds=[bird1,bird2,bird3]
pipe_img=pygame.transform.scale(pygame.image.load(os.path.join('imgs','pipe.png')),(pipe_width,pipe_height))
pipe_90=pygame.transform.scale(pygame.transform.rotate(pipe_img,180),(pipe_width,pipe_height))

base_img= pygame.transform.scale(pygame.image.load(os.path.join('imgs','base.png')),(WIDTH,200))


def draw_base(base_pos):
    base_pos.x-= 5
    base_pos.width-=5
    if base_pos.x+WIDTH<=0:
        base_pos.x= WIDTH
    if base_pos.width +WIDTH<=0:
        base_pos.width =WIDTH


def draw(bird_pos,a,base_pos,tilt,PIPES,number):
    WIN.blit(bg,(0,0))
    rotated_image= pygame.transform.rotate(birds[a],tilt)
    new_rect= rotated_image.get_rect(center=birds[a].get_rect(topleft=(bird_pos.x,bird_pos.y)).center)

    WIN.blit(rotated_image,new_rect.topleft)
    for pipe in PIPES:
        WIN.blit(pipe_img,(pipe.x,pipe.y))
        WIN.blit(pipe_90,(pipe.x,pipe.y-pipeGap-pipe_img.get_height()))
        POINT=POINT_FONT.render(str(number),1,GREEN)
        WIN.blit(POINT,(200,100))    
    WIN.blit(base_img,(base_pos.x,base_pos.y))
    WIN.blit(base_img,(base_pos.width,base_pos.y))
 
def check_collide(PIPES,bird_pos):
    base_rect=pygame.Rect(0,680,WIDTH,200)

    for pipe in PIPES:
        pipe_up=pygame.Rect(pipe.x,pipe.y-pipeGap-pipe_img.get_height(),pipe_90.get_width(),pipe_90.get_height())
        pipe_down=pygame.Rect(pipe.x ,pipe.y,pipe_img.get_width(),pipe_img.get_height())  
        if bird_pos.colliderect(pipe_down) or bird_pos.colliderect(pipe_up) or bird_pos.colliderect(base_rect)  :
            pygame.quit()
            
        if pipe.x ==- pipe_img.get_width():
            PIPES.remove(pipe) 

def main():
    run=True ; number =0
    bird_count=0
    base_pos= pygame.Rect(0,680,WIDTH,0)
    bird_pos= pygame.Rect(250,300,bird_width,bird_height)
    pipe_pos=pygame.Rect(WIDTH,random.randrange(480,580, 10),pipe_img.get_width(),pipe_img.get_height())
    clock= pygame.time.Clock()
    tilt= 0
    d=0 ; bird_vel= 0.9 ; angel= 5 ;PIPES=[pipe_pos]
    
        
    while run:
        clock.tick(35)
        bird_count+=1
        a=bird_count //10
        if bird_count >28:
            bird_count=0
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:       
                    d=0             
                    d=-13
            
        d+=bird_vel
        bird_pos.y+= d
        if bird_pos.y <=0 :
            bird_pos.y=10
        tilt-= angel
        if d>0:
            if tilt <= -90:
                tilt=-90
        if d<0:
            tilt=35
        for pipe in PIPES:
            pipe.x-= pipe_vel
            if pipe.x == bird_pos.x-100:
                new_pipe= pygame.Rect(WIDTH,random.randrange(300,550,10),0,0)
                PIPES.append(new_pipe)
            if pipe.x  == bird_pos.x:
                number+=1

        check_collide(PIPES,bird_pos)        
        draw(bird_pos,a,base_pos,tilt,PIPES,number)
        draw_base(base_pos)
        print(PIPES )
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()


