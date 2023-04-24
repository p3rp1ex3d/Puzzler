import pygame
import random
import time

pygame.init()

col='WHITE'

screen = pygame.display.set_mode((900,600),pygame.RESIZABLE)

box=12
width=25
height=25
margin=10


over=False

def main_menu():
    global over,newl,day,grid,lnew,cr,counter
    menuover=False
    newl=[]
    lnew=[]
    day=1
    cr=6
    counter=6
    grid=[[1 for y in range(box)] for x in range(box)]
    
    
    while not menuover:
        screen.fill((249,228,144))
        instructions()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menuover=True
                    initial_state()
                                        
            if event.type == pygame.QUIT:                
                menuover= True
                over= True
                                
        pygame.display.flip()
    
    

def surround(x,y):
    person_pos=[[x-1,y-1],[x-1,y],[x-1,y+1],
               [x,y-1],          [x,y+1],           
               [x+1,y-1],[x+1,y],[x+1,y+1]]
    t=[]
    for k in person_pos:
        g,h=k
        if 0<=g<box and 0<=h<box:
            t.append(k)            
        
    return t

def get_pos():
    global l,lnew
    l=[]
    for i in range(box):
        for j in range(box):
            if grid[i][j]==0:
                l.append([i,j])
                t=surround(i,j)

                for m,n in t:
                    if grid[m][n]>0:
                        grid[m][n]-=1
                        change()

    lnew.append(l)
    return l

def reverse():
    global grid,lnew
    for i in range(len(lnew[counter-cr])):
        x=lnew[counter-cr][i][0]
        y=lnew[counter-cr][i][1]
        if grid[x][y]==0:
            grid[x][y]=random.randint(18,23)
            change()
    

def initial_state():
    screen.fill('black')
    for i in range(box):
        for j in range(box):
            x=random.randint(1,15)
            grid[i][j]=x
        
    i=random.randint(0,box-1)
    j=random.randint(0,box-1)
    grid[i][j]=0
    ini_draw()
    return grid


def instructions():
    x=30
    y=130
    papyrus1=pygame.font.SysFont('papyrus',50)
    papyrus2=pygame.font.SysFont('papyrus',30)
    About=papyrus1.render("About the Game",1,(124,104,25))
    screen.blit(About,(290,30))
    f=open("vrules.txt",'r').readlines()
    for i in f:
        i=i.rstrip('\n')
        t=papyrus2.render(i,1,(124,104,25))
        screen.blit(t,(x,y))
        y+=36
    papyrus3=pygame.font.SysFont('papyrus',40)
    enter=papyrus3.render("Press enter to continue",1,(124,104,25))
    screen.blit(enter,(460,490))
            
        
def ini_draw():
    ariel=pygame.font.SysFont('ariel',50)
    days=ariel.render("DAY : 0",1,col)
    screen.blit(days,(150,430))
    vijaya=pygame.font.SysFont('vijaya',32)
    back=vijaya.render("press backspace to start a new simulation",1,'yellow')
    nextd=vijaya.render("press the right arrow button for the next day",1,'yellow')
    screen.blit(back,(430,500))
    screen.blit(nextd,(420,460))
    
    for i in range(box):
        for j in range(box):
            if grid[i][j]==0:
                pygame.draw.rect(screen,(213,34,0),[(margin+width)*j+10,(margin+height)*i+10,width,height])
            else:
               pygame.draw.rect(screen,col,[(margin+width)*j+10,(margin+height)*i+10,width,height])
    pygame.display.flip()
    return grid

def count():
    global newl
    ci=0
    cn=0
    for i in range(box):
        for j in range(box):
            if grid[i][j]==0:
                ci+=1
            elif grid[i][j]!=0:
                cn+=1
                
    newl.append(ci)
    return ci,cn,newl

def text():
    t=count()
    ariel=pygame.font.SysFont('ariel',50)
    calibri=pygame.font.SysFont('calibri',40)
    stats=ariel.render("Stats (Day:"+str(day-1)+')',1,'yellow')
    screen.blit(stats,(540,70))
    infected=calibri.render(str("Infected: ")+str(t[0]),1,(213, 34, 0))
    notinfected=calibri.render(str("Not Infected: ")+str(t[1]),1,(255,255,255))
    screen.blit(infected,(460,140))
    screen.blit(notinfected,(460,190))
    days=ariel.render("DAY : "+str(day),1,col)
    screen.blit(days,(150,430))
    vijaya=pygame.font.SysFont('vijaya',32)
    back=vijaya.render("press backspace to start a new simulation",1,'yellow')
    nextd=vijaya.render("press the right arrow button for the next day",1,'yellow')
    screen.blit(back,(420,500))
    screen.blit(nextd,(420,460))
    maxm=calibri.render("Maximum infected: "+str(max(t[2])),1,'light blue')
    screen.blit(maxm,(460,240))

def change():
    for i in range(box):
        for j in range(box):
            if grid[i][j]==0:
                pygame.draw.rect(screen,(213, 34, 0),[(margin+width)*j+10,(margin+height)*i+10,width,height]) 
            elif grid[i][j]!=0:
                pygame.draw.rect(screen,col,[(margin+width)*j+10,(margin+height)*i+10,width,height])
    pygame.display.flip()


main_menu()


while not over:
    count()
    text()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                menuover=False
                main_menu()
            if event.key == pygame.K_RIGHT:
                get_pos()
                day+=1
                if day>5 and counter>5 and day==counter:
                    reverse()
                    counter+=1


    screen.fill('black')
