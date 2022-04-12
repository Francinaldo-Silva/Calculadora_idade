from datetime import datetime

try:
        ano_nas = int(input('Ano em que nasceu: '))
        mes_nas = int(input('Mês que nasceu: '))
        dia_nas = int(input('Dia que nasceu: '))
except ValueError:
    print('Digite somente números')

data_nas = datetime(ano_nas, mes_nas, dia_nas)
data_atual = datetime.now()

diff = data_atual - data_nas

dias = diff.days
anos, dias = dias // 365, dias % 365
meses, dias =  dias // 30, dias % 30

print(f'Você tem: {anos} anos {meses} meses e {dias} dias')
