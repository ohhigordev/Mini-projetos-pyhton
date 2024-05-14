salario = 2000


def salario_bonus(bonus):
    global salario # isso serve para a funcção buscar valores que estão fora dela, ou seja, valores globais.
    salario += bonus
    return salario


salario_bonus(500)  # 25000

