import unittest
from unittest.mock import patch
import pokemon

class TestCatch(unittest.TestCase):

    @patch('pokemon.get_input', return_value='E')
    def test_ex_1(self, input_mock):
        self.assertEqual(pokemon.catch_pokemons(), 2)
    
    @patch('pokemon.get_input', return_value='NESO')
    def test_ex_2(self, input_mock):
        self.assertEqual(pokemon.catch_pokemons(), 4)
    
    @patch('pokemon.get_input', return_value='NSNSNSNSNS')
    def test_ex_3(self, input_mock):
        self.assertEqual(pokemon.catch_pokemons(), 2)
    
    @patch('pokemon.get_input', return_value='NNNNNNNNNNN')
    def test_11_north(self, input_mock):
        self.assertEqual(pokemon.catch_pokemons(), 12)
    
    @patch('pokemon.get_input', return_value='')
    def test_no_movement(self, input_mock):
        self.assertEqual(pokemon.catch_pokemons(), 1)
    
    @patch('pokemon.get_input', return_value='OOOONNNNEEEESSSS')
    def test_4_4_square_movement(self, input_mock):
        self.assertEqual(pokemon.catch_pokemons(), 16)


if __name__ == '__main__':
    unittest.main()
