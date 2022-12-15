from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1, 'qualquer produto', 'tests S.A',
        '20-02-2002', '20-06-2002', 666, 'seco',
    )

    assert product.id == 1
    assert product.nome_do_produto == 'qualquer produto'
    assert product.nome_da_empresa == 'tests S.A'
    assert product.data_de_fabricacao == '20-02-2002'
    assert product.data_de_validade == '20-06-2002'
    assert product.numero_de_serie == 666
    assert product.instrucoes_de_armazenamento == 'seco'
