from modelos.roupa import Roupas

roupa_jaqueta = Roupas('Jaqueta', 'Casual', 'M', 'Morumbi')
roupa_camisa = Roupas('Camisa', 'Social', 'G', 'Vila A')
roupa_calca = Roupas('Calça', 'Jeans', '42', 'Centro')

roupa_jaqueta.alterar_estado()
roupa_calca.receber_preço('Loja Vila', 230)
roupa_calca.receber_preço('Loja Vida', 220)
roupa_calca.receber_preço('São João Moda', 240)

def main():
    Roupas.listar_roupas()

if __name__ == '__main__':
    main()
