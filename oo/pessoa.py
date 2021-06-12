class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 26):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe= super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    renzo = Mutante(nome='Pedro')
    pedro = Homem(renzo, nome='Renzo')
    print(Pessoa.cumprimentar(pedro))
    print(id(pedro))
    print(pedro.cumprimentar())
    print(pedro.nome)
    print(pedro.idade)
    for filho in pedro.filhos:
        print(filho.nome)
    pedro.sobrenome = 'Andrade'
    del pedro.filhos
    pedro.olhos = 1
    del pedro.olhos
    print(pedro.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(pedro.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(pedro.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), pedro.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), pedro.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa)) # verdadeiro: a pessoa acima é uma pessoa
    print(isinstance(pessoa, Homem)) #falso: uma pessoa nao necessariamente é um Homem
    print(isinstance(renzo, Pessoa))  # verdadeiro: a pessoa acima é uma pessoa
    print(isinstance(renzo, Homem))  # falso: uma pessoa nao necessariamente é um Homem
    print(renzo.olhos)
    print(pedro.cumprimentar())
    print(renzo.cumprimentar())