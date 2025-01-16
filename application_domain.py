import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd

data = pd.read_csv("primary_studies.csv")

ordered_domains = data["Domain"].unique()
application_domains = {domain: data["Domain"].value_counts()[domain] for domain in ordered_domains}

category_shades = {
    "AI Workloads": list(mcolors.to_rgba_array(["#0033cc", "#0052cc", "#3366ff", "#668cff", "#99b3ff", "#ccd9ff"])), 
    "Cloud Computing": list(mcolors.to_rgba_array(["#ff7f0e", "#ffa559", "#ffc794", "#ffcc66"])),
    "Digital Services": list(mcolors.to_rgba_array(["#2ca02c"])),  
    "Energy Systems": list(mcolors.to_rgba_array(["#d62728"])) 
}

subdomain_to_category = dict(zip(data["Domain"], data["Category"]))

labels = list(application_domains.keys())
sizes = list(application_domains.values())
colors = []

for label in labels:
    category = subdomain_to_category[label]
    if not category_shades[category]: 
        category_shades[category] = list(mcolors.to_rgba_array(["#1f77b4", "#4f93cf", "#87bdeb", "#aec7e8"] if category == "AI Workloads" else
                                                     ["#ff7f0e", "#ffa559", "#ffc794", "#ffcc66"] if category == "Cloud Computing" else
                                                     ["#2ca02c"] if category == "Digital Services" else
                                                     ["#d62728"]))
    color_shade = category_shades[category].pop(0)
    colors.append(color_shade)

fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(
    sizes,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    textprops={'fontsize': 16},
    pctdistance=0.85  
)

category_positions = {
    "AI Workloads": (1.2, 0.3),
    "Cloud Computing": (-1.2, -0.4),
    "Digital Services": (-0.9, 0.85),
    "Energy Systems": (-0.2, 1.05)
}

category_colors = {
    "AI Workloads": "#1f77b4",      
    "Cloud Computing": "#ff7f0e",   
    "Digital Services": "#2ca02c",   
    "Energy Systems": "#d62728"      
}

for category, position in category_positions.items():
    ax.text(
        position[0],
        position[1],
        category,
        ha='center',
        va='center',
        fontsize=14,
        bbox=dict(boxstyle="round,pad=0.3", edgecolor=category_colors[category], facecolor='white')
    )

plt.legend(
    labels=[f"{label} ({size})" for label, size in zip(labels, sizes)],
    loc="upper center",
    bbox_to_anchor=(0.5, 0),  
    ncol=2,  
    fontsize=18  
)

plt.tight_layout()

plt.savefig("application_domain_pie_chart.png", dpi=300)
