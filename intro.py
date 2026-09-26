import seaborn as sns
import matplotlib.pyplot as plt

# Apply default theme
sns.set_theme()

# Example dataset
tips = sns.load_dataset("tips")

# Create visualization
sns.relplot(
    data = tips,
    x = "total_bill", y = "tip", col = "time",
    hue = "smoker", style = "smoker", size = "size",
)

plt.show()
