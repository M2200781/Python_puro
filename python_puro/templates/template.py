import sys
import os
sys.path.append(os.path.abspath(os.curdir))

from model.password import Password
from views.password_views import FernetHasher


action = input('Digite 1 salvar uma nova senha ou 2 para ver uma determinada senha: ')
if action == '1':
    if len(Password.get()) == 0:
            key, path = FernetHasher.create_key(archive=True) 
            print('Sua chave foi criada com sucesso, salve-a com cuidaddo.')
            print(f'Chave: {key.decode("utf-8")}')
            if path:
                 print('Chave salva no arquivo, lembre-se de remover o arquivo após o transferir de local')
                 print(f'Caminho: {path}')
    else:
        key = input('Digite sua chave usada para criptografia, use sempre a mesma chave: ')
    domain = input('Domínio: ')
    password = input('Digite a senha: ')
    fernet = FernetHasher(key)
    p1 = Password(domain=domain, password=fernet.encrypt(password).decode('utf-8'))
    p1.save()

elif action == '2':
    domain = input('Domínio: ')
    key = input('Key: ')
    fernet = FernetHasher(key)
    data = Password.get()

    for i in data:
        if domain in i['domain']:
            password = fernet.decrypt(i['password'])
    if password:
        print(f'Sua senha: {password}')
    else:
        print('Nenhuma senha encontrada para esse domínio.')



    #Para criar outras chaves: digite a opção 1 no terminal quando rodar o template.py
    #Copie a chave gerada no arquivo .key gerada na pasta keys e cole em 'Digite sua chave usada para criptografia, use sempre a mesma chave: ' no terminal
    #Digite um novo dominio ex: blabla.com.br
    #Crie uma senha ex: 123456
    #na pasta db será gerada um arquivo Password.txt 
    # ex: blabla.com.br|gAAAAABnJ6-RjieDYPIErSR9n5Ca56k4yaeAXWG1xY6fYaEVwX93qeKHBUFjeC_RduFVFpkVQKBRYOaaPeffEijhCFNju6WzeA==|2024-11-03T14:14:57.687497