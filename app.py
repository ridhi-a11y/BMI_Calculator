from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None

    if request.method == "POST":
        weight = float(request.form.get("weight"))
        height = float(request.form.get("height"))
        weight_unit = request.form.get("weight_unit")
        height_unit = request.form.get("height_unit")

        # Convert weight to kg
        if weight_unit == "lb":
            weight = weight * 0.453592

        # Convert height to meters
        if height_unit == "cm":
            height = height / 100
        elif height_unit == "ft":
            height = height * 0.3048

        # BMI calculation
        bmi = round(weight / (height ** 2), 2)

        # Category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal weight"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

    return render_template("index.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True)
