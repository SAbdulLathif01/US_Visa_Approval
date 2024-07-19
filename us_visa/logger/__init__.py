import logging
import os
from datetime import datetime

# Directly set the root path to the D: drive project path
root_dir = os.path.abspath(r"D:\Projects ML\US_Visa_Approval")
#print("Root directory:", root_dir)

# Define log file and directory
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = 'logs'
full_log_dir = os.path.join(root_dir, log_dir)

# Print the full log directory path
#print("Full log directory:", full_log_dir)

# Ensure the log directory exists
os.makedirs(full_log_dir, exist_ok=True)

# Define full path for log file
logs_path = os.path.join(full_log_dir, LOG_FILE)

# Print the full path for the log file
#print("Log file path:", logs_path)

# Setup logging
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

# Add a test log entry

# Additional prints to ensure the function is working correctly
#print("Logging setup completed.")
