from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1, 'qualquer produto', 'tests S.A',
        '20-02-2002', '20-06-2002', 666, 'seco',
    )

    assert product == \
           "O produto qualquer produto fabricado em 20-02-2002 por tests S.A\
            com validade até 20-06-2002 precisa ser armazenado seco."
    pass  # Seu teste deve ser escrito aqui
