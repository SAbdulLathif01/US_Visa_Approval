import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir = 'logs'
#log_dir = os.path.join(from_root(), 'logs')

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

#logs_path = os.path.join(from_root(), 'logs', LOG_FILE)


os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

'''logging.basicConfig(
    level=logging.DEBUG,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(logs_path),
        logging.StreamHandler()
    ]
)'''