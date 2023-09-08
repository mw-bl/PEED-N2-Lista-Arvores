# Marcos Willian :D

# Q1 / Q2
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.inserir_em_nivel_recursivo(valor, self.raiz)

    def inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.direita)

# Q3
    def verificar_valor(self, valor):
        return self._verificar_valor(self.raiz, valor)

    def _verificar_valor(self, no, valor):
        if no is None:
            return False
        if no.valor == valor:
            return True
        return (
            self._verificar_valor(no.esquerda, valor) or
            self._verificar_valor(no.direita, valor)
        )

# Q4
    def calcular_altura(self):
        return self._calcular_altura(self.raiz)

    def _calcular_altura(self, no):
        if no is None:
            return 0
        altura_esquerda = self._calcular_altura(no.esquerda)
        altura_direita = self._calcular_altura(no.direita)
        return max(altura_esquerda, altura_direita) + 1

# Q5
    def inordem(self):
        return self._inordem(self.raiz)

    def _inordem(self, no):
        if no is None:
            return []
        resultado = []
        resultado += self._inordem(no.esquerda)
        resultado.append(no.valor)
        resultado += self._inordem(no.direita)
        return resultado

# Q6
    def preordem(self):
        return self._preordem(self.raiz)

    def _preordem(self, no):
        if no is None:
            return []
        resultado = []
        resultado.append(no.valor)
        resultado += self._preordem(no.esquerda)
        resultado += self._preordem(no.direita)
        return resultado

# Q7
    def posordem(self):
        return self._posordem(self.raiz)

    def _posordem(self, no):
        if no is None:
            return []
        resultado = []
        resultado += self._posordem(no.esquerda)
        resultado += self._posordem(no.direita)
        resultado.append(no.valor)
        return resultado

# Q8
    def em_niveis(self):
        altura = self.calcular_altura()
        resultado = []
        for nivel in range(1, altura + 1):
            self._em_niveis(self.raiz, nivel, resultado)
        return resultado

    def _em_niveis(self, no, nivel, resultado):
        if no is None:
            return
        if nivel == 1:
            resultado.append(no.valor)
        elif nivel > 1:
            self._em_niveis(no.esquerda, nivel - 1, resultado)
            self._em_niveis(no.direita, nivel - 1, resultado)

# Q9
    def contar_nos(self):
        return self._contar_nos(self.raiz)

    def _contar_nos(self, no):
        if no is None:
            return 0

        return 1 + self._contar_nos(no.esquerda) + self._contar_nos(no.direita)

# Q10
    def encontrar_valor_maximo(self):
        if self.raiz is None:
            return None
        return self._encontrar_valor_maximo(self.raiz)

    def _encontrar_valor_maximo(self, no):
        while no.direita is not None:
            no = no.direita
        return no.valor

# Q11  
    def verificar_arvore_de_busca(self):
        return self._verificar_arvore_de_busca(self.raiz, None, None)

    def _verificar_arvore_de_busca(self, no, limite_min, limite_max):
        if no is None:
            return True

        if (limite_min is not None and no.valor <= limite_min) or (limite_max is not None and no.valor >= limite_max):
            return False

        return (
            self._verificar_arvore_de_busca(no.esquerda, limite_min, no.valor) and
            self._verificar_arvore_de_busca(no.direita, no.valor, limite_max)
        )

# Q13
    def nos_no_nivel(self, nivel_desejado):
        return self._nos_no_nivel(self.raiz, 1, nivel_desejado)

    def _nos_no_nivel(self, no, nivel_atual, nivel_desejado, resultado=[]):
        if no is None:
            return []

        if nivel_atual == nivel_desejado:
            resultado.append(no.valor)

        if nivel_atual < nivel_desejado:
            self._nos_no_nivel(no.esquerda, nivel_atual + 1, nivel_desejado, resultado)
            self._nos_no_nivel(no.direita, nivel_atual + 1, nivel_desejado, resultado)

        return resultado

# Q14
    def caminho_ate_no(self, valor):
        return self._caminho_ate_no(self.raiz, valor)

    def _caminho_ate_no(self, no, valor, caminho_atual=[]):
        if no is None:
            return []

        caminho_atual.append(no.valor)

        if no.valor == valor:
            return caminho_atual.copy()

        caminho_esquerda = self._caminho_ate_no(no.esquerda, valor, caminho_atual.copy())
        caminho_direita = self._caminho_ate_no(no.direita, valor, caminho_atual.copy())

        if not caminho_esquerda and not caminho_direita:
            return []

        return caminho_esquerda if caminho_esquerda else caminho_direita
        
# Testes das Questões
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

busca_valor = 4
if arvore.verificar_valor(busca_valor):
    print(f"O número {busca_valor} está presente na árvore.")
else:
    print(f"O número {busca_valor} não está presente na árvore.")

altura = arvore.calcular_altura()
print(f"Altura da árvore: {altura}")

inordem = arvore.inordem()
print("\nPercorrer In-ordem:", inordem)

preordem = arvore.preordem()
print("Percorrer Pré-ordem:", preordem)

posordem = arvore.posordem()
print("Percorrer Pós-ordem:", posordem)

em_niveis = arvore.em_niveis()
print("Percorrer em Níveis:", em_niveis)

total_nos = arvore.contar_nos()
print("\nNúmero total de nós na árvore:", total_nos)

maximo = arvore.encontrar_valor_maximo()
print("Valor máximo na árvore:", maximo)

eh_valida = arvore.verificar_arvore_de_busca()
if eh_valida:
    print("A árvore é uma árvore de busca válida.")
else:
    print("A árvore não é uma árvore de busca válida.")

nivel_desejado = 2
nos_nivel = arvore.nos_no_nivel(nivel_desejado)
print(f"Nós no nível {nivel_desejado}: {nos_nivel}")

no_alvo = 4
caminho = arvore.caminho_ate_no(no_alvo)
if caminho:
    print(f"Caminho até o nó {no_alvo}: {caminho}")
else:
    print(f"Nó {no_alvo} não encontrado na árvore.")
