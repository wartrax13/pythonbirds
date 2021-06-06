class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'    

if __name__ == '__main__':
    renzo = Pessoa(nome='Pedro')
    pedro = Pessoa(renzo, nome='Renzo')
    print(Pessoa.cumprimentar(pedro))
    print(id(pedro))
    print(pedro.cumprimentar())
    print(pedro.nome)
    print(pedro.idade)
    for filho in pedro.filhos:
        print(filho.nome)
    pedro.sobrenome = 'Andrade'
    del pedro.filhos
    print(pedro.__dict__)
    print(renzo.__dict__)
