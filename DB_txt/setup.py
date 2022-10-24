from setuptools import setup
with open('README.md', 'r') as fh:
    readme = fh.read()
setup(
    name='db_txt',
    version='0.0.1',
    packages=['Consulta', 'Interacao', 'Armazenamento'],
    url='https://github.com/wagnerfilh/Meus-trabalhos-academicos/tree/main/DB_txt',
    license='MIT License',
    author='Wagner Wendell Silva Ribeiro Filho',
    long_description=readme,
    long_description_content_type='text/markdown',
    author_email='wagner21070013@aluno.cesupa.br',
    keywords='Pacote',
    description='Uma biblioteca com o foco de armazenar em um .txt informações de CPF, nome e endereço. Podendo ser '
                'acessado por meio do CPF que foi previamente cadastrado. '
)
