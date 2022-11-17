def ordenacao_selecao(A):
      n = len(A)

      for i in range(n):
        minimo = i

        for j in range(i + 1, n):
          if A[minimo] > A[j]:
            minimo = j

      A[i], A[minimo] = A[minimo], A[i]
