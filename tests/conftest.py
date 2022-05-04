import os
import sys

# Set up the path to import from `shorty`.
root = os.path.join(os.path.dirname(__file__))
package = os.path.join(root, '../../..')
sys.path.insert(0, os.path.abspath(package))