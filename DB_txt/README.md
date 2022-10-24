# Pacote Interacao

**Pacote Interacao** é um pacote que, como no próprio nome diz, faz a interação com o usuário, anotando o seu CPF, nome e endereço, para que possa ser armazenados no próximo pacote.

# Pacote Armazenamento

**Pacote Armazenamento** é um pacote para gravar as informações obitidas pelo pacote interacao em um arquivo de texto denominado "dados_usuario.txt".

# Pacote Consulta

**Pacote Consulta** é um pacote para consultar, apartir do CPF, os dados armazenados pelo pacote anterior no arquivo "dados_usuario.txt".

## Dependências
**Python 3.6** ou posterior


## Começando o uso
Você vai precisar instalar o pacote **Armazenamento**, para isso basta executar:
```
pip install Armazenamento 
```
Você vai precisar instalar o pacote **Consulta**, para isso basta executar:
```
pip install Consulta 
```
Você vai precisar instalar o pacote **Interacao**, para isso basta executar:
```
pip install Interacao 
```
## Função

* `db_textual()` - Vai perguntar se você quer escolher entre gerar cadastrar, consultar os dados armazenados apartir do CPF préviamente cadastrado ou encerrar o programa.