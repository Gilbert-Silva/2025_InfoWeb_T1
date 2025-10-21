def nome_mes(m):
    match m: 
        case 1: return "Janeiro"
        case 2: return "Fevereiro"
        case 12: return "Dezembro"
        case _: raise ValueError("Número do mês inválido")



