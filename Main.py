import pygame
import sys

Black=(0,0,0)
Red=(204,0,102)
White=(255,255,255)
Gold = (255, 209, 26)
Grey = (170, 170, 170)
LYellow=(255,255,237)
Blue=(0, 204, 255)
Green=(57, 230, 0)

over=False

pygame.init()
pygame.display.set_caption("Puzzler")
screen = pygame.display.set_mode((900,600),pygame.RESIZABLE)

speed=0

y1=298

inkfree=pygame.font.SysFont('stencil',55)
Vijaya=pygame.font.SysFont('gabriola',42)
Stencil=pygame.font.SysFont('dubai',40)


while not over:
    width=screen.get_width()
    height=screen.get_height()

    bgimg = pygame.image.load('1.jpg')
    bgimg = pygame.transform.scale(bgimg,(width,height)).convert_alpha()

    relx=speed%bgimg.get_rect().width
    screen.fill(Black)
    screen.blit(bgimg,(relx-bgimg.get_rect().width,0))
    if relx<width:
        screen.blit(bgimg,(relx,0))
        speed-=1.4

    title=inkfree.render("Welcome  to  Puzzler!!",1,Gold)
    title_rect = title.get_rect(center=(width/2, 90))
    screen. blit(title, title_rect)

    t="Select a game by using the up and down arrow keys and press enter"
    info=Vijaya.render(t,1,White)
    info_rect=info.get_rect(center=(width/2,220))
    screen.blit(info, info_rect)

    hanoi=Stencil.render("TOWERS  OF  HANOI",1,Blue)
    screen.blit(hanoi,(width/3,290))
    screen.blit(hanoi,(width/3+2,293))

    virus=Stencil.render("VIRUS  SPREAD  SIMULATOR",1,Blue)
    screen.blit(virus,(width/3-70,390))
    screen.blit(virus,(width/3-68,393))

    collatz=Stencil.render("COLLATZ  CONJECTURE",1,Blue)
    screen.blit(collatz,(width/3-28,490))
    screen.blit(collatz,(width/3-26,493))

    pygame.draw.rect(screen, LYellow, pygame.Rect(width/3-85,y1,520,55),True)


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                if y1==498:
                    y1=298
                else:
                    y1=(y1+100)
                

            if event.key==pygame.K_UP:
                if y1==298:
                    y1=498
                else:
                    y1=(y1-100)

            if event.key==pygame.K_RETURN:
                if y1==298:
                    exec(open("./hanoi.py").read())
                elif y1==398:
                    exec(open("./Virus_Spread.py").read())
                else:
                    exec(open("./tk_collatz.py").read())
        
    pygame.display.update()



