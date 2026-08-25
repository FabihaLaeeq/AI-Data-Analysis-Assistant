from analysis import load_data, get_dataset_info, get_basic_statistics

df = load_data("sample_dataset.csv")

print(get_dataset_info(df))

print("\nStatistics:")
print(get_basic_statistics(df))