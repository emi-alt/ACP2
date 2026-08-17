import pandas as pd
serial = [1, 2, 3, 4, 5]
student = ['John', 'Alice', 'Bob', 'Diana', 'Eve']
marks = [85, 92, 78, 90, 88]
df = pd.Series(marks, index=student)
print("Results: ")
print(df)
attendance = pd.Series([187, 196, 123, 200, 190], index=serial)
df = pd.DataFrame({'Students': student, 'Marks': marks, 'Attendance': attendance})
print("\nDataframe:")
print(df)
df = pd.read_csv("student_marks.csv")
print("\nData from CSV:")
print(df.head())
print()
print(df.tail(2))
print()
print(df.info())
print()
serial = [1, 2, 3, 4, 5, 6, ' ', 8, 9, 10]
student = ['John', " ",'Alice', 'Bob', 'Jane', 'Charlie', 'Diana', 'Eve', 'Teddy', '']
#           1      2     3        4      5         6         7       8       9     10
marks = [85, 92, 78, 90, 88, 90, 95, 76, 64, 70]
#        1   2   3   4   5   6   7   8   9   10
 
student_marks = pd.Series(
    marks,
    index=student,
    name="Student Marks" 
)
print(student_marks)
data = {
    "Student":['John', "Maddy",'Alice', 'Bob', 'Jane', 'Charlie', 'Diana', 'Eve', 'Teddy', 'Kyle'],
    'Marks': [85, 92, 78, 90, 88, 90, 95, 76, 64, 70],
    "Attendance": [187, 196, 123, 200, 190, 180, 195, 170, 160, 175]
}
df = pd.DataFrame(data)
print(df)
  
df.to_csv("student_marks.csv", index=False)

student_data = pd.read_csv("student_marks.csv")
 
print("CSV file read successfully!")
print(student_data)
  
print("First 3 rows:")
print(student_data.head(3))
 
print("Last 2 rows:")
print(student_data.tail(2))
 
print("Data Information:")
print(student_data.info())

messy_data = {
    "Serial": [1, 2, 3, 4, 5, 6, ' ', 8, 9, 10],
    "Student": ['John', " ",'Alice', 'Bob', 'Jane', 'Charlie', 'Diana', 'Eve', 'Teddy', ''],
    "Marks": [85, 92, 78, 90, 88, 90, 95, " ", 64, 70]
}
 
messy_df = pd.DataFrame(messy_data)
 
print("Data with Missing Values:")
print(messy_df)
 
cleaned_df = messy_df.fillna(0)
 
print("Cleaned Data:")
print(cleaned_df)
 
# ------------------------------------------------
# PART 7 — SIMPLE ANALYSIS
# ------------------------------------------------
 
print("
PART 7: Student Total and Average Marks")
 
cleaned_df["Total"] = cleaned_df["Math"] + cleaned_df["Science"] + cleaned_df["English"]
cleaned_df["Average"] = cleaned_df["Total"] / 3
 
print(cleaned_df)
print("================================")
print("STUDENT MARKS ANALYSER SUMMARY")
print("================================")
print("Pandas was imported using import pandas as pd.")
print("A Series was used to store one column of marks.")
print("A DataFrame was used to store marks in table form.")
print("CSV data was created, read, and viewed.")
print("Missing values were cleaned using fillna().")
print("Total and average marks were calculated.")
print("================================")