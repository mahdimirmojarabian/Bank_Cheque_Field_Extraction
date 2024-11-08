import subprocess
# import sys

# print("Python executable:", sys.executable)
# print("Python path:", sys.path)

# Path to the virtual environment's Python interpreter
python_path = 'C:/Users/diagl_r84ooau/Desktop/Bank_Cheque_Field_Extraction/bank_env/Scripts/python.exe'

# Define the command and its parameters
command = [
    python_path, 'train.py',
    '--batch', '-1', '--epochs', '500', '--img', '640', '--device', '0',
    '--min-items', '0', '--close-mosaic', '15',
    '--data', 'data/data.yaml',
    '--weights', 'weights/gelan-c.pt',          # 'initial weights path'
    '--cfg', 'models/detect/gelan-c.yaml',      # train using the GELAN-C architecture
    '--hyp', 'data/hyps/hyp.scratch-high.yaml', # hyperparameters path
    '--save-period', '100'                      # Save checkpoint every 100 epochs
]

# Run the command
result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')

# Print the output and error (if any)
print(result.stdout)
print(result.stderr)
