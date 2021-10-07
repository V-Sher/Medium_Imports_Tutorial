import sys
print(sys.path)
import os
fpath = os.path.join(os.path.dirname(__file__), 'utils')
# print(fpath)
sys.path.append(fpath)
# print(sys.path)
# print(os.path.dirname(__file__))

from length import get_length
from upper import to_upper
from lower import to_lower

txt = "Hello"

res_len = get_length(txt)
print("The length of the string is: ",res_len)

res_up = to_upper(txt)
print("Uppercase txt: ", res_up)

res_low = to_lower(txt)
print("Uppercase txt: ", res_low)

### Importing utils as a package ###

import utils
txt = "Hello"
res_len = utils.get_length(txt)
print(res_len)
res_up = utils.to_upper(txt)
print(res_up)
res_low = utils.to_lower(txt)
print(res_low)

utils.yolo(2)