# To do:
# Add more details to results
# Ideal weight?
# BMI

from flask import Flask, render_template, request, redirect, url_for
from NeedsFormula import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    # Access form data
    try:
        age = int(request.form.get("age"))
        weight = float(request.form.get("weight"))
        weight_unit = request.form.get("weight_unit", "lb")
        height_feet = int(request.form.get("height_feet"))
        height_inches = int(request.form.get("height_inches"))
    except ValueError:
        print(
            "Please enter valid numerical values."
        )  # Come up with better error handling
        return redirect(url_for("index"))

    gender = request.form.get("gender")
    activity_level = request.form.get("activity")
    pregnancy_status = request.form.get("pregnancy")
    goal = request.form.get("goal")

    # Convert weight to kilograms for calculations if not already
    if weight_unit == "lb":
        weight_in_kg = weight * 0.453592

    # Convert height from feet&inches to centimeters
    height = ((height_feet * 12) + height_inches) * 2.54

    # Set is_pregnant and is_lactating based on input selections
    if pregnancy_status == "none":
        is_pregnant = False
        is_lactating = False
    elif pregnancy_status == "pregnant":
        is_pregnant = True
        is_lactating = False
    elif pregnancy_status == "breastfeeding":
        is_pregnant = False
        is_lactating = True

    # Calculations using NeedsFormula NeedsCalculator
    needs = NutritionalNeeds(weight_in_kg, height, age, gender, activity_level, is_pregnant, is_lactating, goal)
    total_daily_calories = needs.calculate_daily_calories()
    macros_needs = needs.calculate_macros_needs()
    amino_acid_results = needs.calculate_amino_acid_needs()
    bmi, weight_category = needs.calculate_bmi()  # Unpack the return value

    # User data for results page recalculate form
    user_data = {
        "age": age,
        "weight": weight,
        "weight_unit": weight_unit,
        "height_feet": height_feet,
        "height_inches": height_inches,
        "gender": gender,
        "activity_level": activity_level,
        "pregnancy_status": pregnancy_status,
        "goal": goal,
    }

    return render_template(
        "results.html",
        total_daily_calories=total_daily_calories,
        macros_needs=macros_needs,
        amino_acid_results=amino_acid_results,
        bmi=bmi,  
        weight_category=weight_category,

        user_data=user_data,
    )  # Renders results page based on input


if __name__ == "__main__":
    app.run(debug=True)
