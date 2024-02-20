from flask import Flask, render_template, request, redirect, url_for

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
        print("Please enter valid numerical values.") # Come up with better error handling
        return redirect(url_for("index"))

    # Convert weight to kilograms for calculations
    if weight_unit == "lb":
        weight = weight * 0.453592

    # Convert height from feet,inches to inches
    total_height_inches = (height_feet * 12) + height_inches
    # Convert inches to centimeters if needed for calculations
    total_height_cm = total_height_inches * 2.54

    gender = request.form.get("gender")
    activity_level = request.form.get("activity")
    pregnancy_status = request.form.get("pregnancy")

    # Calculation logic

    return render_template(
        "results.html",
        age=age,
        weight=weight,
        height=total_height_cm,
        gender=gender,
        activity_level=activity_level,
        pregnancy_status=pregnancy_status,
    )  # Renders results page based on input


if __name__ == "__main__":
    app.run(debug=True)
