# Como fazer uma calculadora de idade em Python.
from tkinter import *
from tkinter import ttk


# ---- importando o tkcalendar ----
from tkcalendar import Calendar, DateEntry

# ---- importando o dateuitl ----
from dateutil.relativedelta import relativedelta

# ---- importando o datetime ----
from datetime import date


# cores ------------
cor1 = '#1f1e1e' # preta / black
cor2 = '#2b2b2b' # cinza escuro / dark cian
cor3 = '#edba5a' # laranja / orange
cor4 = '#fffefc' # branco / white


janela = Tk()
janela.title('Calculadora de Idade')
janela.geometry('310x400')


# Criando o frame_cima ------------
frame_cima = Frame(janela, width= 310, height= 140, pady=0, padx=0, relief=FLAT, bg= cor1)
frame_cima.grid(row=0, column=0)

# Criando frame_baixo --------------
frame_baixo = Frame(janela, width= 310, height= 260, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_baixo.grid(row=1,column=0)


# ------------- CRIANDO LABELS DO FRAME_CIMA --------------

l_calculadora = Label(frame_cima, text='CALCULADORA', width=25, height=1, padx=3, relief=FLAT, anchor=CENTER, font='Ivy 15 bold',
                      bg= cor1, fg=cor4)
l_calculadora.place(x = 0, y = 30)

l_de_idade = Label(frame_cima, text='DE IDADE', width= 11, height=1, padx=0, relief='flat', anchor='center', font='Arial 35 bold',
                   bg= cor1, fg= cor3)
l_de_idade.place(x = 0, y = 70)

# ------------- CRIANDO LABELS MOSTRANDO O FRAME_BAIXO -----------

l_data_inicial = Label(frame_baixo, text='Data inicial', height=1, padx=0, pady=0, relief=FLAT, anchor='nw', font='Ivy 10 bold',
                      bg= cor2, fg=cor4)
l_data_inicial.place(x = 30, y = 30)


cal_1= DateEntry(frame_baixo, width=13, bg='dark blue', fg = cor4, borderwidth=2, date_patter='mm/dd/y', y=2024) # Calendario
cal_1.place(x=170, y=30)



l_data_nascimento = Label(frame_baixo, text='Data de nascimento', height=1, padx=0, pady=0, relief=FLAT, anchor='nw', font='Ivy 10 bold',
                      bg= cor2, fg=cor4)
l_data_nascimento.place(x = 30, y = 60)

cal_2= DateEntry(frame_baixo, width=13, bg='dark blue', fg = cor4, borderwidth=2, date_patter='mm/dd/y', y=2024) # Calendario
cal_2.place(x=170, y=60)

# ------- função calcular idade ----------

def calcular():
    inicial=cal_1.get()
    termino=cal_2.get()

    
    ''' O relativedelta recebe sempre duas datas uma inicial e uma de termino para calcular a sua diferença
     e o .years foi usado aqui pois nessa diferença calculada queremos saber só a parte dos anos. '''

    # separando valores -----------
    mes_1, dia_1, ano_1 = [ int(f) for f in inicial.split('/')]
    data_inicial = date(ano_1, mes_1, dia_1) # convertendo os valores em datetime / date ----

    # separando valores -----------
    mes_2, dia_2, ano_2 = [ int(f) for f in termino.split('/')]
    data_nascimento = date(ano_2, mes_2, dia_2) # convertendo os valores em datetime / date ---- 


    anos = relativedelta(data_inicial, data_nascimento).years
    dias = relativedelta(data_inicial, data_nascimento).days
    meses = relativedelta(data_inicial, data_nascimento).months

    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias
   

# ------- CRIANDO OS LABELS DE ANOS, MESES E DIAS --------


''' label de anos'''
l_app_anos = Label(frame_baixo, text='27', height=1, padx=0, pady=0, relief=FLAT, anchor='center', font='Ivy 25 bold',
                      bg= cor2, fg=cor4)
l_app_anos.place(x = 60, y = 135)

l_nome_anos = Label(frame_baixo, text='Anos', height=1, padx=0, pady=0, relief=FLAT, anchor='center', font='Ivy 15 bold',
                      bg= cor2, fg=cor4)
l_nome_anos.place(x = 50, y = 180)

'''label de Dias'''
l_app_meses = Label(frame_baixo, text='12', height=1, padx=0, pady=0, relief=FLAT, anchor='center', font='Ivy 25 bold',
                      bg= cor2, fg=cor4)
l_app_meses.place(x = 140, y = 135)

l_nome_meses = Label(frame_baixo, text='Dias', height=1, padx=0, pady=0, relief=FLAT, anchor='center', font='Ivy 15 bold',
                      bg= cor2, fg=cor4)
l_nome_meses.place(x = 125, y = 180)

'''label de Meses'''
l_app_dias = Label(frame_baixo, text='30', height=1, padx=0, pady=0, relief=FLAT, anchor='center', font='Ivy 25 bold',
                      bg= cor2, fg=cor4)
l_app_dias.place(x = 220, y = 135)

l_nome_dias = Label(frame_baixo, text='Meses', height=1, padx=0, pady=0, relief=FLAT, anchor='center', font='Ivy 15 bold',
                      bg= cor2, fg=cor4)
l_nome_dias.place(x = 220, y = 180)

# -------- CRIANDO O BATÃO ---------
b_calcular = Button(frame_baixo,command=calcular, text='CALCULAR IDADE', height=1, width=20, relief=RAISED, overrelief='ridge', font='Ivy 10 bold',
                      bg= cor2, fg=cor4)
b_calcular.place(x = 70, y = 225)


janela.mainloop()


