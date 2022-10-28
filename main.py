import pandas as pd
import os

filename = os.listdir("downloaded")[0]
f = os.path.abspath("downloaded/" + filename)

print(f)
read_file = pd.read_excel(f, engine='openpyxl')


# for filename in os.listdir("downloaded"):
#     f = os.path.join("downloaded", filename)
#     # checking if it is a file
#     if os.path.isfile(f):
#         read_file = pd.read_excel(f)
#         read_file.to_csv(f.split(".")[0] + ".csv")
