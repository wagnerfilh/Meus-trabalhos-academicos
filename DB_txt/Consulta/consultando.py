def busca():
    arquivo = open(r'Armazenamento\dados_usuario.txt', 'r')
    cpf_cad = input('Digite o seu CPF cadastrado: ')
    cpf = cpf_cad+'\n'
    linha_str = arquivo.readlines()
    if cpf in linha_str:
        linha_array = linha_str.index(cpf)
        print(f'O CPF cadastrado é: {linha_str[linha_array]}O NOME cadastrado é: {linha_str[linha_array+1]}O ENDEREÇO cadastrado é: {linha_str[linha_array+2]}')
    else:
        print("ERRO! CPF não cadastrado!")