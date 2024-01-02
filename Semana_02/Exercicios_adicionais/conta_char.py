def conta_letras(frase, contar="vogais"):
    total_vogais = 0
    total_consoantes = 0
    frase = frase.lower()
    for i in range(len(frase)):
        if (
            frase[i] == "a"
            or frase[i] == "e"
            or frase[i] == "i"
            or frase[i] == "o"
            or frase[i] == "u"
        ):
            total_vogais += 1
        elif ord(frase[i]) >= 97 and ord(frase[i]) <= 122:
            total_consoantes += 1
    if contar == "vogais":
        return total_vogais
    else:
        return total_consoantes
