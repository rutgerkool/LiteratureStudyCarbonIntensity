import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("primary_studies.csv")

data["Energy"] = data["Energy"].fillna("")

methods = {
    "Direct hardware-based": {},
    "Modeled methods": {},
    "Direct software-based": {},
    "Indirect estimation": {}
}

for _, row in data.iterrows():
    energy_methods = row["Energy"].split(";")
    for method in energy_methods:
        if method in {"Intel RAPL", "NVIDIA-SMI", "NVML", "CodeCarbon", "psutil", "DCGM"}:
            methods["Direct hardware-based"][method] = methods["Direct hardware-based"].get(method, 0) + 1
        elif method in {"Workload Models", "Instance Metrics", "Bohra-Chaudhary"}:
            methods["Modeled methods"][method] = methods["Modeled methods"].get(method, 0) + 1
        elif method in {"PowerAPI"}:
            methods["Direct software-based"][method] = methods["Direct software-based"].get(method, 0) + 1
        elif method in {"Cloud Provider Reports"}:
            methods["Indirect estimation"][method] = methods["Indirect estimation"].get(method, 0) + 1

for category in methods:
    methods[category] = dict(sorted(methods[category].items(), key=lambda item: item[1], reverse=True))

colors = {
    "Intel RAPL": "#000080",
    "NVIDIA-SMI": "#0000e6",
    "NVML": "#4d4dff",
    "CodeCarbon": "#e6e6ff",
    "psutil": "#b3b3ff",
    "DCGM": "#8080ff",
    "Workload Models": "#2ca02c",
    "Instance Metrics": "#7de37d",
    "Bohra-Chaudhary": "#98df8a",
    "PowerAPI": "#ff7f0e",
    "Cloud Provider Reports": "#d62728"
}

categories = list(methods.keys())
sub_methods = [list(sub.keys()) for sub in methods.values()]
sub_counts = [list(sub.values()) for sub in methods.values()]

fig, ax = plt.subplots(figsize=(12, 8))

for i, category in enumerate(categories):
    cumulative_height = 0 
    for sub_method, count in zip(sub_methods[i], sub_counts[i]):
        ax.bar(category, count, bottom=cumulative_height, color=colors[sub_method], label=sub_method)
        cumulative_height += count

ax.set_ylabel("Number of Papers", fontsize=16)
ax.set_xlabel("Energy Consumption Measurement Categories", fontsize=16)

ax.tick_params(axis='both', which='major', labelsize=12)

handles, labels = ax.get_legend_handles_labels()
unique_labels = dict(zip(labels, handles)) 
ax.legend(unique_labels.values(), unique_labels.keys(), loc="upper left", bbox_to_anchor=(1.05, 1), fontsize=12)

plt.tight_layout()

plt.savefig("energy_consumption_stacked_bar_chart.png", dpi=300)
