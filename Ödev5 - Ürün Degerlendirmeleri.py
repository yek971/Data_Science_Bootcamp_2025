#DUTY 1: Calculate the Average Rating based on recent comments.
#In this duty, you"ll calculate the average ranking of the products considering up-to-date comments and compare it with actual average.

import pandas as pd
import datetime as dt
import math
import scipy.stats as st

df = pd.read_csv(r'C:\Users\yek97\OneDrive\Masaüstü\Data Science Eurotech\amazon_review.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%5f' % x)


#STEP 1: Calculate the average rating of the product.


df["reviewTime"].min()
df["reviewTime"].max()

df ["day_diff"].describe()
df ["day_diff"].mean()

#STEP 2: Calculate the weighted average time based rating, with more recent comments being more weighted.


def weighted_average_time_based(dataframe, w1=28, w2=26, w3=24, w4=22):
    return dataframe.loc[dataframe["day_diff"] <= 280, ["day_diff"]].mean() * w1 / 100 + \
           dataframe.loc[(dataframe["day_diff"] > 280) & (dataframe["day_diff"] <= 430), "overall"].mean() * w2 / 100 + \
           dataframe.loc[(dataframe["day_diff"] > 430) & (dataframe["day_diff"] <= 600), "overall"].mean() * w3 / 100 + \
           dataframe.loc[(dataframe["day_diff"] > 600), "overall"].mean() * w4 / 100

    weighted_average_time_based(df)
    weighted_average_time_based(df, 28, 26, 24, 22)


#DUTY 2: Decide on top 20 comments on detailed product page. In this duty, you"re supposed to decide on top 20 useful comments.
#STEP 1: Set up helpful_no variable.
#total_vote, is the total number of votes given to a comment. bir yoruma verilen toplam oy sayısıdır.
#helpful_yes, is the amount of times a comment is found useful.
#helpful_no variable is calculated by subtracting useful comments from total comments: helpful_no = total_vote - helpful_yes

df["helpful_no"] = df["total_vote"] - df["helpful_yes"]
df.head()



#STEP 2: Calculate score_pos_neg_diff, score_average_rating ve wilson_lower_bound scores and add them to the data set.
#score_pos_neg_diff: The difference between useful comments and useless comments.
#average_rating_score: Ratio of useful comments to all the comments.
#wilsonlowerbound: Wilson Lower Bound, is a statistical method that measures the trustworthiness of a comment.

def score_pos_neg_diff(helpful_yes, helpful_no):
    return helpful_yes - helpful_no
df["score_pos_neg_diff"] = df.apply(lambda n: score_pos_neg_diff(n["helpful_yes"],n["helpful_no"]), axis=1)
df.head(10)

def score_pos_neg_diff(helpful_yes,helpful_no, confidence = 0.95):
    return helpful_yes - helpful_no

def score_pos_neg_diff(helpful_yes,helpful_no, confidence = 0.95):
n = ["helpful_yes"] + ["helpful_no"]
if n == 0:
    return 0

p =  "helpful_yes"/ n
z = st.norm.ppf(1 - (1 - confidence) / 2)
payda = 1 + z ** 2 / n
pay = p + z ** 2 / (2 * n) - z * np.sqrt((p * (1 - p) + z ** 2 / (4 * n)) / n)
return pay / payda

df["wilson_lower_bound"] = df.apply(lambda x: wilson_lower_bound(x["helpful_yes"], x["helpful_no"]), axis=1)
df

#STEP 3: Set up top 20 comments with the highest score according to Wilson Lower Bound.

df.sort_values("wilson_lower_bound", ascending=False, head=20)