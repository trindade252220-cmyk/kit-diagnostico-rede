cidr = int(input ('Digite o CIDR:'))

if cidr < 0 or cidr > 32:
    print('ERRO: O CIDR deve estar entre 0 e 32')

elif cidr == 32:
    print ('Rede Host Único (/32): 1 IP utilizável.')

elif cidr == 31:
    print('Rede Ponto a Ponto (/31): 2 IPs utilizáveis (RFC 3021).')

else:
    Bits_Host = 32 -cidr
    Totais = 2 **  Bits_Host
    Uteis = Totais - 2
    Salto = Totais
    print(f'Bits Totais: {Totais} // Salto: {Salto}  // Utilizáveis: {Uteis}')
