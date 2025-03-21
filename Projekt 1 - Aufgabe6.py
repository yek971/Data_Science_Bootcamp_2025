import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#DUTY 1: DATA PREPARATION AND EVALUATION

#STEP 1: Read the control and test group data from ab_test_data.xlsx fileAssign the data of control group and test group to different variables.
sheet1 = pd.read_excel("C:\\Users\\yek97\\OneDrive\\Masaüstü\\ab_test_data.xlsx", sheet_name='Control Group')
sheet1.head()

sheet2 = pd.read_excel("C:\\Users\\yek97\\OneDrive\\Masaüstü\\ab_test_data.xlsx", sheet_name='Test Group')
sheet2.head()

#STEP 2: Analyze the main statistics of control and test group data.
#Calculate the main statistics such as mean, median and standard deviation.


sheet1.mean()
sheet1.median()
sheet1.std()

sheet2.mean()
sheet2.median()
sheet2.std()

#STEP 3: Use the concat method to concat the control group and test group data.
df_combined = pd.concat([sheet1, sheet2], axis=0, ignore_index=True)
print(df_combined.shape)


df_combined.mean()
df_combined.median()
df_combined.std()

#DUTY 2: DEFINING HYPOTHESIS FOR A/B TESTING
#STEP 1: Set up hypotheses like below
#H0: There's no meaningful difference between control group and test group M1 = M2
#H1: There's a meaningful difference between control group and test group M1 != M2

#STEP 2: Compute the purchase means of control and test group.
control_group = pd.read_excel("C:\\Users\\yek97\\OneDrive\\Masaüstü\\ab_test_data.xlsx", sheet_name="Control Group")
test_group = pd.read_excel("C:\\Users\\yek97\\OneDrive\\Masaüstü\\ab_test_data.xlsx", sheet_name="Test Group")

control_mean = control_group["Purchase"].mean()
test_mean = test_group["Purchase"].mean()

print(f"Control Group Purchase Average: {control_mean:.2f}")
print(f"Test Group Purchase Average: {test_mean:.2f}")

#DUTY 3: HYPOTHESIS TESTING AND ASSUMPTION CHECK
#STEP 1: Before starting hypothesis testing, run normality and variance homogeneity tests.
#STEP 2: Based on normality and variance homogeneity tests, pick the correct testing (t-Test or Mann-Whitney U Test)


import pandas as pd
from scipy.stats import shapiro, levene, ttest_ind

#1: Shapiro-Wilk Normality Test:
shapiro_control_group = shapiro(control_group["Purchase"])
shapiro_test_group = shapiro(test_group["Purchase"])

print(f"Control Group Normality Test p-value: {shapiro_control_group.pvalue}")
print(f"Test Group Normality Test p-value: {shapiro_test_group.pvalue}")


if shapiro_control_group.pvalue > 0.05 and shapiro_test_group.pvalue > 0.05:
    test_stat, p_value = ttest_ind(control_group["Purchase"], test_group["Purchase"], equal_var=True)
    test_type = "T-Test to be applied, "
print(f"{test_type} p-value: {p_value}")

if p_value < 0.05:
    print("Result: H0 could be rejected, there's a meaningful difference between control group and test group.")
else:
    print("Result: H0 couldn't be rejected , there's not a meaningful difference between control group and test group.")

# Control Group Normality Test p-value = 0.5891 > 0.05, the conditions are met for normality and homogenity so t-test will be applied to test hypotheses.
# Test Group Normality Test p-value: 0.1541, the conditions are met or normality and homogenity so t-test will be applied to test hypotheses.

#2: Levene Variance Homogeneity Test:

levene_test = levene(control_group["Purchase"], test_group["Purchase"])

if levene_test.pvalue > 0.05:
    test_stat, p_value = ttest_ind(control_group["Purchase"], test_group["Purchase"], equal_var=True)
    test_type = "T-Test to be applied, "
print(f"{test_type} p-value: {p_value}")
print(f"Variance Homogeniety Test p-value: {levene_test.pvalue}")

if p_value < 0.05:
    print("Result: H0 could be rejected, there's a meaningful difference between control group and test group.")
else:
    print("Result: H0 couldn't be rejected , there's not a meaningful difference between control group and test group.")