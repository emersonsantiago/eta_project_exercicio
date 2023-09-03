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
        expected_result = "No momento temos os seguintes sabores de sorvete disponíveis:"

        # Chamada
        with StringIO() as out, unittest.mock.patch('sys.stdout', out):
            ice_cream_stand.flavors_available()
            result = out.getvalue().strip()

        # Validação
        self.assertIn(expected_result, result)

    def test_find_flavor(self):
        # Setup
        restaurant_name = "Tio Beto Sorvetes"
        cuisine_type = "Sorvetes Naturais"
        flavors_list = ["Milho verde", "Chocolate", "Morango ao leite"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
        flavor_to_find = "Chocolate"
        expected_result = f"Temos no momento {flavor_to_find}!"

        # Chamada
        with StringIO() as out, unittest.mock.patch('sys.stdout', out):
            ice_cream_stand.find_flavor(flavor_to_find)
            result = out.getvalue().strip()

        # Validação
        self.assertIn(expected_result, result)

    def test_add_flavor(self):
        # Setup
        restaurant_name = "Tio Beto Sorvetes"
        cuisine_type = "Sorvetes Naturais"
        flavors_list = ["Milho verde", "Chocolate", "Morango ao leite"]
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
        flavor_to_add = "Baunilha"
        expected_result = f"{flavor_to_add} adicionado ao estoque!"

        # Chamada
        with StringIO() as out, unittest.mock.patch('sys.stdout', out):
            ice_cream_stand.add_flavor(flavor_to_add)
            result = out.getvalue().strip()

        # Validação
        self.assertIn(expected_result, result)