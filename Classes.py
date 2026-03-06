class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        self.ataque = ""
    
    def Atacar(self):
        if self.tipo == "mago":
            self.ataque = "magia"
        elif self.tipo == "guerreiro":
            self.ataque = "espada"
        elif self.tipo == "monge":
            self.ataque = "artes marciais"
        elif self.tipo == "ninja":
            self.ataque = "shuriken"
        else:
            self.ataque = "sua arma"
        
        print(f"O {self.tipo} atacou usando {self.ataque}")

    
while True:
    nome = input('Qual é o nome do heroi? ')
    idade = int(input('Qual é a idade do heroi? '))
    tipo = input('Qual é o tipo de heroi? [mago, guerreiro, monge ou ninja]: ')
    
    heroi = Heroi(nome, idade, tipo) 
    heroi.Atacar() 
    
    sair = input('Deseja criar um novo heroi? [s/n] ')
    
    if sair.lower() == 'n':
        break

    
