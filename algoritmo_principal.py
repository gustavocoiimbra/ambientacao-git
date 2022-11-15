def ordenacao_selecao(A):
  cont = 0

  for i in range(len(A)):
    minimo = i

    for j in range(i + 1, len(A)):
      if A[minimo] > A[j]:
        minimo = j

        A[i], A[minimo] = A[minimo], A[i]
