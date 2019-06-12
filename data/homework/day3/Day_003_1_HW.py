import pandas as pd
import numpy as np
data = dict()
data["Taiwan"]  = np.random.randint(1e7)
data["USA"]     = np.random.randint(1e4)
data_pd = pd.DataFrame.from_dict(data, columns=["population"], orient="index")
data_pd.index.name = "country"
print (data_pd)
