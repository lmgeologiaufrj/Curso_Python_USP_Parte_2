def primeiro_lex(lista):
    primeiro_lex = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < primeiro_lex:
            primeiro_lex = lista[i]
    return primeiro_lex
