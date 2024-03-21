import bcrypt
import random

from servidor import Servidor
servidor = Servidor()

class Sessoes():
    def gerar_sequencia(self):
        digitos_unicos = random.sample(range(10), 10)
        return ''.join(map(str, digitos_unicos))
    

    def GerarSessoes(self):
        dados = [self.gerar_sequencia() for _ in range(1000)]
        for dado in dados:
            valor_aleatorio = str(random.randint(0, 999999999))
            hash_obj = bcrypt.hashpw(valor_aleatorio.encode('utf-8'))
            hash_calculado = hash_obj.hexdigest()
            mydb = servidor.conecta()
            mydb.inserirSessoes(hash_calculado, dado)

    def BuscarSessaoValida(self):
        mydb = servidor.conecta()
        mydb.LiberarSessoes()
        linha = mydb.buscarDado('Sessoes', 'hash, ordem', f'disponivel = 1')
        hashRetorno = linha[0][0]
        OrdemRetorno = linha[0][1]
        mydb.AtualizarRegistro('Sessoes', 'disponivel = 0, ultima_vez_usado = GETDATE()', f"hash = '{hashRetorno}'")
        return hashRetorno, OrdemRetorno
