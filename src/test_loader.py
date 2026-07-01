from dataset_loader import load_dataset

df = load_dataset("Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")

print(df.head())