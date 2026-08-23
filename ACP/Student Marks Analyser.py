import pandas as pd

print("Student Marks Analyser") 
print()
print("PART 2: Pandas Series")
 
marks = [88, 76, 92, 67, 85]
 
student_marks = pd.Series(
    marks,
    index=["Aarav", "Meera", "Kabir", "Anaya", "Rohan"]
)
 
print(student_marks)
 
print()
print("PART 3: Pandas DataFrame")
 
data = {
    "Student": ["Aarav", "Meera", "Kabir", "Anaya", "Rohan"],
    "Math": [88, 76, 92, 67, 85],
    "Science": [91, 80, 89, 72, 87],
    "English": [84, 78, 95, 70, 82],
    "Attendance": [96, 90, 98, 85, 92]
}
 
df = pd.DataFrame(data)
 
print(df)

print()
print("PART 4: Reading Data from a CSV File")
 
df.to_csv("student_marks.csv", index=False)
 
student_data = pd.read_csv("student_marks.csv")
 
print("CSV file read successfully!")
print(student_data)

print()
print("PART 5: Viewing Data")
 
print()
print("First 3 rows:")
print(student_data.head(3))
 
print()
print("Last 2 rows:")
print(student_data.tail(2))
 
print()
print("Data Information:")
print(student_data.info())

print()
print("PART 6: Cleaning Data")
 
messy_data = {
    "Student": ["Aarav", "Meera", "Kabir", "Anaya", "Rohan"],
    "Math": [88, None, 92, 67, 85],
    "Science": [91, 80, None, 72, 87],
    "English": [84, 78, 95, None, 82]
}
 
messy_df = pd.DataFrame(messy_data)
 
print()
print("Data with Missing Values:")
print(messy_df)
 
cleaned_df = messy_df.fillna(0)
 
print()
print("Cleaned Data:")
print(cleaned_df)

print()
print("PART 7: Student Total and Average Marks")
 
cleaned_df["Total"] = cleaned_df["Math"] + cleaned_df["Science"] + cleaned_df["English"]
cleaned_df["Average"] = cleaned_df["Total"] / 3
 
print(cleaned_df)