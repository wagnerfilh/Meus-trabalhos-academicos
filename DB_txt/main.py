import Armazenamento.salvando
import Consulta.consultando

def db_textual():
    continuar = 0
    while continuar != 3:
        continuar = int(input('Digite [1] para cadastrar [2] para consultar seu cadastro [3] para sair: '))
        if continuar == 1:
            Armazenamento.salvando.memorinha()
        if continuar == 2:
            Consulta.consultando.busca()
    print(('Programa encerrado'))

db_textual()