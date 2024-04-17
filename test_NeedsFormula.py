import unittest
from NeedsFormula import NutritionalNeeds


class TestNutritionalNeeds(unittest.TestCase):

    def setUp(self):
        self.person1 = NutritionalNeeds(
            80, 180, 30, "male", "moderate", False, False, "maintain"
        )
        self.person2 = NutritionalNeeds(
            60, 165, 25, "female", "active", False, False, "lose"
        )
        self.person3 = NutritionalNeeds(
            75, 175, 35, "male", "sedentary", False, False, "gain"
        )
        self.pregnant_woman = NutritionalNeeds(
            70, 170, 28, "female", "sedentary", True, False, "maintain"
        )
        self.lactating_woman = NutritionalNeeds(
            65, 168, 32, "female", "sedentary", False, True, "maintain"
        )

    def test_calculate_bmr(self):
        self.assertAlmostEqual(self.person1.calculate_bmr(), 1780)
        self.assertAlmostEqual(self.person2.calculate_bmr(), 1345.25)
        self.assertAlmostEqual(self.person3.calculate_bmr(), 1673.75)
        self.assertAlmostEqual(self.pregnant_woman.calculate_bmr(), 1461.5)
        self.assertAlmostEqual(self.lactating_woman.calculate_bmr(), 1379)

    def test_calculate_daily_calories(self):
        self.assertAlmostEqual(self.person1.calculate_daily_calories(), 2530.94)
        self.assertAlmostEqual(self.person2.calculate_daily_calories(), 2421.45)
        self.assertAlmostEqual(self.person3.calculate_daily_calories(), 2108.92)
        self.assertAlmostEqual(self.pregnant_woman.calculate_daily_calories(), 1534.58)
        self.assertAlmostEqual(self.lactating_woman.calculate_daily_calories(), 1447.95)

    def test_calculate_macros_needs(self):
        self.assertIn("Protein: 189.82 g", self.person1.calculate_macros_needs())
        self.assertIn("Fat: 84.36 g", self.person1.calculate_macros_needs())
        self.assertIn("Carbohydrates: 253.09 g", self.person1.calculate_macros_needs())

        self.assertIn("Protein: 242.14 g", self.person2.calculate_macros_needs())
        self.assertIn("Fat: 80.71 g", self.person2.calculate_macros_needs())
        self.assertIn("Carbohydrates: 181.61 g", self.person2.calculate_macros_needs())

        self.assertIn("Protein: 158.17 g", self.person3.calculate_macros_needs())
        self.assertIn("Fat: 46.86 g", self.person3.calculate_macros_needs())
        self.assertIn("Carbohydrates: 263.62 g", self.person3.calculate_macros_needs())

        self.assertIn("Protein: 140.09 g", self.pregnant_woman.calculate_macros_needs())
        self.assertIn("Fat: 51.15 g", self.pregnant_woman.calculate_macros_needs())
        self.assertIn("Carbohydrates: 153.46 g", self.pregnant_woman.calculate_macros_needs())

        self.assertIn(
            "Protein: 128.60 g", self.lactating_woman.calculate_macros_needs()
        )
        self.assertIn("Fat: 48.27 g", self.lactating_woman.calculate_macros_needs())
        self.assertIn(
            "Carbohydrates: 144.80 g", self.lactating_woman.calculate_macros_needs()
        )


if __name__ == "__main__":
    unittest.main()
