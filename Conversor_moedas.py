#Janela 500x50px
#Titulo - Converso de moedas
#Campo de selecionar moedas de origem e destino (campos de listas) com labels delecione a moeda de origem
#Botão de converter
#Lista exibição com os nomes das moedas

import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda
# Criar e configurar a janela
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

dic_conversoes_disponiveis = conversoes_disponiveis()

#dic_conversoes_disponiveis['USD'] => ['BRL', 'CAD', 'BTC', 'AUD']

# Criar os botões, textos e elementos
titulo = customtkinter.CTkLabel(janela, text=('CONVERSOR DE MOEDAS'))
texto_moeda_origem = customtkinter.CTkLabel(janela, text='Selecione a moeda de origem')
texto_moeda_destino = customtkinter.CTkLabel(janela, text='Selecione a moeda de destino')

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])


campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()),
                                                 command=carregar_moedas_destino)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=['Selecione uma moeda de origem'])

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f'1 {moeda_origem} = {cotacao}{moeda_destino}')



botao_converter = customtkinter.CTkButton(janela, text='Converter', command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text='')


moedas_disponiveis = nomes_moedas()
{'BRL': 'Real Brasileiro', 'USD': 'Dólar americanio'}
for codigo_moeda in moedas_disponiveis:
    nomes_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f'{codigo_moeda}: {nomes_moeda}')
    texto_moeda.pack()

#colocar todos os elementos na tela
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=1)
campo_moeda_origem.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx=10, pady=1)
campo_moeda_destino.pack(padx=10, pady=10)
botao_converter.pack(padx=10, pady=10)
texto_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)



# Rodar a janela
janela.mainloop()