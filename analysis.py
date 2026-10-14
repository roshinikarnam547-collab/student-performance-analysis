import pandas as pd
import matplotlib.pyplot as plt

# Load student data
df = pd.read_csv("students.csv")

# Calculate average marks
subjects = ["Python", "Java", "SQL"]
df["Average"] = df[subjects].mean(axis=1)

print("Student Performance Analysis")
print(df)

# Find the topper
topper = df.loc[df["Average"].idxmax()]
print("\nTop Performer:", topper["Name"])
print("Average Marks:", round(topper["Average"], 2))

# Plot average marks
plt.bar(df["Name"], df["Average"])
plt.title("Student Average Marks")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("student_performance.png")
plt.show()
