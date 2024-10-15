
print(f'''
    comandos:
      ''')

Ação = input('insira um comando ')

match Ação.split():

    case ["sair"]:
        print(f' xau xau')
    
    case ["usar", item]:
        print(f'vc vai usar {item}')

    case ["atacar", inimigo, arma]:
        print(f'vc vai atacar {inimigo} com uma {arma}')  
    
    case _:
        print(f'ação incorreta')
