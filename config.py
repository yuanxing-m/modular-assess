import os
from pathlib import Path

path_env = os.path.dirname(os.path.abspath("config.py"))

# path_chromedriver = str(Path(path_env, 'tools/chromedriver_mac'))
path_chromedriver = str(Path(path_env, 'tools/chromedriver.exe'))

