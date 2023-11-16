
from tkinter import *
import keyboard as keyb
import pygame
from PIL import ImageTk


from image import *


from arguments import *
from music import *
from timeone import *


root = Tk()
root.geometry('1900x950+5+50')
root.title('...')



def leanguage():
    global root
    global yess
    for i in range(10):
        yess -= 10
   
    root.destroy()
def leanguage1():
    global root
    global yess
    for i in range(10):    
        yess += 10
    root.destroy()
imgt1 = ImageTk.PhotoImage(file='C:/Users/SoaPisGirseb/Desktop/gagaGame/photo/fonchik.png')
v1 = Label(root, image=imgt1, font='100', bg='black', fg='white' )  
v1.pack() 
root.config(bg='black')    
bht = Button(root, text='ENG', command=leanguage, font='10', height='5', width='15', fg='yellow', bg='black')
bht.pack()
bht.place(x='900', y='200')
yest = Button(root, text='RUS', command=leanguage1, font='10', height='5', width='15', fg='yellow', bg='black')
yest.pack()
yest.place(x='900', y='50')
root.overrideredirect(1)
root.mainloop()



pygame.init()
win = pygame.display.set_mode((1900, 950))
pygame.display.set_caption('game')
pygame.display.set_icon(icon)
while yess <= -1:
    from mainENG import *
