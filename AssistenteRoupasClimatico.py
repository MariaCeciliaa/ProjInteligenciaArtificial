class AssistenteRoupasClimatico:
    def __init__(self):
        self.temperatura_atual = None

    def perceber_clima(self, temperatura):
        self.temperatura_atual = temperatura

    def recomendar_roupas(self):
        if self.temperatura_atual is None:
            return "Não foi possível determinar a temperatura."

        if self.temperatura_atual <= 18:
            return "É recomendado que você utilize roupas de frio, pois o clima está mais ameno. ❄️"
        else:
            return "É recomendado que você utilize roupas mais leves, pois o clima está quente. ☀️"

assistente = AssistenteRoupasClimatico()

temperaturaFria = 15
temperaturaQuente = 25

assistente.perceber_clima(temperaturaFria)
print(assistente.recomendar_roupas())

assistente.perceber_clima(temperaturaQuente)
print(assistente.recomendar_roupas())
