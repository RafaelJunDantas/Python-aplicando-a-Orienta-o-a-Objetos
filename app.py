import os
from modelos.restaurante import Restaurante

restaurante1 = Restaurante('pizza', 'pizza')
restaurante2 = Restaurante('sushi', 'sushi')

restaurante1.adicionar_avaliacao('a', 5)
restaurante1.adicionar_avaliacao('b', 10)
restaurante1.adicionar_avaliacao('c', 6)

restaurante1.alternar_estado()

def main():
    os.system('clear')

    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()