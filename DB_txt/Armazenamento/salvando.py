import Interacao.inputs_usuario


def memorinha():
    with open(r'Armazenamento\dados_usuario.txt', 'a+') as arq:
        arq.writelines(Interacao.inputs_usuario.interac() + '\n')
