class AssistenteTreinamentoGatos:
    def __init__(self):
        self.idade = None
        self.condicao_fisica = None
        self.historico_exercicios = []
        self.plano_exercicios_personalizado = None

    def perceber_gato(self, idade, condicao_fisica, historico_exercicios):
        self.idade = idade
        self.condicao_fisica = condicao_fisica
        self.historico_exercicios = historico_exercicios

    def atualizar_modelo(self):
        adaptacao_idade = self.adaptar_exercicios_por_idade()
        avaliacao_condicao = self.avaliar_condicao_fisica()
        analisar_historico = self.analisar_historico_exercicios()

        self.plano_exercicios_personalizado = f'''
A partir dos estudos feitos, o melhor treinamento para seu gato seria:
    - Analisando a idade: {adaptacao_idade}
    - Analisando a condição física: {avaliacao_condicao}
    - Analisando o histórico de exercícios: {analisar_historico}'''

    def adaptar_exercicios_por_idade(self):
        if self.idade <= 9:
            return "Fazer exercícios todos os dias da semana."
        else:
            return "Fazer exercícios 3 vezes por semana."

    def avaliar_condicao_fisica(self):
       if self.condicao_fisica == "boa":
            return "Fazer exercícios de alto impacto, como estimular a escalada em vários lugares da casa."
       elif self.condicao_fisica == "intermediária":
            return "Fazer exercícios de medio impacto, como brincar."
       elif self.condicao_fisica == "ruim":
            return "Fazer exercícios de pouco impacto, como espreguiçar e alongar."

    def analisar_historico_exercicios(self):
        if any("brincadeira" in exercicio.lower() for exercicio in self.historico_exercicios):
            return "Seu gato iniciára com exercícios mais dinâmicos."
        elif any("corrida" in exercicio.lower() for exercicio in self.historico_exercicios):
            return "Seu gato iniciára com exercícios mais focados."

    def recomendar_plano_exercicios(self):
        if self.plano_exercicios_personalizado is None:
            return "Não foi possível determinar um plano de exercícios personalizado."

        return self.plano_exercicios_personalizado


assistente_gatos_1 = AssistenteTreinamentoGatos()

idade_gato_1 = 3
condicao_fisica_gato_1 = "boa"
historico_exercicios_gato_1 = ["brincadeira com bolinha", "brincadeira com novelo de lã"]

assistente_gatos_1.perceber_gato(idade_gato_1, condicao_fisica_gato_1, historico_exercicios_gato_1)
assistente_gatos_1.atualizar_modelo()
plano_exercicios_recomendado = assistente_gatos_1.recomendar_plano_exercicios()

print(plano_exercicios_recomendado)


assistente_gatos_2 = AssistenteTreinamentoGatos()

idade_gato_2 = 11
condicao_fisica_gato_2 = "intermediária"
historico_exercicios_gato_2 = ["corridas matinais", "escaladas"]

assistente_gatos_2.perceber_gato(idade_gato_2, condicao_fisica_gato_2, historico_exercicios_gato_2)
assistente_gatos_2.atualizar_modelo()
plano_exercicios_recomendado = assistente_gatos_2.recomendar_plano_exercicios()

print(plano_exercicios_recomendado)