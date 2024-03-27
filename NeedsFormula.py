
class NutritionalNeeds:
    def __init__(self,weight,height,age,gender,activity_level,is_pregnant,is_lactating,goal):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.activity_level = activity_level
        self.is_pregnant = is_pregnant
        self.is_lactating = is_lactating
        self.goal = goal

        self.bmr = self.calculate_bmr()
        self.daily_calories = self.calculate_daily_calories()

    def calculate_bmr(self):
        """Calculates the Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation.
        Returns: Bmr in calories (g)
        """
        if self.gender == "male":
            return 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            return 10 * self.weight + 6.25 * self.height - 5 * self.age - 161

    def calculate_daily_calories(self):
        """Calculate daily calories based on workout parameters and goal.
        Returns: Total daily calories (g) rounded to 2 dec places
        """
        workout_days, workout_duration, met_value = 0, 0, 1.2  # Defaults for Sedentary
        if self.activity_level == "moderate":
            workout_days, workout_duration, met_value = 3, 45, 4.5
        elif self.activity_level == "active":
            workout_days, workout_duration, met_value = 5, 60, 6

        daily_calorie_adjustment = (
            self.bmr / 24 * met_value * (workout_duration / 60) * workout_days
        )
        daily_calories = self.bmr + daily_calorie_adjustment

        # Adjust calorie intake based on goal
        if self.goal == "lose":
            daily_calories = daily_calories * 0.8  # Decrease calories by 20%
        elif self.goal == "gain":
            daily_calories = daily_calories * 1.2  # Increase calories by 20%
        else:
            daily_calories = daily_calories  # Maintain calories

        return round(daily_calories, 2)

    def calculate_amino_acid_needs(self):
        """Calculate daily amino acid needs.
        Returns: Amino acid needs in string for html output
        """
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
            for aa, value in amino_acids[category].items():
                need_in_grams = round(
                    (value * self.weight) / 1000, 2
                )  # Convert mg to grams
                amino_acid_needs[category][aa] = need_in_grams
                total_per_category[category] += need_in_grams

        # Return amino acid needs in string for html output
        amino_acid_results = ""
        for category, needs in amino_acid_needs.items():
            amino_acid_results += f"{category}:<br>"
            for aa, need in needs.items():
                milligrams = need * 1000
                amino_acid_results += (
                    f"&nbsp;&nbsp;{aa}: {need:.2f} g ({milligrams:.0f} mg)<br>"
                )
            total_grams = total_per_category[category]
            total_milligrams = total_grams * 1000
            amino_acid_results += f"&nbsp;&nbsp;Total {category}: {total_grams:.2f} g ({total_milligrams:.0f} mg)<br><br>"
        amino_acid_results += f""
        return amino_acid_results

    def calculate_macros_needs(self):
        """Calculate daily macronutrient needs: protein, fat, and carbohydrates.
        Returns: Macros needs in string for html output
        """
        if self.goal == "lose":
            protein_percentage = 0.4
            fat_percentage = 0.3
            carb_percentage = 0.3
        elif self.goal == "gain":
            protein_percentage = 0.3
            fat_percentage = 0.2
            carb_percentage = 0.5
        else:  # Maintain
            protein_percentage = 0.3
            fat_percentage = 0.3
            carb_percentage = 0.4

        protein_needs = self.daily_calories * protein_percentage / 4
        if self.gender == "female":
            if self.is_pregnant:
                protein_needs += 25
            if self.is_lactating:
                protein_needs += 20

        fat_needs = self.daily_calories * fat_percentage / 9
        carb_needs = self.daily_calories * carb_percentage / 4

        # Return macros needs in nicely formatted string for html output
        macros_results = f"Protein: {protein_needs:.2f} g<br>"
        macros_results += f"Fat: {fat_needs:.2f} g<br>"
        macros_results += f"Carbohydrates: {carb_needs:.2f} g<br>"
        return macros_results