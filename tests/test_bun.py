from praktikum.bun import Bun
import pytest

class TestBun:

    @pytest.mark.parametrize('name', 
            ['Булочка с кунжутом', 
             'Ржаная', 
             'Солёная-солёная'])
    def test_bun_get_name(self, name):
        bun = Bun(name, 9.99)
        
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [11.99, 0.99, 11])
    def test_bun_get_price(self, price):
        bun = Bun('name', price)
        
        assert bun.get_price() == price

        