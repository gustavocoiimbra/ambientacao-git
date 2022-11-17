import random

def ordenacao_selecao(A):
      n = len(A)
      
      for i in range(n):
        minimo = i

        for j in range(i + 1, n):
          if A[minimo] > A[j]:
            minimo = j

      A[i], A[minimo] = A[minimo], A[i]

A = random.sample(range(-10, 10), 10)

print("Arranjo desordenado:", A)

ordenacao_selecao(A)

print("Arranjo ordenado:", A)