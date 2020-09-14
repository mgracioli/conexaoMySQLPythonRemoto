#cria um modelo de usuário

class Usuario(object):
    #método construtor
    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome.title()