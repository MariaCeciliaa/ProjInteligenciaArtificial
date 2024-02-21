class CoachBemEstarAnimal:
    def __init__(self):
        self.idade = 0
        self.condicao_fisica = 0
        self.historico_exercicios = []
        self.estado_emocional = "feliz"

    def definir_idade(self, idade):
        self.idade = idade

    def definir_condicao_fisica(self, condicao):
        self.condicao_fisica = condicao

    def adicionar_exercicio(self, exercicio):
        self.historico_exercicios.append(exercicio)

    def avaliar_emocional(self, estado_emocional):
        self.estado_emocional = estado_emocional

    def gerar_plano_exercicios(self):
        plano_exercicios = []

        if self.idade <= 9 and self.condicao_fisica == "boa":
            plano_exercicios.append("Brincadeiras intensas e escalada em morros de grama.")
        elif self.idade > 9 and self.condicao_fisica == "boa":
            plano_exercicios.append("Passeios diários e atividades mais leves.")
        if "corrida" in self.historico_exercicios:
            plano_exercicios.append("Incluir corridas regulares no plano.")
        elif "caminhada" in self.historico_exercicios:
            plano_exercicios.append("Adicionar caminhadas diárias ao plano.")

        if self.estado_emocional == "contente":
            plano_exercicios.append("Escolha atividades que seu animal desfrute para manter o contentamento.")

        print("Plano de exercícios gerado:")
        for exercicio in plano_exercicios:
            print(f"- {exercicio}")

coach_animal = CoachBemEstarAnimal()
coach_animal.definir_idade(5)
coach_animal.definir_condicao_fisica("boa")
coach_animal.adicionar_exercicio("corrida")
coach_animal.avaliar_emocional("contente")
coach_animal.gerar_plano_exercicios()
