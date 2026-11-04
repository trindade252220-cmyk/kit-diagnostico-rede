# Kit de diagnóstico de rede

## O que é
Um programa em Python que calcula, a partir da máscara CIDR informada, o total de endereços da rede, o salto e a quantidade de hosts utilizáveis. Ele é o primeiro passo de um kit de diagnóstico que estou construindo nos meus estudos de redes.

## Como usar
Execute o programa e digite apenas o número do CIDR, sem a barra (por exemplo, 27). O programa subtrai esse valor de 32, que é a quantidade de bits de um endereço IPv4, e o resultado é a quantidade de bits de host. Em seguida, calcula 2 elevado a essa quantidade, o que dá o total de endereços e o salto. Por fim, subtrai 2 do total, porque o primeiro endereço é o da rede e o último é o de broadcast, e o resultado são os hosts utilizáveis.

Exemplo: CIDR 27 → Total: 32 / Salto: 32 / Hosts utilizáveis: 30

## O que aprendi
Descobri na prática que o Python resolve a potência antes da subtração. Também percebi que a primeira versão do programa mostrava só o total e esquecia de descontar os endereços de rede e de broadcast.

## Limitações
- Para os CIDRs /31 e /32 o resultado não vale (o cálculo dá 0 e -1), e precisaria de um if para tratar esses casos.
- O programa não valida a entrada: se for digitada uma letra ou uma barra (como /27), ele para com erro.
- O salto só tem esse significado para as máscaras de /24 a /30; para as outras, o valor mostrado é apenas o total de endereços.
- O programa não calcula o endereço de rede nem o de broadcast, apenas as quantidades.
