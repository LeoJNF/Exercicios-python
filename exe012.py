from time import sleep
print('\033[7m-' * 5, 'Bem-vindo a calculadora de tinta', '-----\033[m')
sleep(1.5)
print('Para calcular o quanto de tinta você vai precisar. Precisamos da:')
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('\033[34mPROCESSANDO...\033[m')
sleep(2)
print('\033[33mSua parede tem a dimensão de {:.1f}x{} e sua area é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta\033[m'.format(tinta))
