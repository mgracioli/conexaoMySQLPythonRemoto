
from usuario import Usuario
from crud import Crud

def main():

    usuario = Usuario('LolInHA LUana')

    tarefas = Crud()

    tarefas.adicionarNovoUsuario(usuario)
    #tarefas.excluirUsuario()
    #tarefas.atualizarDados()

main()

