class AssistenteTreinamentoGatosSimples:
    def __init__(self):
        self.sensor_idade = 0

    def coletar_dados_sensores(self, idade):
        self.sensor_idade = idade

    def analisar_padrões_atividade(self):
        if self.sensor_idade < 3:
            return "Alta atividade para gatos jovens e saudáveis."
        elif self.sensor_idade >= 3:
            return "Necessidade de aumentar a atividade para gatos mais velhos com baixa condição física."


    def gerar_plano_exercicios(self):
        padrao_atividade = self.analisar_padrões_atividade()

        if "Alta atividade" in padrao_atividade:
            return "Plano de exercícios vigorosos."
        elif "Necessidade de aumentar" in padrao_atividade:
            return "Plano de exercícios moderados e supervisionados."
        else:
            return "Plano de exercícios leves e regulares."


agente_gato = AssistenteTreinamentoGatosSimples()
agente_gato.coletar_dados_sensores(2, 60)
plano_exercicios = agente_gato.gerar_plano_exercicios()
print(plano_exercicios)
