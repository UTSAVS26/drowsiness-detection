import os
import shutil
import random
from tqdm import tqdm

# Directories
data_root = '../../data/drowsiness/'
train_dir = os.path.join(data_root, 'train')
val_dir = os.path.join(data_root, 'val')
processed_dir = '../../data/processed/'

# Create processed directory if not exists
os.makedirs(processed_dir, exist_ok=True)

# Function to preprocess data
def preprocess_data(input_dir, output_dir):
    classes = os.listdir(input_dir)
    
    for class_name in classes:
        class_dir = os.path.join(input_dir, class_name)
        output_class_dir = os.path.join(output_dir, class_name)
        os.makedirs(output_class_dir, exist_ok=True)
        
        images = os.listdir(class_dir)
        random.shuffle(images)
        num_images = min(500, len(images))  # Limit to 500 images per class for example
        
        # Use tqdm for progress bar
        with tqdm(total=num_images, desc=f'Processing {class_name} images') as pbar:
            for img in images[:num_images]:
                src = os.path.join(class_dir, img)
                dst = os.path.join(output_class_dir, img)
                shutil.copy(src, dst)
                pbar.update(1)  # Update progress bar
        
        pbar.close()  # Close progress bar after finishing

# Preprocess training data
preprocess_data(train_dir, processed_dir)

# Preprocess validation data
preprocess_data(val_dir, processed_dir)