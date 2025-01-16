import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("primary_studies.csv")

system_counts = data["System"].value_counts()

categories = system_counts.index.tolist()
counts = system_counts.values.tolist()

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(categories, counts, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], width=0.6, edgecolor='black')

ax.set_xlabel("System Type", fontsize=16)
ax.set_ylabel("Number of Papers", fontsize=16)
ax.tick_params(axis='both', labelsize=12)

for bar, count in zip(bars, counts):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 0.2, str(count), ha='center', va='bottom', fontsize=12)

ax.set_ylim(0, max(counts) + 2)

plt.tight_layout()
plt.savefig("simulators_vs_real_systems_bar_chart.png", dpi=300)

data["API"] = data["API"].fillna("") 
api_list = data["API"].str.split(";").explode()

api_list = api_list[api_list != ""]

api_counts = api_list.value_counts()

sorted_apis = api_counts.index.tolist()[::-1]
sorted_counts = api_counts.values.tolist()[::-1]

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.barh(sorted_apis, sorted_counts, color=plt.cm.tab20.colors[:len(sorted_apis)], edgecolor='black')

ax.set_xlabel("Number of Papers", fontsize=16)
ax.set_ylabel("APIs Used", fontsize=16)
ax.tick_params(axis='both', labelsize=12)

for bar, count in zip(bars, sorted_counts):
    width = bar.get_width()
    ax.text(width + 0.2, bar.get_y() + bar.get_height() / 2, str(count), ha='left', va='center', fontsize=12)

ax.set_xlim(0, max(sorted_counts) + 1)

plt.tight_layout()
plt.savefig("api_usage_horizontal_bar_chart.png", dpi=300)
