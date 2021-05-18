class JurosSimples():

    def __init__(self, capital_inicial, taxa, periodo, juros, montante):
        self.capital_inicial = capital_inicial
        self.taxa = taxa / 100
        self.periodo = periodo
        self.juros = juros
        self.montante = montante
        
    def calculo_juros(self):
        self.juros = self.capital_inicial * self.taxa * self.periodo
        return self.juros

    def calculo_capital_inicial(self):
        self.capital_inicial = self.juros / ( self.taxa * self.periodo )
        return self.capital_inicial

    def calculo_taxa(self):
        self.taxa = (self.juros / ( self.capital_inicial * self.periodo )) * 100
        return self.taxa

    def calculo_periodo(self):
         self.periodo = self.juros / ( self.capital_inicial * self.taxa )
         return self.periodo

    def calculo_montante(self):
         self.montante = self.capital_inicial + (self.capital_inicial * self.taxa * self.periodo)
         return self.montante



opcao = input(print('''
Juros (mensal): J
Capital Inicial: C
Taxa (mensal): T
Período (meses): P
Montante: M
Escolha uma opção:
'''))

if opcao == 'J':
    c = float(input('Digite o capital inicial: '))
    t = float(input('Digite a taxa de juros (mensal): '))
    p = int(input('Digite o período (meses): '))
    j = 0
    m = 0

    c1 = JurosSimples(c, t, p, j, m)
    c1.calculo_juros()
    print(c1.juros)


elif opcao == 'C':
    j = float(input('Digite o juros mensal esperado: '))
    t = float(input('Digite o taxa de juros (mensal): '))
    p = int(input('Digite o período (meses): '))
    c = 0
    m = 0

    c1 = JurosSimples(c, t, p, j, m)
    c1.calculo_capital_inicial()
    print(c1.capital_inicial)

elif opcao == 'T':
    j = float(input('Digite o juros mensal esperado: '))
    c = float(input('Digite o capital inicial: '))
    p = int(input('Digite o período (meses): '))
    t = 0
    m = 0

    c1 = JurosSimples(c, t, p, j, m)
    c1.calculo_taxa()
    print(c1.taxa)

elif opcao == 'P':
    j = float(input('Digite o juros mensal esperado: '))
    c = float(input('Digite o capital inicial: '))
    t = float(input('Digite o taxa de juros (mensal): '))
    p = 0
    m = 0

    c1 = JurosSimples(c, t, p, j, m)
    c1.calculo_periodo()
    print(c1.periodo)

else:
    c = float(input('Digite o capital inicial: '))
    t = float(input('Digite a taxa de juros (mensal): '))
    p = int(input('Digite o período (meses): '))
    j = 0
    m = 0

    c1 = JurosSimples(c, t, p, j, m)
    c1.calculo_montante()
    print(c1.montante)