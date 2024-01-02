def soma_matrizes(m1, m2):
    l1 = len(m1)
    c1 = len(m1[0])
    l2 = len(m2)
    c2 = len(m2[0])
    soma_matriz = []

    if (l1 == l2) and (c1 == c2):
        for i in range(l1):
            linha_matriz = []
            for j in range(c1):
                linha_matriz.append(m1[i][j] + m2[i][j])
            soma_matriz.append(linha_matriz)
    else:
        return False
    return soma_matriz
