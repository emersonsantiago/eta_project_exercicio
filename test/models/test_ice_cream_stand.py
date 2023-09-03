import unittest
from io import StringIO

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand(unittest.TestCase):
    def test_flavors_available(self):
        # Setup
        restaurant_name = "Tio Beto Sorvetes"
        cuisine_type = "Sorvetes Naturais"
        flavors_list = ["Milho verde", "Chocolate", "Morango ao leite"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
        expected_result = "No momento temos os seguintes sabores de sorvete disponíveis: Milho verde, Chocolate, Morango ao leite"

        # Chamada
        result = ice_cream_stand.flavors_available()


        # Validação
        assert expected_result == result

    def test_find_flavor(self):
        # Setup
        restaurant_name = "Tio Beto Sorvetes"
        cuisine_type = "Sorvetes Naturais"
        flavors_list = ["Milho verde", "Chocolate", "Morango ao leite"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
        expected_result = "Temos no momento Chocolate"

        # Chamada
        result = ice_cream_stand.find_flavor("Chocolate")

        # Validação
        assert expected_result == result

    def test_add_flavor(self):
        # Setup
        restaurant_name = "Tio Beto Sorvetes"
        cuisine_type = "Sorvetes Naturais"
        flavors_list = ["Milho verde", "Chocolate", "Morango ao leite"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
        expected_result = f"Baunilha adicionado ao estoque!"

        # Chamada
        result = ice_cream_stand.add_flavor("Baunilha")

        # Validação
        assert expected_result == result