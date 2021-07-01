import pandas as pd

from mongoDB.init_db import sinfun

cursor = sinfun.find()
entries = list(cursor)
entries[:1]

df = pd.DataFrame(entries)
df.head()
print(df.head)
