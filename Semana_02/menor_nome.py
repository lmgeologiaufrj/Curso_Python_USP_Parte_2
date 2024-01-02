def menor_nome(nomes):
    menor_nome = nomes[0].strip()
    for i in range(1, len(nomes)):
        strip = nomes[i].strip()
        if len(strip) < len(menor_nome):
            menor_nome = strip
    menor_nome = menor_nome.capitalize()
    return menor_nome
