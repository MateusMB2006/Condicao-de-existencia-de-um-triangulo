print('\033[34m-_\033[m' * 20)
print('\033[36mCondição de existência de um triângulo\033[m')
print('\033[34m-_\033[m' * 20)
p = float(input('Primeira reta: '))
s = float(input('Segunda reta: '))
t = float(input('Terceira reta: '))
retas = [p, s, t]
retas.sort()
if retas[0] + retas[1] >= retas[2] :
    print('Com essas três retas é \033[32m>POSSIVÉL<\033[m fazer um \033[36mtriângulo\033[m')
else :
    print('Com essas três retas \033[31m>NÃO É POSSIVÉL<\033[m fazer um \033[36mtriângulos\033[m')