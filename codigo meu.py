# Passo a passo do projeto 

# Passo 1 - Entrar no sistema da empresa
 # https://dlp.hashtagtreinamentos.com/python/intensivao/login


import pyautogui
import time


# clicar = pyautogui.click
# escrever = pyautogui.write
# apertar uma tecla = pyautogui.press

# Fazer o código de um jeito mais lento
pyautogui.PAUSE = 1
# Aperta a tecla win
pyautogui.press('win')
# Digita a palavra a ser pesquisada
pyautogui.write('Chrome')
# Digita uma tecla
pyautogui.press('Enter')

# Digitar o link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# Pressionar o Enter
pyautogui.press('Enter')

# Adicionar tempo de espera

time.sleep(1)

# Passo 2 - Fazer login
pyautogui.click(x=730, y=506)

# Digitando o e-mail
pyautogui.write('emaildeteste@gmail.com')

# indo para o campo de baixo 
pyautogui.press('Tab')

#digitando a senha 
pyautogui.write('kkeaeman')

# Ir para o campo de baixo 
pyautogui.press('Tab')

# Finalizando o login
pyautogui.press('Enter')

pyautogui.click(x=631, y=349)


# Importar a base de dados  

import pandas
tabela = pandas.read_csv('produtos-01.csv')
print(tabela)


# Cadastrar um produto 

#codigo
pyautogui.write('MOLO000251')
pyautogui.press('tab')
# MARCA 
pyautogui.write('logitech')
pyautogui.press('tab')
# Tipo 
pyautogui.write('Mouse')
pyautogui.press('tab')
#categoria
pyautogui.write(str(1))
pyautogui.press('tab')
# Preço 
pyautogui.write('25.95')
pyautogui.press('tab')
# Custo
pyautogui.write('6.50')
pyautogui.press('tab')
#Obs 
pyautogui.write('')
pyautogui.press('tab')
#Enviar o produto
pyautogui.press('Enter')



# Repetir isto até acabar a base de dados Chrome

