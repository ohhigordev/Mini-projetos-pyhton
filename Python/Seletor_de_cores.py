from tkinter import *
import tkinter.messagebox

'''
Esse messagebox será usado nesse programa para quando a cor que pedirmos para ser copiada para a área de
tranferência ele avisa que a cor foi copiada.
'''
#cores ------------------------
cor0 = '#444466' # Preta
cor1 = '#feffff' # Branca
cor2 = '#004338'
cor3 = '#202120' # Cinza 

#Criando a janela -------------

janela = Tk()
janela.geometry('530x205')
janela.configure(bg=cor1)



#configurando janela ------------

tela = Label(janela, bg=cor3, width=40, height=10, bd=1)
tela.grid(row=0, column=0)

fram_direita = Frame(janela, bg=cor1, padx=5)
fram_direita.grid(row=0, column=1)

frame_baixo = Frame(janela, bg=cor1)
frame_baixo.grid(row=1, column=0, columnspan=2, pady=15)


#função scale -------------------
def escala(valor):
    r = s_red.get()
    g = s_green.get()
    b = s_blue.get()

    

    rgb = f'{r}, {g}, {b}' # Aqui foi criada uma formated string para receber os valores da variaveis a cima.

    '''==== Vamos converter esse corpo RGB em Hexadecimal. ===='''
    hexadecimal = "#%02x%02x%02x" % (r, g, b)

    tela['bg'] = hexadecimal # isso aqui faz com que o código hexadecimal reflita na tela em formato de cor.

    # Alterando a Entry ----------
    e_cor.delete(0, END)
    e_cor.insert(0, hexadecimal)
    '''
    Isso daqui mostra o código hexadecimal na Entry para ser cópiado.
    '''

# Função clicar/deslizar -----------
def onClick():
    
    #Infromar
    tkinter.messagebox.showinfo('Cor', 'a cor foi copiada.')



    # Serve para criar o botão copiar.
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(e_cor.get())
    clip.destroy



#configurando o frame direita -------
''' === CONFIGURAÇÃO DO RED ==='''
l_red = Label(fram_direita,text='RED',width=7, bg=cor1, fg='red', anchor='nw',font='Time 12 bold')
l_red.grid(row=0, column=0)
s_red = Scale(fram_direita,command=escala, from_= 0, to=255, length=150, bg=cor1, fg='Red', orient=HORIZONTAL)
s_red.grid(row=0, column=1)

'''=== CONFIGURAÇÃO DO GREEN ==='''
l_green = Label(fram_direita,text='GREEN',width=7, bg=cor1, fg='green', anchor='nw',font='Time 12 bold')
l_green.grid(row=1, column=0)
s_green = Scale(fram_direita,command=escala, from_= 0, to=255, length=150, bg=cor1, fg='green', orient=HORIZONTAL)
s_green.grid(row=1, column=1)

'''=== CONFIGURAÇÃO DO BLUE ==='''
l_blue = Label(fram_direita,text='BLUE',width=7, bg=cor1, fg='blue', anchor='nw',font='Time 12 bold')
l_blue.grid(row=2, column=0)
s_blue = Scale(fram_direita,command=escala, from_= 0, to=255, length=150, bg=cor1, fg='blue', orient=HORIZONTAL)
s_blue.grid(row=2, column=1)


#configurando frame_baixo ------
l_rgb = Label(frame_baixo,text='Código HEX :', bg=cor1, font='Ivy 10 bold') # frame que está abaixo do display das cores.
l_rgb.grid(row=0, column=0, padx=5)

e_cor = Entry(frame_baixo, width=12, font='Ivy 10 bold', justify=CENTER ) # entrada do código RGB.
e_cor.grid(row=0, column=1, padx=5)

#Botão Copiar ------------------
b_copiar = Button(frame_baixo, command=onClick, text='Copiar a cor:', bg=cor1, font='Ivy 8 bold', relief=RAISED, overrelief=RIDGE)
b_copiar.grid(row=0, column=2, padx=5)

#Nome do APP -------------------
l_app_nome = Label(frame_baixo,text='Seletor de Cores', bg=cor1, fg=cor3, font='Ivy 15 bold')
l_app_nome.grid(row=0, column=3, padx=10)


janela.mainloop()