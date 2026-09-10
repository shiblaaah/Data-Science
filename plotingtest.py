import matplotlib.pyplot as plt

# Categories and values
subjects = ["Math", "Science", "English", "Computer", "History"]
marks = [85, 90, 78, 95, 80]

# Create bar graph
plt.bar(subjects, marks, color="skyblue")

# Add title and labels
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Display the graph
plt.show()
