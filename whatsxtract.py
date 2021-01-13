from glob import glob
import os
import re
from pprint import pprint
class Grupo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.nome, self.numero = self.extrair_nome_numero()
        self.alunos = '' #Alunos.extrair_alunos

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
if __name__ == '__main__':
   arquivos_grupos = Grupo.importar_grupos()
   arquivos_grupo = arquivos_grupos[0]

   pprint(arquivos_grupo)
   grupo = Grupo(arquivos_grupo)

   pprint(f' Grupo: {grupo.nome} \n Número: {grupo.numero}')


