import pandas as pd
import matplotlib.pyplot as plt
from dataset_loader import load_dataset

df = load_dataset("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

df.columns = df.columns.str.strip()

df.replace([float("inf"), float("-inf")], pd.NA, inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

features = [
    "Flow Duration",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Packet Length Mean",
    "Average Packet Size",
    "Fwd Packet Length Mean"
]

for feature in features:

    plt.figure(figsize=(8,5))

    plt.hist(df[feature], bins=50)

    plt.title(feature)

    plt.xlabel(feature)

    plt.ylabel("Frequency")

    plt.tight_layout()

    file_name = feature.replace("/", "_").replace(" ", "_")

    plt.savefig(f"reports/{file_name}.png")

    plt.show()