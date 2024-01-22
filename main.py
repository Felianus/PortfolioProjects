import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
pd.options.display.width = 0
plt.style.use("ggplot")
matplotlib.rcParams["figure.figsize"] = (12,8)
pd.set_option("display.max_columns", 15)
pd.set_option("display.max_rows", 20)
df= pd.read_csv(r"C:\Users\Kevin\Documents\CsvFiles\movies.csv")

#Check how many Values are Null
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())*100
    print(f"{col} - {pct_missing}% ")

#Cleanup the Data
df= df.dropna()
df= df.drop_duplicates()
for col in ["votes","budget","gross"]:
    df[col]= df[col].astype("int64")

#Create new Column with the correct year of release
for index1,row in df.iterrows():
    df.loc[index1,"year_correct"]= df.loc[index1,"released"][df.loc[index1,"released"].index("(")-5:df.loc[index1,"released"].index("(")-1]

#Plotting data
# df=df.sort_values(by=["gross"], ascending= False)
# plt.scatter(x=df["budget"], y=df["gross"])
# plt.title("Budget vs Gross Earnings")
# plt.xlabel("Budget")
# plt.ylabel("Gross Earnings")
# plt.show()

# sns.regplot(x="budget",y="gross", data= df, line_kws={"color":"blue"})
# plt.show()

#Check Correlation
corr = df.corr(numeric_only=True,method="pearson")
sns.heatmap(corr,annot=True)
plt.title("Correlation Matrix")
plt.xlabel("Features")
plt.ylabel("Features")
plt.show()
