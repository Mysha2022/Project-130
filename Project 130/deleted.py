import pandas as pd

# pandas module helps us by reading the data from csv files
df = pd.read_csv("merged_dataset.csv")

# to check the total number of rows and columns --> shape keyword is used
print(df.shape)

# (4284, 85) --> (rows , cols)


# delete extra columns
del df["luminosity"]
del df["NAN"]


print(df.shape)


df.to_csv("final.csv")