while yess >= 1:    
    print(v)
    test = 0

    cikl = True

    while cikl == True:
            
        
        pygame.time.delay(15)
        # Этот код заставляет игру не закрыватся
        keys = pygame.key.get_pressed() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cikl = cikl = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backpack1 == 2 :
                    if left == True:
                        leveltop2 = damage_left
                        leveltop2 = damage_left2
                        leveltop2 = damage_left3
                    if right == True:
                        leveltop1 = damage
                        leveltop1 = damage2
                        leveltop1 = damage3
                        
        
        while money < 0:
            money += 1
            
        # Это магазин здесь написано что мы берем из глобала деньги и  к = деньгам = деньги минус сломаны меч и если к будет менше чем сломманы меч или меньше чем 1 то к = 0
        
        if keys[pygame.K_p] :
            
            
            
                
            
                    
            
            
                if playerx + speed > -15 and playerx + speed < 100:
                    if money >= 0:    
                        def buy():
                            
                            global breakswords
                            global money
                            breakswords = breakswords = 2        
                            money -= breaksword
                            
                            if money <= eklift:
                                for i in range(15):    
                                    root = Toplevel()
                                    root.geometry('250x250+100+100')
                                    root.title(money)
                                    
                                    root.config(bg='black')
                                    g = Label(root, text='YOU DONT HAVE MONEY',  height='5', width='25', bg='black', fg='yellow', font='10')
                                    g.pack()
                                    g.place()
                                    root.overrideredirect(1)
                                    root.mainloop
                                    
                                    
                            if money < breaksword or money < 1:
                                money = 0
                    
                    
                    
                            
                        root = Tk()
                    
                        root.geometry('1000x500+500+250')
                        root.config(bg='black')
                        root.title(f'shop, {money}')
                        imgsword = ImageTk.PhotoImage(file='C:/Users/SoaPisGirseb/Desktop/gagaGame/photo/sword1.png')
                        btn = Button(root,  height='150', width='200', bg='gold',  command = buy, image=imgsword, compound=BOTTOM,  text='BreakSword',)
                        btn.pack()
                        btn.place(x='1')
                        talk = True
                        
                        root.mainloop()       
                    
                    
        
                        
            
        
        
        
        # здесь написано что если игрок нажмет на букву р то откроются характеристки предметов я рекоминдую самому себе научится масиву и тогда этот код улучится потому что не будет засарено текст лаебалом
        if keys[pygame.K_r]:
            root = Tk()
            root.geometry('900x900+500+500')
            root.title('lol')
            
            text = Label(text = ' breaksword characters: \n Dmg = 15 \n forge = 60 \n sell = 100', bg='yellow', fg='black')
            text.pack()
            text.place(x='1')
        
            root.mainloop()  
            
        # Здесь написано что если игрок нажмет на букву м тооно покажет денги и если к будет меньше чем ноль то к будет равнятся нулю

        
        
                
        if keys[pygame.K_o]:
            def money2():
                pass
                
                
                


        
            root = Tk()
            root.geometry('500x50+25+75')
            root.title(money)
            root.config(bg='black')
            money1 = Button(root, text=f'Это Денги {money}', font='10', bg='black', width='20', height='20', fg='yellow', command=money2)
            money1.pack()
            
            root.mainloop()    
            
                
                
            
                    
            
        if keys[pygame.K_1] and breakswords == fbn:
            leveltop1 = playersword
            leveltop2 = playersword2
        # Это код движение персонажа и код анимаций если х будет  добовлятся скорость игрока и если будет добовлятся то лефт = ложь д райт = истына и здесь написано что если игрок будет нажимать на а то х будет добовлятся скорость игрока
        if keys[pygame.K_q]:
            cikl = False
        if keys[pygame.K_d] and moved == 2:
            playerx += speed
            right = True
            left = False 
            
        
        
        if playerx + speed > 1300:
            playerx = 1300
        # Это код движение персонажа и код анимаций если х будет  отбовлятс скорость игрока и если будет отбовлятся  то лефт = истына а райт = ложь и здесь написано что если игрок будет нажимать на а то х будет отбовлятся скорость игрока
        if keys[pygame.K_a] and movea == 2:
            playerx -= speed
            left = True
            right = False
            
        
            
        
        # Это граница мира
        if playerx - speed < -15:
            playerx = -15
        # Это анимация если лефт будет истына то оно будет рисовать анимацию
        
        if left == True:
            
            if v >= 21 and v <= 50:
            
                win.blit(fon2, (0, 0))
                win.blit(magic, (1500, 725))
                if leveltop2 == player3:    
                    win.blit(leveltop2, (playerx, (playery-left1)))
                elif leveltop2 == playersword2:
                    win.blit(leveltop2, (playerx, (playery-left2)))
                if breakswords == fbn and money >= eklift:
                    
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                    
                pygame.display.update() 
            if v >= 10 and v <=20:
                
                win.blit(fon1, (0, 0))
                win.blit(magic, (1500, 725))
                if leveltop2 == player3:    
                    win.blit(leveltop2, (playerx, (playery-left1)))
                elif leveltop2 == playersword2:
                    win.blit(leveltop2, (playerx, (playery-left2)))
                if breakswords == fbn and money >= eklift:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                        
                        

                pygame.display.update() 
                
    
                
            if v > 50 or v < 10:
            
                win.blit(fon, (0, 0))
                win.blit(magic, (1500, 725))
                if leveltop2 == player3:    
                    win.blit(leveltop2, (playerx, (playery-left1)))
                elif leveltop2 == playersword2:
                    win.blit(leveltop2, (playerx, (playery-left2)))
                if breakswords == fbn and money > eklift:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                
                            
                pygame.display.update()        
            
        # Это анимация если райт будет истына  то будет рисовать анимацию
        
        if right == True:
            
            
            
            if v >= 10 and v <=20:
                
                win.blit(fon1, (0, 0))
                win.blit(magic, (1500, 725))
                if leveltop1 == player2:    
                    win.blit(leveltop1, (playerx, (playery-right1)))
                elif leveltop1 == playersword:
                    win.blit(leveltop1, (playerx, (playery-right2)))
                if breakswords == fbn and money >= eklift:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                            
                pygame.display.update()    
            
            
            if v >= 21 and v <= 50:
                
                
                win.blit(fon2, (0, 0))
                win.blit(magic, (1500, 725))
                if leveltop1 == player2:    
                    win.blit(leveltop1, (playerx, (playery-right1)))
                elif leveltop1 == playersword:
                    win.blit(leveltop1, (playerx, (playery-right2)))
                if breakswords == fbn and money >= eklift:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                pygame.display.update()

            if v > 50 or v < 10:
                    
                
                win.blit(fon, (0, 0))
                win.blit(magic, (1500, 725))
                if leveltop1 == player2:    
                    win.blit(leveltop1, (playerx, (playery-right1)))
                elif leveltop1 == playersword:
                    win.blit(leveltop1, (playerx, (playery-right2)))
                if breakswords == fbn and money >= eklift:
                    
                    backpack1 = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                pygame.display.update()            
                
        # Это анимация если персонаж не будет двигатся ту лефт и райт = фолс и он не будет делать анимацию
        
        if right == False and left == False:
            
            if v >= 21 and v <= 50:
                
                
                win.blit(fon2, (0, 0))
                win.blit(magic, (1500, 725))
                win.blit(leveltop1, (playerx, playery))
                if breakswords == fbn and money >= eklift:
                    
                    backpack =  2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                pygame.display.update() 
            
            if v >= 10 and v <=20:
            
                
                win.blit(fon1, (0, 0))
                win.blit(magic, (1500, 725))
                win.blit(leveltop1, (playerx, (playery - 10)))
                if breakswords == fbn and money >= 150:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                        
                            
                pygame.display.update() 
            
            
            if right == False and left == False and v > 50 or v < 10:
                
                
                win.blit(fon, (0, 0))
                win.blit(magic, (1500, 725))
                win.blit(leveltop1, (playerx, playery))
                if breakswords == fbn and money >= 150:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                pygame.display.update() 
                
            
            if right == False and left == False and v >20 and v <=40:
            
                
                win.blit(fon2, (0, 0))
                win.blit(magic, (1500, 725))
                win.blit(leveltop1, (playerx, playery))
                if breakswords == fbn and money >= eklift:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                pygame.display.update() 
            

            if right == False and left == False and v >= 10 and v <=20:    
                
                win.blit(fon1, (0, 0))
                win.blit(magic, (1500, 725))
                win.blit(leveltop1, (playerx, (playery - 10)))
                if breakswords == fbn and money >= eklift:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                    

                pygame.display.update()            
            
        if shop1 == 2 or playerx + speed > 150: 
            movea = movea = 2
        
        if shop1 == 1 and playerx + speed < 150:
            movea = movea = 1
        
        
    

            
    # Это Диалог с волшебником у тебя здесь написано если игрок нажмет на т в конкретных кординатах то тогда и будет роботат твой скрыпт если нет то он не будет включатся
        if keys[pygame.K_t] and playerx + speed > 1300 :
            if shop1 == 2:
                talk = talk = 2
            if talk == 1:
                from talk import *
            
            if talk == 2:
                

                root = Tk()
                root.wm_attributes('-alpha', 0.9)
                root.geometry('1925x750+1+350')
                root.title('lol')
                dialog_1_lvl_5 = Label(root, text='молодец теперь убей монстров задий тебя')
                dialog_1_lvl_5.pack()
                dialog_1_lvl_5.place()
                root.mainloop()
            
        # Это прижок сдесь исползовоно физика кинетичаская энергя E = mV**2/2 где "M" это *масса* а "V" это *скорость обекта* 
        if jump == False:
            if keys[pygame.K_SPACE]:
                jump = True
                

        else:
            if jumppower >= -10:
                if jumppower < 0:
                    playery += (jumppower ** 2) / 2
                else: 
                    playery -= (jumppower ** 2) / 2
                jumppower -= 1
                
                
                    
            else:
                jump = False
                jumppower = 10
        pygame.display.update()     
