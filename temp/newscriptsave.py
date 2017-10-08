#For Sachathya

import sys
import inspect
from schLib import schLookups as lookups
import os

os.environ["REQUESTS_CA_BUNDLE"] = os.path.join(os.getcwd(),'certifi', 'cacert.pem')
print(os.environ["REQUESTS_CA_BUNDLE"])
print('Hello every one. This is from Common Starter')