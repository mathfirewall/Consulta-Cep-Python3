import requests
import os


#autor: Thiago Araújo
#Consulta de CEP básico em Python 3

print("""

    ##########################
    #### Consulta CEP ########
    ################## V0.1 ##



""")
resposta = True
while resposta:
    cep = input("Digite o CEP: ")


    if len(cep) !=8:
        print("Quantidade de Digitos Inválidos!") 
        exit()

    request =  requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    addresss_data = request.json()

    if 'erro' not in  addresss_data:

        print("CEP: {}".format(addresss_data['cep']))
        print("Endereço: {}".format(addresss_data['logradouro']))
        print("Bairro: {}".format(addresss_data['bairro']))
        print("Cidade: {}".format(addresss_data['localidade']))
        print("Estado: {}".format(addresss_data['uf']))

        rp = input("Deseja Consultar outro cep? S/N: ")
        os.system('clear') or None
        if rp.lower() == 'nao':
            exit()
            


    else:
        print("{} CEP Inválido!".format(cep))


