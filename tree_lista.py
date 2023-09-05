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
