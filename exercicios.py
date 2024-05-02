class exercicios:
    def __init__(self, nome, idade, sexo, status):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.status = status

    def exericicios():
        nome = "Maria Eduarda"
        idade = 17
        sexo = "feminino"
        status = True
        print("Meu nome é:", nome, "tenho", idade, "anos", sexo, "sexo", status, "status")

    def exericio2 (self):
        alunos = ["bibizinha", "danilevousoco", "mariapombamurcha", "justinheineken"]
        notas = [1, 2, 3, 4]
        print("Alunos:")
        for aluno in alunos:
            print(aluno)

        print("\nNotas:")
        for nota in notas:
            print(nota)

            



Mariaeduarda = exercicios("maria eduarda", 17, "machuco mendigos", True)
Mariaeduarda.exercicios1()


    