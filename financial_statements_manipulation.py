# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 00:16:43 2023

@author: YAPHENGTEH
"""

import pandas as pd
import os

os.chdir(r'C:\Users\yaphengteh\OneDrive')
financial = pd.read_excel('financial_statements.xlsx', sheet_name='Export Worksheet')

# remove rows with future years and find out most app_num have how many years of records
# df_count = data_raw.dropna(subset=['FI_APP_NUM'])
# df_count.drop(df_count[df_count['YEAR'] > 2023].index, inplace=True)
# df_check = df_count.groupby(['FI_APP_NUM'])['FI_APP_NUM'].count()
# df_check.to_excel('df_check.xlsx')

os.chdir(r'C:\Users\yaphengteh\OneDrive')
main = pd.read_excel('merged_main_data.xlsx', sheet_name='Post-removal')
main.drop('Unnamed: 0', axis=1, inplace=True)
main.dropna(subset=['APPLICATION_NUMBER'], inplace=True)
main['FI_NEED_MERIT'].replace('NEEDS', 'DEVELOPMENTAL', inplace=True)
main['FI_NEED_MERIT'].replace('MERITS', 'COMMERCIAL', inplace=True)

app_date = main.get(['APPLICATION_NUMBER','FI_APP_DATE'])
df1 = pd.merge(financial, app_date, how='left', left_on='FI_APP_NUM', right_on='APPLICATION_NUMBER')

# remove financial year more than or same as application year
df1['FI_APP_DATE'] = pd.to_datetime(df1['FI_APP_DATE'], errors='coerce', dayfirst=True)
df1['FI_APP_YEAR'] = df1['FI_APP_DATE'].dt.year
df1['DELTA'] = df1['FI_APP_YEAR'] - df1['YEAR']
df2 = df1[df1['DELTA'] > 0]
df2.reset_index(drop=True, inplace=True)

# remove rows with missing FI_APP_NUM and rows with future years
ms_app_num = df2[df2['FI_APP_NUM'].isna()]
df2.dropna(subset=['FI_APP_NUM'], inplace=True)
df2.drop(df2[df2['YEAR'] > 2023].index, inplace=True)

# drop repeated columns
df2.drop('Gross_Cash_from_Operation_1', axis=1, inplace=True)
df2.drop('FID_AUDITOR_QUAL_1', axis=1, inplace=True)

# sort rows by FI_APP_NUM and YEAR
df2.sort_values(by=['FI_APP_NUM','DELTA'], ascending=True, inplace=True)
df2.reset_index(drop=True, inplace=True)

# tag year as t, t-1, t-2, t-3, t-4, t-5
num_lst = []
y_lst = []
for num in df2['FI_APP_NUM']:
    if num not in num_lst:
        y_lst.append('T')
        num_lst.append(num)
    elif num_lst.count(num) == 1:
        y_lst.append('T-1')
        num_lst.append(num)
    elif num_lst.count(num) == 2:
        y_lst.append('T-2')
        num_lst.append(num)
    elif num_lst.count(num) == 3:
        y_lst.append('T-3')
        num_lst.append(num)
    elif num_lst.count(num) == 4:
        y_lst.append('T-4')
        num_lst.append(num)
    elif num_lst.count(num) == 5:
        y_lst.append('T-5')
        num_lst.append(num)
    else:
        y_lst.append(None)
        num_lst.append(None)
        
df2['Year_Tag'] = y_lst

# remove financial statement that more than 6 years
df2.dropna(subset=['Year_Tag'], inplace=True)

# remove main dataset and additional columns
df2.drop(['YEAR','APPLICATION_NUMBER','FI_APP_DATE','FI_APP_YEAR','DELTA'], axis=1, inplace=True)

# pivot and export
pv_data = df2.pivot(index=['FI_CLIENT_NUM', 'FI_APP_NUM'], columns='Year_Tag')
pv_data.columns = [c[0] + '_' + str(c[1]) for c in pv_data.columns]
pv_data.reset_index(inplace=True)
os.chdir(r'C:\Users\yaphengteh\OneDrive')
pv_data.to_excel('pivot_financial_statements.xlsx', index=False)
