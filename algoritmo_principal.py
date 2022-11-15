import random

def ordenacao_selecao(A):
  cont = 0

  for i in range(len(A)):
    # Encontra o elemento mínimo em A
    minimo = i

    for j in range(i + 1, len(A)):
      if A[minimo] > A[j]:
        minimo = j

    # Coloca o elemento mínimo na posição correta
    A[i], A[minimo] = A[minimo], A[i]

A = random.sample(range(-10, 10), 10)

print("Arranjo não ordenado", A)

ordenacao_selecao(A)

print("Arranjo ordenado", A)
