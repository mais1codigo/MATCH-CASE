print('''
      1 serviço A
      2 serviço B
      3 serviço C
      informe sua opção''')


opção = input('insira um valor pra escolher')

match opção:
    case '1':
        print('vc optou pela 1')
    
    case '2':
        print('vc optou pela 2')

    case '3':
        print('vc optou pela 3')
    
    case outro:
        print('esse case {outro} não existe')