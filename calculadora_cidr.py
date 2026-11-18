import sys

cidr = int(input('Digite o CIDR: '))
if cidr < 0 or cidr > 32:
    sys.exit('ERRO: O valor precisa ser entre 0 e 32!')
    
elif cidr == 32:
    sys.exit('CIDR com 1 endereço de IP utiliável para Host')
    
elif cidr == 31:
    sys.exit('CIDR com 2 endereços de IP utilizáveis, usado em conexões (ponto a potno) ')
ip = int(input('Digite o último octeto:'))
if ip < 0 or ip > 255:
    sys.exit('ERRO: O valor precisa estar entre 0 e 255!')
    
host = 32 - cidr
salto = 2 ** host
disponiveis = salto - 2
rede = (ip//salto) * salto
broadcast = rede + salto - 1
primeiro = rede + 1 
ultimo = broadcast - 1


print(f'Salto: {salto} // Disponiveis: {disponiveis} // Rede: {rede} // Broadcast: {broadcast} // Primeiro endereço: {primeiro} // Ultimo ednereço: {ultimo}')
