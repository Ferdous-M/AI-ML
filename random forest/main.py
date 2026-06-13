
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv(r"D:\python\random forest\student_data.csv")

# Features (inputs)
X = data[["StudyHours", "Attendance"]]

# Target (output)
y = data["Passed"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")

# Feature importance
print("\nFeature Importance:")
for feature, importance in zip(X.columns, model.feature_importances_):
    print(f"{feature}: {importance:.4f}")

# Predict a new student
new_student = pd.DataFrame({
    "StudyHours": [7],
    "Attendance": [88]
})

prediction = model.predict(new_student)

print("\nNew Student Prediction:")
if prediction[0] == 1:
    print("PASS")
else:
    print("FAIL")