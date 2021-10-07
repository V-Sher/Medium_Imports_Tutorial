import os
import sys
print(sys.path)

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
print(PROJECT_ROOT)
sys.path.append(PROJECT_ROOT)
print(sys.path)

import utils

print(utils.get_length("Hello"))
utils.yolo(2)