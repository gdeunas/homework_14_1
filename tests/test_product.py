def test_product_init(product):
    """test product class"""
    assert product.name == "product_n"
    assert product.description == "product_dec"
    assert product.price == 12.2
    assert product.quantity == 10
