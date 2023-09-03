import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):

    def test_describe_restaurant(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_result = f"Esse restaurante se chama {restaurant_name} e serve {cuisine_type}.\nEsse restaurante serviu 0 consumidores desde que abriu."

        # Chamada
        result = restaurant.describe_restaurant()

        # Validação
        assert expected_result == result

    def test_open_restaurant(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_result = "Tio Beto Restaurante agora está aberto!"

        # Chamada
        result = restaurant.open_restaurant(True)

        # Validação
        assert expected_result == result

    def test_close_restaurant(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_result = "Tio Beto Restaurante agora está fechado!"
        # Chamada
        result = restaurant.close_restaurant(False)

        # Validação
        assert expected_result == result

    def test_set_number_served(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        number_served = 10

        # Chamada
        result = restaurant.set_number_served(10)

        # Validação
        assert number_served == result

    def test_increment_number_served(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        initial_customers = 5
        increment_customers = 3
        expected_customers = initial_customers + increment_customers

        # Chamada
        restaurant.number_served = initial_customers
        restaurant.increment_number_served(increment_customers)

        # Validação
        assert restaurant.number_served == expected_customers

