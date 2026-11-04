# Calculadora de hosts por CIDR (estudos)
# Limitação: para /31 e /32 o resultado não vale (precisa de um if)

cidr = int(input('Digite o CIDR: '))
bits_host = 32 - cidr
total = 2 ** bits_host
uteis = total - 2

print('Total: {} / Salto: {} / Hosts utilizáveis: {}'.format(total, total, uteis))
