import logging
import os

LOG_DIR = "output"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename="output/test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()