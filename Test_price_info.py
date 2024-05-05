import price_info as PR

def test_total_cost_of_shopping():
    total_cost = PR.total_cost_shopping()
    assert total_cost == 46.75

def test_cost_of_fruits():
    cost_of_apple = PR.cost_of_fruits('apple', 10)
    assert cost_of_apple == 12.0