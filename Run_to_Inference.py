import subprocess
# import sys

# print("Python executable:", sys.executable)
# print("Python path:", sys.path)

# Path to the virtual environment's Python interpreter
python_path = 'C:/Users/diagl_r84ooau/Desktop/Bank_Cheque_Field_Extraction/bank_env/Scripts/python.exe'

# Define the command and its parameters
command = [
    python_path, 'detect.py',
    '--img', '1280', # We trained our model on images with a size of 640, which allows us to train a model with lesser computational resources. During inference, we increase the image size to 1280, allowing us to get more accurate results from our model.
    '--conf-thres', '0.1',
    '--iou-thres', '0.45'
    '--max-det', '1000',
    '--device', '0',
    '--save-crop',
    '--weights', 'runs/train/exp/weights/best.pt', # weights of our trained model
    '--source', 'data/valid/images'
]

# Run the command
result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')

# Print the output and error (if any)
print(result.stdout)
print(result.stderr)
