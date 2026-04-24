# 🧮 BMI Calculator Web App

A simple and interactive **Body Mass Index (BMI) Calculator** built using **Python (Flask)** and a basic **HTML/CSS frontend**.
This project allows users to calculate their BMI using different units (kg/lb, cm/m/ft) with automatic conversion and a clean UI.

---

## 🚀 Features

* 🌐 Web-based UI using Flask
* ⚖️ Supports multiple units:

  * Weight → Kilograms (kg), Pounds (lb)
  * Height → Centimeters (cm), Meters (m), Feet (ft)
* 🔄 Automatic unit conversion
* 📊 Displays BMI value and category:

  * Underweight
  * Normal weight
  * Overweight
  * Obese
* 🎨 Clean and responsive UI design

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS
* **Server:** Flask Development Server

---

## 📂 Project Structure

```
bmi_calculator/
│── app.py
│── templates/
│     └── index.html
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/bmi-calculator.git
cd bmi-calculator
```

### 2. Install dependencies

```
pip install flask
```

### 3. Run the application

```
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

1. User enters weight and height along with units
2. Backend converts values into standard units:

   * Weight → kilograms
   * Height → meters
3. BMI is calculated using:

```
BMI = weight / (height × height)
```

4. Based on the result, a category is displayed

---

## 📊 BMI Categories

| BMI Range   | Category      |
| ----------- | ------------- |
| < 18.5      | Underweight   |
| 18.5 – 24.9 | Normal weight |
| 25 – 29.9   | Overweight    |
| ≥ 30        | Obese         |

---

## ✨ Future Enhancements

* ⚡ Live calculation using JavaScript (no page reload)
* 📈 BMI history tracking with database (SQLite/PostgreSQL)
* 📊 Graph visualization of BMI trends
* 🌍 Deployment on cloud (AWS / Render / Heroku)
* ⚛️ Frontend upgrade using React

---

## 🤝 Contributing

Feel free to fork the repository and submit pull requests to improve the project.

---

## 👩‍💻 Author

**Ridhi Gupta**
Section 220A | UID: 25BAI10044

---
