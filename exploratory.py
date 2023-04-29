import numpy as np
import matplotlib.pyplot as plt

data = open("gruid-translator/out/out__1-0.json", "r").read()

# Initialize empty lists to store the data
means_side1 = []
stds_side1 = []
means_side2 = []
stds_side2 = []

# Loop through each event and calculate the mean and standard deviation of energy deposited
for event in data:
    # Side 1
    energy_side1 = []
    for k, v in data[int(event)]["gruid hits - side 1"]["0.0"].items():
        energy_side1.extend([hit["energy deposited"] for hit in v.values()])
    means_side1.append(np.mean(energy_side1))
    stds_side1.append(np.std(energy_side1))
    
    # Side 2
    energy_side2 = []
    for k, v in data[int(event)]["gruid hits - side 2"]["0.0"].items():
        energy_side2.extend([hit["energy deposited"] for hit in v.values()])
    means_side2.append(np.mean(energy_side2))
    stds_side2.append(np.std(energy_side2))

# Plot the results
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs[0, 0].bar(range(len(data)), means_side1, yerr=stds_side1)
axs[0, 0].set_xticks(range(len(data)))
axs[0, 0].set_xticklabels(list(data.keys()))
axs[0, 0].set_ylabel("Mean energy deposited (Side 1)")
axs[0, 1].bar(range(len(data)), means_side2, yerr=stds_side2)
axs[0, 1].set_xticks(range(len(data)))
axs[0, 1].set_xticklabels(list(data.keys()))
axs[0, 1].set_ylabel("Mean energy deposited (Side 2)")
axs[1, 0].hist(energy_side1, bins=20)
axs[1, 0].set_xlabel("Energy deposited (Side 1)")
axs[1, 0].set_ylabel("Frequency")
axs[1, 1].hist(energy_side2, bins=20)
axs[1, 1].set_xlabel("Energy deposited (Side 2)")
axs[1, 1].set_ylabel("Frequency")
plt.tight_layout()
plt.show()
