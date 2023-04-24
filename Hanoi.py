import pygame, sys, time
import mysql.connector
from sys import exit

#exec(open("./login.py").read())

pygame.init()
pygame.display.set_caption("Towers of Hanoi")
screen = pygame.display.set_mode((900, 600),pygame.RESIZABLE)


gameover=False


#variables
moves=0
ndisks=3 #change this variable to adjust the number of disks(minimum:3)
towermid=[160, 450, 740]
l=[]
f=False
point=0
pointer=0
timer=0
start=0

#colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (204, 0, 102)
gold = (204, 122, 0)
blue = (0,51,53)
lblue=(0, 38, 153)
grey = (255, 251, 224)
green = (77, 206, 145)
brown = (100,40,0)
pink = (255, 204, 255)


def info():
        global screen, gameover,start
        infoover=False
        f=open('rules.txt','r')
        text=f.read()
        sentence=text.splitlines()
        while not infoover:
                screen.fill(grey)

                width=screen.get_width()
                height=screen.get_height()
                
                vijaya=pygame.font.SysFont('Latha',60)
                vijaya1=pygame.font.SysFont('Vijaya',40)
                
                head=vijaya.render("HOW TO PLAY",1,black)
                head_rect=head.get_rect(center=(width/2,60))
                screen.blit(head,head_rect)
                
                nextp = vijaya1.render('(Press enter to continue)', 1, blue)
                nextp_rect = nextp.get_rect(center=(width/2+240,height-150))
                screen.blit(nextp,nextp_rect)
                
                x=0
                for i in sentence:
                        rule=pygame.font.Font(None,27)
                        rules= rule.render(i, 1, brown)
                        screen.blit(rules, (width/12-20,140+x))
                        x+=60
                
                
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                        start = pygame.time.get_ticks()
                                        infoover=True
                                
                                        
                        if event.type == pygame.QUIT:
                                infoover= True
                                gameover= True
                                
                pygame.display.flip()

def intro():
        global ndisks,gameover
        introover=False
        while not introover:

                width=screen.get_width()
                height=screen.get_height()
                
                screen.fill(grey)
                vijaya=pygame.font.SysFont('lisu',70)
                font=pygame.font.SysFont('dubai',30)

                #vijaya.set_underline(True)

                title = vijaya.render('Towers Of Hanoi', 1, blue)
                title_rect = title.get_rect(center=(width/2,80))
                screen.blit(title,title_rect)

                text = font.render('Select number of discs using right and left arrow keys and press enter', 1, black)
                text_rect = text.get_rect(center=(width/2,260))
                screen.blit(text,text_rect)

                fonts=pygame.font.Font(None,60)
                disk=fonts.render(str(ndisks),1,blue)
                screen.blit(disk,(width/2,330))

                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN:
                                        introover=True
                                        info()
                                if event.key == pygame.K_RIGHT:
                                        if ndisks<6:
                                                ndisks+=1
                                        
                                if event.key == pygame.K_LEFT:
                                        if ndisks>3:
                                                ndisks-=1
                                        
                                
                                        
                        if event.type == pygame.QUIT:
                                gameover= True
                                introover= True
                                
                                
                pygame.display.flip()
                
        

def towers():
        global screen
        for x in range(65,690,290):
                pygame.draw.rect(screen, black, pygame.Rect(x,450,190,20))
                pygame.draw.rect(screen, black, pygame.Rect(x+90,250,10,200))
        
                
def disks():
        global ndisks, l
        l=[]
        h=23
        y=425
        w= ndisks*34
        for i in range(ndisks):
                d={}
                d['re']=pygame.Rect(0,0,w,h)
                d['re'].midtop=(160,y)
                d['val']=ndisks-i
                d['tower']=0
                l.append(d)
                y -= h+3
                w -= 32
                
def ddisks():
        global screen
        for i in l:
                pygame.draw.rect(screen, gold, i['re'])
        return
        
def pointers():
        ptr_points = [(towermid[point]+20 ,490), (towermid[point]-20 ,490), (towermid[point], 480)]
        pygame.draw.polygon(screen,brown, ptr_points)
        return
        
def text(moves):
   font=pygame.font.Font(None,60)
   scoretext=font.render("Moves: "+str(moves), 1,lblue)
   screen.blit(scoretext, (width/2-100, 20))
   t=156
   for i in range(3):
        fonts=pygame.font.Font(None,20)
        ttext=fonts.render(str(i+1), 1, white)
        screen.blit(ttext, (t,455))
        t+=290
        
