class AssistenteComprasModa:
    def __init__(self):
        self.preferencias_estilo = []
        self.eventos_planejados = []

    def adicionar_preferencia_estilo(self, estilo):
        self.preferencias_estilo.append(estilo)

    def adicionar_evento_planejado(self, evento):
        self.eventos_planejados.append(evento)

    def recomendar_roupa(self):
        if "formal" in self.preferencias_estilo:
            print("Recomendação de roupa: Terno ou vestido elegante.")
        elif "casual" in self.preferencias_estilo:
            print("Recomendação de roupa: Jeans e camiseta descontraída.")

        for evento in self.eventos_planejados:
            if evento == "festa":
                print("Adicione brilho ao seu look.")
            elif evento == "casamento":
                print("Escolha algo mais formal, como um vestido, terno ou roupas com cores mais básicas.")

assistente_fashion = AssistenteComprasModa()
assistente_fashion.adicionar_preferencia_estilo("casual")
assistente_fashion.adicionar_evento_planejado("festa")
assistente_fashion.recomendar_roupa()
