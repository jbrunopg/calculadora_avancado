from tkinter import *
from tkinter import ttk

# cor
cor1 = "#3b3b3b" #preto
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #laranja

janela =Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

# criando frames
frame_tela = Frame(janela, width=235, height=50,bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268,bg=cor1)
frame_corpo.grid(row=0, column=0)

#criando botões

b_1 = Button(frame_corpo, text="C", width=11, height=2)

janela.mainloop()
