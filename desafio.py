#EXPERIMENTAÇÃO

LIMITE_SAQUES = 3
SAQUE_MAXIMO = 500

#start class ContaBanco
class ContaBanco:

    def __init__(self):
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0

	
    def depositar(self):
        valor = float(input("Informe o valor do depósito:\t"))
	    
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depóstivo: R$ {valor:.2f}\n"
        else:
            print("Operação inválida! O valor informado precisa ser maior que R$ 0,00.")
	
    def sacar(self):
        valor = float(input("Informe o valor do saque:\t"))
        global LIMITE_SAQUES
        global SAQUE_MAXIMO
		
        if self.saldo < valor:
            print("Operação inválida! Saldo insuficiente.")
        elif valor > SAQUE_MAXIMO:
            print("Operação inválida! Valor máximo para saque é de R$500,00.")
        elif self.numero_saques >= LIMITE_SAQUES:
            print("Operação inválida! Limite de saques diários atingido.")
		
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
		    
        else:
            print("Operação inválida! O valor informado precisa ser maior que R$ 0,00.")
		
		
    def emitir_extrato(self):
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("=============================")
	
def mensagem_erro():
	print("Operação inválida! Por favor certifique-se de que esteja selecionando a operação desejada e tente de novo.")
#end class ContaBanco

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>\t"""

conta_banco = ContaBanco()

DEFAULT = float('inf')
switch_para_loop = {
		"d" : conta_banco.depositar,
		"s" : conta_banco.sacar,
		"e" : conta_banco.emitir_extrato,
		"q" : None,	
}
#o normal seria usar if else elif no loop, ou o match do Python 3.10
#mas isto também funciona

while True:
	opcao = input(menu)
	executar = switch_para_loop.get(opcao, mensagem_erro)
	if executar:
	    executar()
	else:
	    print("Saindo...")
	    break
		
	
	
