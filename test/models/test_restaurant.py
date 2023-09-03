import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):

    def test_describe_restaurant(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        expected_output = f"Esse restaurante se chama {restaurant_name} and serve {cuisine_type}.\nEsse restaurante serviu 0 consumidores desde que abriu."

        # Chamada
        with unittest.mock.patch('sys.stdout', new_callable=unittest.mock.StringIO) as mock_stdout:
            restaurant.describe_restaurant()
            result = mock_stdout.getvalue().strip()

        # Validação
        self.assertEqual(result, expected_output)

    def test_open_restaurant(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        restaurant.open_restaurant()

        # Validação
        self.assertTrue(restaurant.open)

    def test_close_restaurant(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        restaurant.close_restaurant()

        # Validação
        self.assertFalse(restaurant.open)

    def test_set_number_served(self):
        # Setup
        restaurant_name = "Tio Beto Restaurante"
        cuisine_type = "Comida Brasileira"
        restaurant = Restaurant(restaurant_name, cuisine_type)
        total_customers = 10

        # Chamada
        restaurant.set_number_served(total_customers)

        # Validação
        self.assertEqual(restaurant.number_served, total_customers)

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
        self.assertEqual(restaurant.number_served, expected_customers)

