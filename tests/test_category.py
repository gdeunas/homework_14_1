def test_category_init(first_category, second_category):
    assert first_category.name == "category_n"
    assert first_category.description == "category_dec"
    assert len(first_category.products) == 2
    assert len(second_category.products) == 1

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.all_products_count == 3

