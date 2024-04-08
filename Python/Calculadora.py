from tkinter import *
from tkinter import ttk

# cores
cor1 = '#1c1c1b'  # Preta / Black
cor2 = '#feffff'  # Branca / White
cor3 = '#38576b'  # Azul Carregado
cor4 = '#ECEFF1'  # Cinzenta
cor5 = '#FFAB40'  # Laranka / Orange

# Configurações da janela
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=cor1)


# Configurações da tela onde aparece os números da calcauladora
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

# Configurações do corpo da calculadora
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# VARIAVEL TODOS OS VASLORES.
todos_valores = ''

'''=== CRIANDO FUNÇÃO ==='''
def entrar_valores(event):

    global todos_valores    


    todos_valores = todos_valores + str(event)
    
    
    ''' PASSANDO O VALOR PARA A TELA.'''
    valor_texto.set(todos_valores)



'''=== FUNÇÃO PARA CALCULAR ==='''
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))


''' === LIMPAR TELA ==='''
def limpar_tela():
    global todos_valores  # todas as coisas que foram feitas com essa varialvel seram alteradas onde ela estiver.
    todos_valores = ''
    valor_texto.set('')




# CRIANDO LABEL
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT,
                  font='Ivy 18', bg=cor3, fg=cor2)
app_label.place(x=0, y=0)




# Criando os botões da calculadora
'''=== PRIMEIRA FILA DA CALCULADORA ==='''
b_1 = Button(frame_corpo, command=limpar_tela, text='AC', width=11, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text='%', width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_corpo,  command= lambda: entrar_valores('/'), text='/', width=5, height=2, bg=cor5, fg=cor2, font="Ivy 13 bold", relief=RAISED,
             overrelief=RIDGE)
b_3.place(x=180, y=0)
'''
=> 'relief = RAISED'. Esse comando define um parametro de borda a um determinado widget, o estilo usado foi o 'RAISED'
que pode ser explicado como deixar uma coisa com um aspecto mais avantajado ou um borda mais elevada.

=> 'overrelief=RIDGE'. Esse comando  define um estilo de borda de um widge quando o mouse está sobre ele, o valor
'RIDGE' define uma borda saliente, criano um efeito de relevo para o widge quando o mouse está sobre ele.
'''
'''=== SEGUNDA FILA DA CALCULADORA ==='''
b_4 = Button(frame_corpo, command= lambda: entrar_valores('9'), text='9', width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=53)
b_5 = Button(frame_corpo, command= lambda: entrar_valores('8'), text='8', width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=53)
b_6 = Button(frame_corpo, command= lambda: entrar_valores('7'), text='7', width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_6.place(x=120, y=53)
b_7 = Button(frame_corpo,  command= lambda: entrar_valores('*'), text='*', width=5, height=2, bg=cor5, fg=cor2, font="Ivy 13 bold", relief=RAISED,
             overrelief=RIDGE)
b_7.place(x=180, y=53)
'''=== TERCEIRA FILA DA CALCULADORA ==='''
b_8 = Button(frame_corpo, command= lambda: entrar_valores('4'), text='4', width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=105)
b_9 = Button(frame_corpo, command= lambda: entrar_valores('5'), text='5', width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=105)
b_10 = Button(frame_corpo, command= lambda: entrar_valores('6'), text='6', width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_10.place(x=120, y=105)
b_11 = Button(frame_corpo, command= lambda: entrar_valores('-'), text='-', width=5, height=2, bg=cor5, fg=cor2, font="Ivy 13 bold", relief=RAISED,
              overrelief=RIDGE)
b_11.place(x=180, y=105)
'''=== QUARTA FILA DA CALCULADORA ==='''
b_12 = Button(frame_corpo, command= lambda: entrar_valores('1'), text='1', width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=157)
b_13 = Button(frame_corpo, command= lambda: entrar_valores('2'), text='2', width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=157)
b_14 = Button(frame_corpo, command= lambda: entrar_valores('3'), text='3', width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_14.place(x=120, y=157)
b_15 = Button(frame_corpo, command= lambda: entrar_valores('+'), text='+', width=5, height=2, bg=cor5, fg=cor2, font="Ivy 13 bold", relief=RAISED,
              overrelief=RIDGE)
b_15.place(x=180, y=157)
'''=== QUINTA FILA DA CALCULADORA ==='''
b_16 = Button(frame_corpo, command= lambda: entrar_valores('0'), text='0', width=11, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=209)
b_17 = Button(frame_corpo, command= lambda: entrar_valores('.'), text='.', width=5, height=2, bg=cor4, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b_17.place(x=120, y=209)
b_18 = Button(frame_corpo, command=calcular, text='=', width=5, height=2, bg=cor5, fg=cor2, font="Ivy 13 bold", relief=RAISED,
             overrelief=RIDGE)
b_18.place(x=180, y=209)



janela.mainloop()

