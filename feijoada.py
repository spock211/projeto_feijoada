   def volumeFeijoada():
    global vol2
    ru = 1392625
    while True:
        try:
            print('Bem-Vindo ao Programa de Feijoada do Alexandre Rangel de Oliveira, RU:', ru)
            print('Menu Volume Feijoada\n')
            vol = int(input('Entre com a quantidade que deseja(ml):'))
            if vol < 300 or vol > 5000:
                print('Não aceitamos porções abaixo de 300ml ou acima de 5l')
                continue
            elif vol >= 300 and vol <= 5000:
                vol2 = vol * 0.08
                break
        except ValueError:
            print('Foi inserido um caracter não numérico.')
            continue

def opcaoFeijoada():
    global total
    global valorOpc
    while True:
        print('Menu Opção Feijoada\n')
        print('Entre com a opção de Feijoada:\n')
        print('b - Básica  (Feijão + paiol + costelinha')
        print('p - Premium (Feijão + paiol + costelinha + partes de porco')
        print('s - Suprema (Feijão + paiol + costelinha + partes de porco')
        opc1 = input('Digite a opção: ')
        if opc1 == 'b':
            total = vol2 * 1
            valorOpc = 1.00
            break
        elif opc1 == 'p':
            total = vol2 * 1.25
            valorOpc = 1.25
            break
        elif opc1 == 's':
            total = vol2 * 1.50
            valorOpc = 1.50
            break
        elif opc1 != 'b' or opc1 != 'p' or opc1 != 's':
            print('Você não digitou uma opção válida!')
            continue

def acompanhamentoFeijoada():
    global side_dish
    global valorAcomp
    while True:
        print('Deseja mais algum acompanhamento?')
        print('0 - Não desejo mais acompanhamentos (encerrar pedido)')
        print('1 - 200g de arroz')
        print('2 - 150g de farofa especial')
        print('3 - 100g de couve cozida')
        print('4 - Uma laranja descascada\n')
        try:
            acomp1 = int(input('Escolha o acompanhamento: '))
            if acomp1 == 0:
                break
            elif acomp1 == 1:
                valorAcomp = 5.00
                side_dish = side_dish + valorAcomp
                continue
            elif acomp1 == 2:
                valorAcomp = 6.00
                side_dish = side_dish + valorAcomp
                continue
            elif acomp1 == 3:
                valorAcomp = 7.00
                side_dish = side_dish + valorAcomp
                continue
            elif acomp1 == 4:
   
                continue
                valorAcomp = 3.00
                side_dish = side_dish + valorAcomp
            else:
                acomp1 != 0 or acomp1 != 1 or acomp1 != 2 or acomp1 != 3 or acomp1 != 4
                print('Opção Inválida')
        except ValueError:
            print('Foi inserido um caracter não numérico.')
            continue

# Programa Principal



side_dish = 0
valorOpc = 0
valorAcomp = 0

volumeFeijoada()
opcaoFeijoada()
acompanhamentoFeijoada()
print('O valor a ser pago é (R$){:.2f}'.format(total+side_dish),'( Volume = {:.2f}'.format(vol2),'* Opção = {:.2f}'.format(valorOpc),'+ acompanhamento = {:.2f}'.format(side_dish),')')
        
    
            
    




