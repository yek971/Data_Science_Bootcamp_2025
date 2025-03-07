#DUTY 1: Answer the questions below:

#Question 1: Read customers.csv file and display general info about the data set.

import seaborn as sns
import pandas as pd
from sqlalchemy.dialects.mssql.information_schema import columns

df = pd.read_csv("C:/Users/yek97/OneDrive/Masaüstü/customers.csv")

print(df.head())

print(df.tail())

print(df.info())   # Overview of dataset

print(df.describe()) # Summary statistics

print(df.columns()) # Column names

print(df.shape)

print(df.index)

print(df.isnull().values.any())

print(df.isnull().sum())
#Question 2: How many unique PLATFORMS are there? What are their frequencies?
import seaborn as sns
import pandas as pd

df["PLATFORM"].nunique()

#Question 2: How many unique PRICES are there?

df["PRICE"].nunique()

#Question 3: How many sales have been done from each PRICE?

sales_count_by_price = df.groupby("PRICE").size()
print(sales_count_by_price)

#Question 5: How many sales have been done from each country?
sales_count_by_price = df.groupby("REGION").size()
print(sales_count_by_price)

#Question 6: Based on sales in each country, how much revenue in total has been made?

revenue_by_region = df.groupby("REGION")["PRICE"].sum()
print(revenue_by_region)

revenue_by_region2 = df.groupby("REGION")["PRICE"].count()
print(revenue_by_region2)

#Question 7: What's the total amount of sales based on platform?

satis_sayilari = df["PLATFORM"].value_counts()
print(satis_sayilari)

#Question 8: What are the PRICE averages based on each region?

satis_ortalamalari_ulke = df.groupby("REGION")["PRICE"].mean()
print(satis_ortalamalari)

#Question 9: What are the PRICE averages based on each platform?

satis_ortalamalari_platform = df.groupby("PLATFORM")["PRICE"].mean()
print(satis_ortalamalari_platform)

#Question 10: What are the PRICE averages at REGION-PLATFORM intersection?

satis_ortalamalari_ulke_platform = df.groupby(["REGION", "PLATFORM"])["PRICE"].mean()
print(satis_ortalamalari_ulke_platform)

satis_ortalamalari_platform_ulke = df.groupby(["PLATFORM", "REGION"])["PRICE"].mean()
print(satis_ortalamalari_platform_ulke)

#DUTY 2: What are the average turnovers at the intersection of REGION,PLATFORM,GENDER,AGE?

satis_ortalamalari_genel= df.groupby(["REGION","PLATFORM","GENDER","AGE"])["PRICE"].mean()
print(satis_ortalamalari_genel)

#DUTY 3:  Put the output in a descending order based on PRICE and save the results as agg_df

agg_df = (df.groupby(["REGION", "PLATFORM"])["PRICE"]
      .agg(["mean", "sum"])
      .sort_values("mean", ascending=False)
      .reset_index()

#DUTY 4: Define the names at the index as variables

df = agg_df.reset_index()

df.head()
df.dtypes()

for column in df.column:
    globals()[column] = df[column]

#DUTY 5: Categorize the AGE variable and add it to agg_df. Age categories should be such as:
    #0_18
    #19_23
    #24_30
    #31_40
    #41_70


import seaborn as sns
import pandas as pd
df = pd.read_csv("C:/Users/yek97/OneDrive/Masaüstü/customers.csv")


bins = [0, 18, 23, 30, 40, 70]
labels = ["0_18", "19_23", "24_30", "31_40", "41_70"]

df["AGE"] = pd.cut(df["AGE"], bins, labels)

print(df["AGE"])
agg_df = df.copy()
print(agg_df.head())


#DUTY 6: Construct new level-based customer groups. Add a new variable: customers_profile

import pandas as pd
import seaborn as sns
df = pd.read_csv("C:/Users/yek97/OneDrive/Masaüstü/customers.csv")

bins = [0, 18, 23, 30, 40, 70]
labels = ["0_18", "19_23", "24_30", "31_40", "41_70"]
df["AGE_CATEGORY"] = pd.cut(df["AGE"], bins=bins, labels=labels, right=True)
df["customer_profile"] = [ f"{region}_{platform}_{gender}_{age}" for region, platform, gender, age in zip(df["REGION"], df["PLATFORM"], df["GENDER"], df["AGE_CATEGORY"])]
agg_df = df.groupby("customer_profile").agg(PRICE_MEAN=("PRICE", "mean")).reset_index()
print(agg_df.head())


#DUTY 7: Divide the new customers (e.g. USA_ANDROID_MALE_0_18) into four segments based on PRICE.
#Add segments to "agg_df" as variables with the title "SEGMENT".
#Describe the segments (Use groupby function and find the mean,max and sum values)

df = pd.read_csv("C:/Users/yek97/OneDrive/Masaüstü/customers.csv")

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE_MEAN"], 4, labels=["D", "C", "B", "A"])
segment_summary = agg_df.groupby("SEGMENT").agg( PRICE_MEAN=("PRICE_MEAN", "mean"),
    PRICE_MAX=("PRICE_MEAN", "max"),
    PRICE_SUM=("PRICE_MEAN", "sum")).reset_index()

print(agg_df.head())
print(segment_summary)

#DUTY 8: Classify the new coming customers and estimate how much revenue they'll bring in.
#A 33-year-old Turkish woman who uses Android belongs to which segment and how much revenue is she expected to bring in?
#A 35-year-old French woman who uses IOS belongs to which segment and how much revenue is she expected to bring in?


import pandas as pd
import seaborn as sns
df = pd.read_csv("C:/Users/yek97/OneDrive/Masaüstü/customers.csv")

new_users = ["TUR_ANDROID_FEMALE_31_40", "FRA_IOS_FEMALE_31_40"]

for user in new_users:
    user_info = agg_df[agg_df["customer_profile"] == user]

if not user_info.empty:
        segment = user_info["SEGMENT"].values[0],
        expected_income = user_info["PRICE_MEAN"].values[0],
        print(f"{user} müşterisi {segment} segmentine aittir ve ortalama {expected_income:.2f} gelir kazandırması beklenir.")
    else:
        print(f"{user} müşterisi için veri bulunamadı.")
