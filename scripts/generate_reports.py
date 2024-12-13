import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Define paths
cleaned_data_path = os.path.join("data", "cleaned")
report_output_path = os.path.join("reports")
os.makedirs(report_output_path, exist_ok=True)

# List all .csv files in the cleaned directory
cleaned_files = [os.path.join(cleaned_data_path, file) for file in os.listdir(cleaned_data_path) if file.endswith(".csv")]
if not cleaned_files:
    raise FileNotFoundError("No .csv files found in the data/cleaned directory.")

# Load and combine all cleaned files
dataframes = [pd.read_csv(file) for file in cleaned_files]
combined_data = pd.concat(dataframes, ignore_index=True)

# Standardize column names
combined_data.columns = [
    "type_of_construction",
    "jan_2024",
    "dec_2023",
    "nov_2023",
    "oct_2023",
    "sep_2023",
    "jan_2023",
    "percent_change_dec",
    "percent_change_jan"
]

# Ensure numeric columns are properly formatted
numeric_columns = [
    "jan_2024", "dec_2023", "nov_2023", "oct_2023", "sep_2023", "jan_2023",
    "percent_change_dec", "percent_change_jan"
]
combined_data[numeric_columns] = combined_data[numeric_columns].apply(pd.to_numeric, errors="coerce").fillna(0)

# Spending Trends Report
combined_data_melted = combined_data.melt(
    id_vars=["type_of_construction"],
    value_vars=["jan_2024", "dec_2023", "nov_2023", "oct_2023", "sep_2023", "jan_2023"],
    var_name="month",
    value_name="spending"
)

plt.figure(figsize=(12, 8))  # Adjusted size
sns.lineplot(
    data=combined_data_melted,
    x="month",
    y="spending",
    hue="type_of_construction",
    marker="o",
    palette="tab10"
)
plt.title("Spending Trends by Construction Type (2023-2024)", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Spending (Millions)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.legend(title="Construction Type", bbox_to_anchor=(0.5, -0.25), loc="lower center", ncol=3)  # Legend below
plt.tight_layout()
plt.savefig(os.path.join(report_output_path, "spending_trends.png"), bbox_inches="tight")
plt.close()

# Top Construction Types Report
top_types = combined_data.groupby("type_of_construction")["jan_2024"].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 8))  # Adjusted size
sns.barplot(
    x=top_types.values,
    y=top_types.index,
    palette="coolwarm",
    hue=top_types.index
)
plt.title("Top Construction Types (January 2024)", fontsize=16)
plt.xlabel("Spending (Millions)", fontsize=12)
plt.ylabel("Type of Construction", fontsize=12)
for index, value in enumerate(top_types.values):
    plt.text(value + 0.05 * max(top_types.values), index, f"{value:,.0f}", va="center")
plt.legend().set_visible(False)  # Hide unnecessary legend
plt.tight_layout()
plt.savefig(os.path.join(report_output_path, "top_construction_types_jan_2024.png"), bbox_inches="tight")
plt.close()

# Enhanced Summary Report
summary = {
    "Total Spending (January 2024)": f"{combined_data['jan_2024'].sum():,.0f}",
    "Total Spending (December 2023)": f"{combined_data['dec_2023'].sum():,.0f}",
    "Top Construction Type (January 2024)": top_types.idxmax(),
    "Highest Spending Value (January 2024)": f"{top_types.max():,.0f}"
}

with open(os.path.join(report_output_path, "summary_report.txt"), "w") as f:
    for key, value in summary.items():
        f.write(f"{key}: {value}\n")