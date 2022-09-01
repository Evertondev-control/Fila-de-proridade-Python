#Fila De Prioridade(Ordem de prioridade: Gestante , Maior idade , Nome)
import heapq

fila =[]
filagestante=[]

class FilaDePrioridade:
	def __init__(self):
		self._fila = []

	def inserir(self, item):
		prioridade = -int(str(item.gestante) + str(item.idade))
		heapq.heappush(self._fila, (prioridade, item.nome))
	
	def ordenaFila(self):
		h = []
		for value in self._fila:
			heapq.heappush(h, value)
		return [heapq.heappop(h) for i in range(len(h))]

class Pessoa:
	def __init__(self, nome, gestante, idade):
		self.nome = nome
		self.gestante = gestante
		self.idade = idade

	def __repr__(self):
		return self.nome + " que tem " + str(self.idade) + " anos"


fila = FilaDePrioridade()
nome= "a"
idade= 1

while len(nome) !=0 and idade != 0:
	nome=str(input("Nome: "))
	idade=int(input("Idade: "))
	gestante = int(input("\nÉ gestante?\nS = 1 \nN = 0\n"))
	if idade != 0:
		fila.inserir(Pessoa(nome ,gestante,idade))	
	
print(fila.ordenaFila())