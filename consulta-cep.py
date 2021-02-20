import requests
import os


#autor: Thiago Araújo
#Consulta de CEP básico em Python 3


#apresentação
print("""

    ##########################
    #### Consulta CEP ########
    ################## V0.1 ##



""")

#resposta recebe True ou False
resposta = True

#loop
while resposta:
    #aqui é a entrada de dados ou seja o CEP a ser pesquisado
    cep = input("Digite o CEP: ")

    #aqui verifica se o cep tem 8/ digitos se for diderente ele exibe a mensagem de inválido
    if len(cep) !=8:
        #exibe mensagem
        print("Quantidade de Digitos Inválidos!") 
        exit()

    #aqui é API de consulta em JSON
    request =  requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    #aqui ele recebe as informções da API
    addresss_data = request.json()

    
    #aqui verifica se a resposta erro na consulta se não tiver ele mostra as seguintes informações 
    if 'erro' not in  addresss_data:
        
        #aqui são as informções pega do json e printada na Tela
        print("CEP: {}".format(addresss_data['cep'])) #aqui mostra o cep
        print("Endereço: {}".format(addresss_data['logradouro'])) #aqui mostra o endereço
        print("Bairro: {}".format(addresss_data['bairro'])) #aqui mostra o bairro
        print("Cidade: {}".format(addresss_data['localidade'])) #aqui mostra a cidade
        print("Estado: {}".format(addresss_data['uf'])) #aqui mostra o Estado

        #aqui é a entrada para saber se o user que sair ou fazer uma nova consulta 
        rp = input("Deseja Consultar outro cep? S/N: ")
        os.system('clear') or None

        #aqui verifica se a entrada é igual se for não ele sai do programa se for diferente ou seja sim ele continua no loop
        if rp.lower() == 'nao':
            exit()
            

    #se caso o CEP for inválido ele exibe essa mensagem de erro
    else:
        print("{} CEP Inválido!".format(cep))


