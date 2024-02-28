class BMRCalculator:
    @staticmethod
    def calculate_bmr(weight, height, age, gender):
        """Calculates the Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation."""
        if gender.lower() == "male":
            return 10 * weight + 6.25 * height - 5 * age + 5
        else:  # Female
            return 10 * weight + 6.25 * height - 5 * age - 161

class DailyCalories:
    @staticmethod
    def calculate_daily_calories(bmr, workout_days, workout_duration, met_value):
        """Adjust daily calories based on workout parameters."""
        # Assuming 1 hour of workout equals an increase of met_value times BMR/24
        daily_calorie_adjustment = bmr / 24 * met_value * (workout_duration / 60) * workout_days
        return bmr + daily_calorie_adjustment
    
class AminoAcidNeeds:
    @staticmethod
    def calculate_amino_acid_needs(weight, height, age, gender, activity_level, is_pregnant, is_lactating):
        """Calculate daily protein and essential amino acid needs."""
        # Setting variables based on activity level
        workout_days, workout_duration, met_value = 0, 0, 1.2  # Defaults for Sedentary
        if activity_level == "Moderate":
            workout_days, workout_duration, met_value = 3, 45, 4.5
        elif activity_level == "Active":
            workout_days, workout_duration, met_value = 5, 60, 6

        bmr = BMRCalculator.calculate_bmr(weight, height, age, gender)
        daily_calories = DailyCalories.calculate_daily_calories(bmr, workout_days, workout_duration, met_value)

        """Estimates daily protein needs and hypothetical amino acid distribution from total protein."""
        protein_needs = (
            daily_calories * 0.15 / 4
        )  # 15% of calories from protein, 4 cal/g of protein

        # Additional protein for pregnant or lactating females
        if gender.lower() == "female":
            if is_pregnant:
                protein_needs += 25
            if is_lactating:
                protein_needs += 20

        # WHO guideline values for essential amino acids (in mg/kg/day)
        amino_acids = {
            "Essential": {
                "Histidine": 10,
                "Isoleucine": 20,
                "Leucine": 39,
                "Lysine": 30,
                "Methionine": 10.4,
                "Phenylalanine": 25,
                "Threonine": 15,
                "Tryptophan": 4,
                "Valine": 26,
            },
            "Conditional": {
                "Arginine": 214.29,
                "N-Acetyl Cysteine": 14.29,
                "Glycine": 42.86,
                "Proline": 21.43,
                "Tyrosine": 200,
            },
            "Non-essential": {
                "Beta-Alanine": 45.71,
                "Asparagine": 1.28,
                "D-Aspartic acid": 42.86,
                "Betaine": 85.71,
                "Glutamic acid (Glutamate)": 30,
                "Glutamine": 71.43,
                "Hydroxyproline": 4.29,
                "Ornithine": 85.71,
                "Serine": 57.14,
            },
        }

        amino_acid_needs = {"Essential": {}, "Conditional": {}, "Non-essential": {}}
        total_per_category = {"Essential": 0, "Conditional": 0, "Non-essential": 0}

        for category in amino_acids:
            total = 0
            for aa, value in amino_acids[category].items():
                need_in_grams = round((value * weight) / 1000, 2)  # Convert mg to grams
                amino_acid_needs[category][aa] = need_in_grams
                total += need_in_grams
            total_per_category[category] = total

        return protein_needs, amino_acid_needs, total_per_category, daily_calories


"""
def print_amino_acid_needs(amino_acid_needs, total_per_category):
    print("Estimated Daily Amino Acid Needs in grams:\n")
    for category, needs in amino_acid_needs.items():
        print(f"{category}:")
        for aa, need in needs.items():
            milligrams = need * 1000
            print(f"  {aa}: {need:.2f} g ({milligrams:.0f} mg)")
        total_grams = total_per_category[category]
        total_milligrams = total_grams * 1000
        print(f"  Total {category}: {total_grams:.2f} g ({total_milligrams:.0f} mg)\n")
"""

class AAPrinter:
    @staticmethod
    # New print function for displaying html
    def print_amino_acid_needs(amino_acid_needs, total_per_category):
        results = "Estimated Daily Amino Acid Needs in grams:<br>"
        for category, needs in amino_acid_needs.items():
            results += f"{category}:<br>"
            for aa, need in needs.items():
                milligrams = need * 1000
                results += f"&nbsp;&nbsp;{aa}: {need:.2f} g ({milligrams:.0f} mg)<br>"
            total_grams = total_per_category[category]
            total_milligrams = total_grams * 1000
            results += f"&nbsp;&nbsp;Total {category}: {total_grams:.2f} g ({total_milligrams:.0f} mg)<br><br>"
        return results


"""
# Example usage
weight = 70  # kg
height = 175  # cm
age = 30  # years
gender = "Male"
workout_days = 3
workout_duration = 45  # minutes
workout_intensity = "Moderate"
is_pregnant = False
is_lactating = False


protein_needs, amino_acid_needs, total_per_category, total_daily_calories = (
    calculate_amino_acid_needs(
        weight,
        height,
        age,
        gender,
        workout_days,
        workout_duration,
        workout_intensity,
        is_pregnant,
        is_lactating,
    )
)

print(f"Estimated Daily Calorie Needs: {total_daily_calories:.2f} kcal")
print(f"Estimated Daily Protein Needs: {protein_needs:.2f} g")
print_amino_acid_needs(amino_acid_needs, total_per_category)
"""
