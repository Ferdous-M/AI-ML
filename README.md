# Python Learning Journey 🐍

A comprehensive collection of Python practice files covering fundamental to intermediate concepts — from basic syntax and data structures to object-oriented programming, data analysis, and machine learning.

---

## 📁 Project Structure

```
python/
├── python basic/           # Python fundamentals
├── Data structure/         # Core data structures
├── OOP/                    # Object-Oriented Programming concepts
├── NumPy/                  # Numerical computing with NumPy
├── Pandas/                 # Data manipulation with Pandas
├── random forest/          # Machine Learning with Random Forest
├── data/                   # Jupyter notebooks & data files
├── web scrapping/          # Placeholder for future web scraping
└── hello.py                # Entry point
```

---

## 📚 Topics Covered

### 🔰 Python Basics — [`python basic/`](python%20basic/)
Fundamental building blocks of Python:
- **Variables & Data Types** — `variables.py`
- **Operators** — `operators.py`
- **Conditional Statements** — `if else.py`
- **Loops** — `loop.py`
- **Functions** — `function.py`
- **String Slicing** — `string_slicing.py`
- **Keywords** — `keywords.py`
- **First Scripts** — `hello.py`

### 📦 Data Structures — [`Data structure/`](Data%20structure/)
Manual implementations and demonstrations of classic data structures:
- **Lists** — `listDemo.py`
- **Tuples** — `tupleDemo.py`
- **Sets** — `setDemo.py`
- **Maps / Dictionaries** — `map.py`
- **Stacks** — `stackDemo.py`
- **Queues** — `queueDemo.py`
- **Recursion** — `recursion.py`
- **Search Algorithms** — `search.py`

### 🧩 Object-Oriented Programming — [`OOP/`](OOP/)
Core OOP principles with practical examples:
- **Classes & Objects** — `object.py`
- **Inheritance** — `inheritance.py`
- **Polymorphism** — `polymorphism.py`
- **Encapsulation** — `encapsulation.py`
- **Abstraction** — `abstraction.py`

### 🔢 NumPy — [`NumPy/`](NumPy/)
Numerical computing with NumPy — includes array operations, reshaping, indexing, and mathematical functions via interactive notebooks.

### 🐼 Pandas — [`Pandas/`](Pandas/)
Data analysis with Pandas — Series & DataFrames, data loading (CSV/JSON), filtering with `loc`/`iloc`/`query`, date/time handling, and data cleaning (missing values, duplicates). Includes sample datasets:
- **`employee_data.csv` / `employee_data.json`** — employee records
- **`raw_data.csv`** — messy data for cleaning practice
- **`globalAirQuality.csv`** — 18,000 rows of global air quality data

### 🧹 Data Cleaning — [`data/demo/`](data/demo/)
Practical data cleaning with Python:
- **`thinking_data.ipynb`** — loads `store_data.json`, cleans missing values, converts word-based ratings to numbers, and generates insights & recommendations

### 🌲 Random Forest — [`random forest/`](random%20forest/)
Machine learning project using **Random Forest Classifier** to predict student pass/fail based on study hours and attendance.
- **Libraries:** `pandas`, `scikit-learn`
- **Features:** StudyHours, Attendance
- **Model Evaluation:** Accuracy score & feature importance

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd python
   ```

2. **Install required packages:**
   ```bash
   pip install pandas numpy scikit-learn
   ```

### Run a script
```bash
# Python basics
python "python basic/hello.py"

# Data structures
python "Data structure/listDemo.py"

# OOP concepts
python "OOP/inheritance.py"

# Machine Learning
cd "random forest" && python main.py
```

For Jupyter notebooks, launch:
```bash
jupyter notebook
```

---

## 🎯 Purpose

This repository serves as a hands-on Python learning resource, progressing from:
1. **Beginner** — syntax, variables, control flow
2. **Intermediate** — data structures, OOP, NumPy, Pandas
3. **Applied ML** — building and evaluating a Random Forest model

Each topic is独立 (self-contained), making it easy to jump to the concept you want to study or review.

---

## 📝 License

This project is for educational purposes. Feel free to use, modify, and share.

---

*Happy coding!* 🚀
