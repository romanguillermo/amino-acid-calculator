import unittest
from NeedsFormula import NutritionalNeeds

class TestNeedsFormula(unittest.TestCase):
    def setUp(self):
        self.nutritional_needs = NutritionalNeeds(weight=70, height=170, age=30, gender='male', activity_level='moderate', is_pregnant=False, is_lactating=False, goal='maintain')

    def test_calculate_bmr(self):
        self.assertEqual(self.nutritional_needs.calculate_bmr(), 1666.5)

    def test_calculate_daily_calories(self):
        self.assertEqual(self.nutritional_needs.calculate_daily_calories(), 2166.5)

    def test_calculate_protein_needs(self):
        self.assertEqual(self.nutritional_needs.calculate_protein_needs(), 70)

    def test_calculate_amino_acid_needs(self):
        self.assertEqual(self.nutritional_needs.calculate_amino_acid_needs(), {'leucine': 2.5, 'isoleucine': 1.5, 'valine': 1.8})

    def test_calculate_macros_needs(self):
        self.assertEqual(self.nutritional_needs.calculate_macros_needs(), {'carbohydrates': 270, 'fat': 60, 'protein': 70})


if __name__ == "__main__":
    unittest.main()
