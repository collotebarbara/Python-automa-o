# Passo 1: Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar com mouse
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> apertar um atalho no teclado (ctrl, C etc)

# abrindo o site no navegador 
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# pausa de 3 segundos 
time.sleep(2)
pyautogui.click(x=2659, y=406)
pyautogui.write('babicollote@gmail.com')
pyautogui.press('tab')
pyautogui.write('123258')
pyautogui.press('enter')

# passo 3: importar base de dados: pandas 
import pandas
tabela = pandas.read_csv('produtos.csv')
print(tabela)

# passo 4: cadastrar produto


for linha in tabela.index:
    pyautogui.click(x=2630, y=290)
    
    # pyautogui.hotkey('ctrl', 'a')  # Seleciona tudo no campo
    # pyautogui.press('backspace')   # Apaga o conteúdo selecionado


    # codigo do prod
    codigo = tabela.loc[linha,'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    # marca do prod
    marca = tabela.loc[linha,'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    # tipo de prod
    tipo = tabela.loc[linha,'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    # categoria do prod
    categoria = tabela.loc[linha,'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    # preço unitario do prod
    preco = tabela.loc[linha,'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('tab')

    # custo do prod
    custo = tabela.loc[linha,'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    #obs 
    obs = tabela.loc[linha,'obs']
    if not pandas.isna(obs): # se  o campo nao estiver vazio, escreva 
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    
    pyautogui.press('enter')
    pyautogui.scroll(3000)