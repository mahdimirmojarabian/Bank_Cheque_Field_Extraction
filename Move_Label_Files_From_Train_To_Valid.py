import os
import shutil

# Define paths
images_path = r'C:\Users\diagl_r84ooau\Desktop\Bank_Cheque_Field_Extraction\data\valid\images'
train_labels_path = r'C:\Users\diagl_r84ooau\Desktop\Bank_Cheque_Field_Extraction\data\train\labels'
valid_labels_path = r'C:\Users\diagl_r84ooau\Desktop\Bank_Cheque_Field_Extraction\data\valid\labels'

# Get all file names in the images directory without the .jpg extension
image_files = [os.path.splitext(f)[0] for f in os.listdir(images_path) if f.endswith('.jpg')]

# Move corresponding label files from train_labels_path to valid_labels_path
for file_name in image_files:
    label_file = f"{file_name}.txt"  # Assuming labels are text files with .txt extension
    src_file = os.path.join(train_labels_path, label_file)
    dst_file = os.path.join(valid_labels_path, label_file)
    
    if os.path.exists(src_file):
        shutil.move(src_file, dst_file)
        print(f"Moved: {label_file}")
    else:
        print(f"File not found: {label_file}")

print("Completed moving label files.")
