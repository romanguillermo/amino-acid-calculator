from flask import Flask, render_template, request, redirect, url_for
from AAFormula import *

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

    # Convert weight to kilograms for calculations if not already
    if weight_unit == "lb":
        weight = weight * 0.453592

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

    # Calculation logic using AAFormula module
    protein_needs, amino_acid_needs, total_per_category, total_daily_calories = (
        AminoAcidNeeds.calculate_amino_acid_needs(
            weight,
            height,
            age,
            gender,
            activity_level,
            is_pregnant,
            is_lactating,
        )
    )

    amino_acid_results = AAPrinter.print_amino_acid_needs(amino_acid_needs, total_per_category)

    return render_template(
        "results.html",
        total_daily_calories=total_daily_calories,
        protein_needs=protein_needs,
        amino_acid_results=amino_acid_results,
    )  # Renders results page based on input


if __name__ == "__main__":
    app.run(debug=True)