def gamewin():
        global screen,l,moves,start,timer,gameover
        done=True
        gameover=False
        
        for d in l:
                if d['tower']!=2:
                        done=False
        if done==True:
                timer= (pygame.time.get_ticks()-start)//1000
                scoreboard()
        
        while done:
                gameover=True

                width=screen.get_width()
                height=screen.get_height()
                
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                
                screen.fill((206,206,206))
                reqmoves= (2**(ndisks))-1
                if moves == reqmoves:
                        font=pygame.font.Font(None,50)
                        con=font.render('CONGRATULATIONS!!',1,blue)
                        fonts=pygame.font.Font(None,30)
                        tex=fonts.render('You have finished in minimum number of moves', 3, red)
                        screen.blit(con, (width/3-20,40))
                        screen.blit(tex, (width/4+25,80))
                        last()
                        
                else:
                        font=pygame.font.Font(None,40)
                        ops=font.render('OOPS!',1,blue)
                        fonts=pygame.font.Font(None,30)
                        dis=fonts.render('You did not complete in the minimum number of moves', 3, red)
                        screen.blit(ops, (width/2-20,40))
                        screen.blit(dis, (width/5+20,80))
                        last()

                       
                pygame.display.flip()
                

def scoreboard():
        global timer
        con=mysql.connector.connect(user='root',password='mysql',host='127.0.0.1',database='puzzler')
        cur = con.cursor()
        t= cur.execute("select * from scoreboard")
        t = len(cur.fetchall())
        reqmoves= (2**(ndisks))-1
        if moves == reqmoves:
                up= cur.execute("update scoreboard set disks=%s, time=%s where SNo=%s"%(ndisks,timer,t))
                con.commit()
        else:
                dele=cur.execute("delete from scoreboard where SNo=%s"%(t))
                con.commit()

def last():
        for i in range(4):
                for j in range(11):
                        rect = pygame.Rect(i*170+130, j*30+150,170, 30)
                        pygame.draw.rect(screen, black, rect, 1)
        con=mysql.connector.connect(user='root',password='mysql',host='127.0.0.1',database='puzzler')
        cur = con.cursor()
        t= cur.execute("select * from scoreboard order by disks DESC,time ASC")
        t=cur.fetchall()
        n=1
        k=[]
        k.insert(0,('Rank','Name','Disks','Time'))
        for i in t:
                m=list(i)
                m[0]=n
                n+=1
                k.append(m)
        for x in range(1):
                for y in range(len(k)):
                        for i in t:
                                
                                font=pygame.font.SysFont('dubai',26)
                                sn=font.render(str(k[y][0]),1,blue)
                                screen.blit(sn, (x*50+140,y*30+140))
                                name=font.render(str(k[y][1]),1,blue)
                                screen.blit(name, (x*50+308,y*30+140))
                                d=font.render(str(k[y][2]),1,blue)
                                screen.blit(d, (x*50+480,y*30+140))
                                ti=font.render(str(k[y][3]),1,blue)
                                screen.blit(ti, (x*50+650,y*30+140))

        

intro() 
disks()                    
while not gameover:
        
        width=screen.get_width()
        height=screen.get_height()

        for event in pygame.event.get():
        

                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                
                        if event.key == pygame.K_RIGHT:
                                point = (point+1)%3
                                if f:
                                        l[pointer]['re'].midtop= (towermid[point],160)
                                        l[pointer]['tower'] = point
                                        
                        if event.key ==pygame.K_LEFT:
                                point = (point-1)%3
                                if f:
                                        l[pointer]['re'].midtop= (towermid[point],160)
                                        l[pointer]['tower'] = point
                        
                        if event.key == pygame.K_UP and not f:
                                for d in l[::-1]:
                                        if d['tower'] == point:
                                                f=True
                                                pointer = l.index(d)
                                                d['re'].midtop =(towermid[point], 160)
                                                break
                                                
                        if event.key == pygame.K_DOWN and f:
                                for d in l[::-1]:
                                        if d['tower']==point and l.index(d)!=pointer:
                                                if d['val']>l[pointer]['val']:
                                                        f = False
                                                        l[pointer]['re'].midtop = (towermid[point], d['re'].top-26)
                                                        moves+= 1
                                                break
                                else: 
                                        f = False
                                        l[pointer]['re'].midtop = (towermid[point], 400+25)
                                        moves += 1
                        
                        
        
        screen.fill(grey)
        towers()
        ddisks()
        pointers()
        text(moves)
        if not f:
                gamewin()
                
        pygame.display.flip()
                
