import unittest
from NeedsFormula import NutritionalNeeds


class TestNutritionalNeeds(unittest.TestCase):
    def setUp(self):
        # Example setup for a moderate active male aiming to maintain weight
        self.male_user = NutritionalNeeds(
            weight=70,
            height=175,
            age=25,
            gender="male",
            activity_level="moderate",
            is_pregnant=False,
            is_lactating=False,
            goal="maintain",
        )
        # Example setup for a moderately active female aiming to lose weight, not pregnant or lactating
        self.female_user = NutritionalNeeds(
            weight=60,
            height=165,
            age=30,
            gender="female",
            activity_level="moderate",
            is_pregnant=False,
            is_lactating=False,
            goal="lose",
        )

    def test_calculate_bmr(self):
        # Testing BMR calculation
        self.assertAlmostEqual(self.male_user.calculate_bmr(), 1673.75, places=2)
        self.assertAlmostEqual(self.female_user.calculate_bmr(), 1320.25, places=2)

    def test_calculate_daily_calories(self):
        # Testing daily calories calculation
        # Note: The exact numbers depend on the implementation details of calculate_daily_calories method
        self.assertTrue(
            self.male_user.calculate_daily_calories() > self.male_user.calculate_bmr()
        )
        self.assertTrue(
            self.female_user.calculate_daily_calories()
            < self.female_user.calculate_bmr() * 1.2
        )  # considering weight loss goal

    def test_calculate_amino_acid_needs(self):
        # Testing the amino acid needs string format and checking if it's not empty
        self.assertTrue(isinstance(self.male_user.calculate_amino_acid_needs(), str))
        self.assertTrue(len(self.male_user.calculate_amino_acid_needs()) > 0)

        self.assertTrue(isinstance(self.female_user.calculate_amino_acid_needs(), str))
        self.assertTrue(len(self.female_user.calculate_amino_acid_needs()) > 0)

    def test_calculate_macros_needs(self):
        # Testing the macronutrient needs string format and checking if it's not empty
        self.assertTrue(isinstance(self.male_user.calculate_macros_needs(), str))
        self.assertTrue(len(self.male_user.calculate_macros_needs()) > 0)

        self.assertTrue(isinstance(self.female_user.calculate_macros_needs(), str))
        self.assertTrue(len(self.female_user.calculate_macros_needs()) > 0)


if __name__ == "__main__":
    unittest.main()
