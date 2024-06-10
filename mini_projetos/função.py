# Aqui vamos criar a logica que sera usada no programa datas_funções:
from datetime import datetime

# Aqui puxamos a todas informações do dia de hoje com base no seu computador:
def today():
    today = datetime.now()
    return today

# Vamos criar uma função para verificar a formatação da data:
def verify_date(date):
    try: # Aqui ele vai tentar executar o que esta abaixo
        date_format = datetime.strptime(date, '%d-%m-%Y') # %d - dia | %m - mês | %Y(maiusculo) - ano
        return date_format
    except: # Se ele não conseguir ele vai parar o programa e disparar um erro.
        raise Exception('Entrada invalida! Formato sugerido: dd-mm-aaaa.') 



# Agora vamos comparar o dia de hoje com a data de vencimento:
def verify_due(date_ref):
    due_date = verify_date(date = date_ref)
    if today() > due_date:
        return 'Data expirou....'
    else:
        return 'Data não expirou...'


