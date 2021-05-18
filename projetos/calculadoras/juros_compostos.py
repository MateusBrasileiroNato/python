class JurosCompostos():
    
    def __init__(self, capital_inicial, taxa, periodo, juros, montante):
        self.capital_inicial = capital_inicial
        self.capital_inicial = capital_inicial
        self.taxa = taxa / 100
        self.periodo = periodo
        self.juros = juros
        self.montante = montante

    def calculo_montante(self):
        self.montante = self.capital_inicial * ((1 + self.taxa) ** self.periodo)
        return self.montante

    def calculo_capital_inicial(self):
        self.capital_inicial = self.montante / ((1 + self.taxa) ** self.periodo)
        return self.capital_inicial