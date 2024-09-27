from data_loader import get_datasets

train_ds, val_ds, test_ds = get_datasets("data/train", "data/val", "data/test")

print("✅ Dataset loaded successfully!")
print("Number of training batches:", len(train_ds))
print("Class Names:", train_ds.class_names)
