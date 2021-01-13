from enum import Enum
from glob import glob
import os
import re
from pprint import pprint
class Grupo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.nome, self.numero = self.extrair_nome_numero()
        self.alunos = Aluno.extrair_alunos(self.arquivo)

    def extrair_nome_numero(self):
         padrao_grupo = r"Conversa do WhatsApp com (\[(\d{1,})].*)"
         resultado = re.search(padrao_grupo,self.arquivo, re.MULTILINE)
         nome = resultado.group(1)
         numero = resultado.group(2)

         return nome, numero

    def importar_grupos():
        caminho_conversas = 'conversas' + os.path.sep
        return glob(caminho_conversas + '*.txt')
        

    def remover_duplicados():
        ...

class Operacao(Enum):
    ENTRADA = 1
    SAIDA = 2
    MUDANCA = 3

class Aluno:
    def __init__(self, numero):
        self.numero = numero
        self.presente = True
    
    def extrair_alunos(arquivo):
        padrao_aluno = r"([\d/ :]*) - *(\+55 [\d\s-]*) (entrou|saiu)(\+55 [\d\s-]*$)?"
        alunos = []
        with open(arquivo, encoding='UTF-8') as arq:
            conversa = arq.readlines()

        for linha in conversa:
            resultado = re.search(padrao_aluno,linha,re.MULTILINE)

            if resulta != None:
                horario = resultado.group(1)
                numero = resultado.group(2)
                operacao = resultado.group(3)
                novo_numero =resultado.group(4)

                print("||", horario,numero,operacao, novo_numero)

                if novo_numero is not None:
                    for aluno in alunos:
                        if aluno.numero == numero:
                            aluno.alterar_numero(novo_numero)
                elif 'entrou' in operacao:
                    aluno = Aluno.criar_aluno(numero)
                    aluno.entrada_saida(Operacao.ENTRADA, horario)
                    alunos.append(aluno)
                else
                    for aluno in alunos:
                        if aluno.numero == numero:
                            aluno.entrada_saida(Operacao.SAIDA, horario)               




    def alterar_numero(self, novo_numero):
        self.numero = novo_numero
    def criar_aluno(numero):
        return Aluno(numero)

    def entrada_saida(self, operacao, horario):
        if operacao == Operacao.ENTRADA:
            self.data_entrada = horario
        else:
            self.data_saida = horario

    def remover_duplicatas(alunos):

    def exportar_contatos(arquivo, alunos):

if __name__ == '__main__':
   arquivos_grupos = Grupo.importar_grupos()
   arquivos_grupo = arquivos_grupos[0]

   pprint(arquivos_grupo)
   grupo = Grupo(arquivos_grupo)

   print(f'Grupo: {grupo.nome} \nNúmero: {grupo.numero}')


