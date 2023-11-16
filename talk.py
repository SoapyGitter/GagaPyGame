from tkinter import *
import pygame
from arguments import *
from PIL import ImageTk
from timeone import *


                        
                            
                            
                        
                


def dialog():
    g = Label(root, text='Вы выбрали ответ Соврать', fg='red', bg='black', font='10')
    g.pack()
    g.place(y='50')
    btn3.place(y='10000')
    but.place(y='1000000', )
    def dialog_1():
                
        def dialog_2():
            def dialog_3():
                def dialog_4():
                    def dialog_5():
                            
                        root.overrideredirect(0)
                        talk4.place(y='50011')
                        global shop1
                        shop1 += 1   
                            
                        
                        g = Label(root, text='Вы выбрали ответ понял', fg='red', bg='black', font='10')
                        g.pack()
                        g.place(y='540')
                            



                            
                            
                            
                                        
                                                                    
                                        

                    magic4 = Label(root, text='хорошо Но для начала давай я обясню тебе управление нажимая на "P" ты открываеш магазин а\n нажимая на "M" ты открываешь кошелёк а нажимая на "R" ты открываеш характеристики мечей и брони, чтобы посмотреть свой баланс нажмите на "O", чтобы купить меч подойди к магазинчику и нажми на "P"', fg='yellow', bg='black', font='1')
                    magic4.pack()
                    magic4.place(y='460')
                        
                    talk2.place(y='333380') 
                    talk4 = Button(root, text='Понял',fg='white', bg='black',height='3', width='10', command=dialog_5)
                    talk4.pack()
                    talk4.place(y='540')
                    g = Label(root, text='Вы выбрали ответ Принять', fg='red', bg='black', font='1')
                    g.pack()
                    g.place(y='420')
                    talk3.place(y='380', x='151111310')
                            
                def dialog_4_lvl_4():
                        
                    talk2.place(y='333380')
                    talk3.place(y='380', x='151111310')
                    magic4 = Label(root, text='Хорошо пока', fg='yellow', bg='black', font='10')
                    magic4.pack()
                    magic4.place(y='420')
                    g = Label(root, text='Вы выбрали ответ Нет', fg='red', bg='black', font='1')
                    g.pack()
                    g.place(y='420')
                    root.overrideredirect(0)
                        
                                    
                g = Label(root, text='Вы выбрали ответ да кончено', fg='red', bg='black', font='1')
                g.pack()
                g.place(y='300')    
                talkp.place(y='30000')
                magic4 = Label(root, text='Для того чтобы ты выполнил мое поручение ты должен купить меч', fg='yellow', bg='black', font='1')
                magic4.pack()
                magic4.place(y='340')
                talk2 = Button(root, text='Принять',fg='white', bg='black',height='3', width='10', command=dialog_4)
                talk2.pack()
                talk2.place(y='380')
                talk3 = Button(root, text='нет',fg='white', bg='black',height='3', width='10', command=dialog_4_lvl_4)
                talk3.pack()
                talk3.place(y='380', x='150')

            magic3 = Label(root, text='Хорошо забудем это, не мог бы ты мне помочь?', fg='yellow', bg='black', font='1')
            magic3.pack()
            magic3.place(y='250')
            g = Label(root, text='Вы выбрали ответ Я не знаю', fg='red', bg='black', font='1')
            g.pack()
            g.place(y='225')
            btn3.place(y='2502222')
            talkp = Button(root, text='Да ...Конечно',fg='white', height='3', width='10', bg='black', command=dialog_3)
            talkp.pack()
            talkp.place(y='300', x='50')
                            

        magic2 = Label(root, text='Волшебник: почему ты мне соврал?', fg='yellow', bg='black', font='1')
        magic2.pack()
        magic2.place(y='200')
        btn3 = Button(root, text='я..я не знаю', fg='white', bg='black', height='3', width='10', command=dialog_2)
        btn3.pack()
        btn3.place(y='250', x='75')
        game.place(y='150111', x='50')
        g = Label(root, text='Вы выбрали ответ да кончено', fg='red', bg='black', font='1')
        g.pack()
        g.place(y='150')
                    
                    
                        
    draw = Label(root, text='мг понятно хорошо a можно вопрос?', fg='yellow', bg='black', font='1')
    draw.pack()
    draw.place(y='100')
                    
    game = Button(root, text='ты: Да конечно', fg='white', bg='black', height='3', width='10', command=dialog_1)
    game.pack()
    game.place(y='150', x='50')               
                    

            
                        
def dialog_lvl2():
    def dialog_2_lvl_2():
        def dialog_3_lvl_2():
            
               
            game3.place(y='2510', x='50')
            
        game2.place(y='150', x='501111')
        magic4 = Label(root, text='хорошо Но для начала давай я обясню тебе управление нажимая на "P" ты открываеш магазин а\n нажимая на "M" ты открываешь кошелёк а нажимая на "R" ты открываеш характеристики мечей и брони, чтобы посмотреть свой баланс нажмите на "O", чтобы купить меч подойди к магазинчику и нажми на "P"', fg='yellow', bg='black', font='10')
        magic4.pack()
        magic4.place(y='200')
        game3 = Button(root, text='понятно', fg='white', bg='black', height='3', width='10', command=dialog_3_lvl_2)
        game3.pack()
        game3.place(y='250', x='50')
        g = Label(root, text='Вы выбрали ответ ты да конечно', fg='red', bg='black', font='10')                
        g.pack()
        g.place(y='150')
        
        root.overrideredirect(0)
            
    btn3.place(x='100', y='10000')
    draw = Label(root, text='всмысле не знаешь, может память потерял?, хорошо можеш помочь?', fg='yellow', bg='black', font='1')
    draw.pack()
    draw.place(y='100')
        
    g = Label(root, text='Вы выбрали ответ Я не знаю', fg='red', bg='black', font='1')
    game2 = Button(root, text='ты: Да конечно', fg='white', bg='black', height='3', width='10', command=dialog_2_lvl_2)
    game2.pack()
    game2.place(y='150', x='50')
    g.pack()
    g.place(y='50'), but.place(y='511111110')
                    
                    

   
root = Tk()
root.geometry('1925x750+1+350')
                
    
draw2 = Label(root, text='Привет друг, как я вижу ты не здешний откуда ты?', fg='yellow', bg='black', font='1' )
draw2.pack()																																																													
    

draw2.place(y='10')
    
root.wm_attributes('-alpha', 0.9)

    
btn3 = Button(root, text='соврать,', fg='white', bg='black', height='3', width='10', command = dialog)
btn3.pack()
    
btn3.place(x='100', y='50')
    
imgt = ImageTk.PhotoImage(file='C:/Users/SoaPisGirseb/Desktop/gagaGame/photo/talk.png')
    
root.config(bg='black')
yes = Label(root, image=imgt, text='Волшебник', font='10', bg='black', compound=BOTTOM, width='400', height='700', fg='white' )
yes.pack()
yes.place(x = '1600', y='100')
    
but = Button(root, text='я не знаю', fg='white', bg='black', height='3', width='10', command=dialog_lvl2)
but.pack()
but.place(y='50')  
            
root.overrideredirect(1)
but.pack()
but.place(y='50')
root.mainloop()
            



    
    