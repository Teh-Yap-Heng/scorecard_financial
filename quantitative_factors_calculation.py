# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 00:55:32 2023

@author: YAPHENGTEH
"""

import pandas as pd
import os

os.chdir(r'C:\Users\yaphengteh\OneDrive')
data = pd.read_excel('pivot_financial_statements.xlsx', sheet_name='Sheet1')

tag_lst = ['_T','_T-1','_T-2','_T-3','_T-4','_T-5']

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_ASSET' + tag] < 0:
            frame.append(row['TOTAL_ASSET' + tag])
        elif pd.isnull(row['TOTAL_ASSET' + tag]) and pd.notnull(row['FI_CURRENT_ASSET' + tag]) and pd.notnull(row['FI_FIXED_ASSET' + tag]):
            frame.append(row['FI_CURRENT_ASSET' + tag] + row['FI_FIXED_ASSET' + tag])
        elif pd.isnull(row['TOTAL_ASSET' + tag]) and pd.notnull(row['FI_CURRENT_ASSET' + tag]) and pd.isnull(row['FI_FIXED_ASSET' + tag]):
            frame.append(row['FI_CURRENT_ASSET' + tag])
        elif pd.isnull(row['TOTAL_ASSET' + tag]) and pd.notnull(row['FI_CURRENT_ASSET' + tag]) and pd.isnull(row['FI_FIXED_ASSET' + tag]):
            frame.append(row['FI_FIXED_ASSET_T'])
        elif pd.isnull(row['TOTAL_ASSET' + tag]) and pd.notnull(row['FI_TOTAL_LIABILITY' + tag]):
            frame.append(0)
        else:
            frame.append(row['TOTAL_ASSET' + tag])
    data['TOTAL_ASSET2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_CURRENT_ASSET' + tag] < 0:
            frame.append(None)
        elif pd.isnull(row['FI_CURRENT_ASSET' + tag]) and pd.notnull(row['TOTAL_ASSET' + tag]) and pd.notnull(row['FI_FIXED_ASSET' + tag]):
            frame.append(row['TOTAL_ASSET' + tag] - row['FI_FIXED_ASSET' + tag])    
        elif pd.isnull(row['FI_CURRENT_ASSET' + tag]) and pd.notnull(row['TOTAL_ASSET' + tag]) and pd.isnull(row['FI_FIXED_ASSET' + tag]):
            frame.append(row['TOTAL_ASSET2' + tag])
        elif pd.isnull(row['FI_CURRENT_ASSET' + tag]) and pd.isnull(row['TOTAL_ASSET' + tag]) and pd.notnull(row['FI_FIXED_ASSET' + tag]):
            frame.append(0)
        elif pd.isnull(row['FI_CURRENT_ASSET' + tag]) and pd.notnull(row['FI_CURRENT_LIABILITY' + tag]):
            frame.append(0)     
        else:
            frame.append(row['FI_CURRENT_ASSET' + tag])
    data['CURRENT_ASSET2' + tag] = pd.DataFrame(frame)
    
frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_TOTAL_LIABILITY' + tag] < 0:
            frame.append(None)
        elif pd.isnull(row['FI_TOTAL_LIABILITY' + tag]) and pd.notnull(row['FI_CURRENT_LIABILITY' + tag]):
            frame.append(row['FI_CURRENT_LIABILITY' + tag]) 
        elif pd.isnull(row['FI_TOTAL_LIABILITY' + tag]) and pd.notnull(row['TOTAL_ASSET' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_TOTAL_LIABILITY' + tag])   
    data['TOTAL_LIABILITY2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_CURRENT_LIABILITY' + tag] < 0:
            frame.append(None)
        elif pd.isnull(row['FI_CURRENT_LIABILITY' + tag]) and pd.notnull(row['FI_TOTAL_LIABILITY' + tag]):
            frame.append(row['TOTAL_LIABILITY2' + tag])
        elif pd.isnull(row['FI_CURRENT_LIABILITY' + tag]) and pd.notnull(row['FI_CURRENT_ASSET' + tag]):
            frame.append(0)
        elif pd.isnull(row['FI_CURRENT_LIABILITY' + tag]) and pd.notnull(row['FI_CASH' + tag]):
            frame.append(0)  
        else:
            frame.append(row['FI_CURRENT_LIABILITY' + tag])  
    data['CURRENT_LIABILITY2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if pd.isnull(row['FI_REVENUE' + tag]) and pd.notnull(row['SALES' + tag]):
            frame.append(row['SALES' + tag])
        elif pd.isnull(row['FI_REVENUE' + tag]) and pd.notnull(row['FI_COGS' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_REVENUE' + tag])
    data['REVENUE2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if pd.isnull(row['FI_COGS' + tag]) and pd.notnull(row['FI_REVENUE' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_COGS' + tag])
    data['COGS2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if pd.isnull(row['FI_PAT' + tag]) and pd.notnull(row['FI_TAX' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_PAT' + tag])
    data['PAT2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if pd.isnull(row['FI_TAX' + tag]) and pd.notnull(row['FI_PAT' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_TAX' + tag])
    data['TAX2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if pd.isnull(row['FI_ EBITDA' + tag]) and pd.notnull(row['FI_DEPRECIATION' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_ EBITDA' + tag])
    data['EBITA2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if pd.isnull(row['FI_DEPRECIATION' + tag]) and pd.notnull(row['FI_ EBITDA' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_DEPRECIATION' + tag])       
    data['DEPRECIATION2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_FIXED_ASSET' + tag] < 0:
            frame.append(None)
        elif pd.isnull(row['FI_FIXED_ASSET' + tag]) and pd.notnull(row['FI_CURRENT_ASSET' + tag]) and pd.notnull(row['TOTAL_ASSET' + tag]):
            frame.append(row['TOTAL_ASSET2' + tag] - row['CURRENT_ASSET2' + tag])            
        elif pd.isnull(row['FI_FIXED_ASSET' + tag]) and pd.notnull(row['FI_CURRENT_ASSET' + tag]) and pd.isnull(row['TOTAL_ASSET' + tag]):
            frame.append(0)
        elif pd.isnull(row['FI_FIXED_ASSET' + tag]) and pd.isnull(row['FI_CURRENT_ASSET' + tag]) and pd.notnull(row['TOTAL_ASSET' + tag]):
            frame.append(row['TOTAL_ASSET2' + tag])  
        else:
            frame.append(row['FI_FIXED_ASSET' + tag])
    data['FIXED_ASSET2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_CASH' + tag] < 0:
            frame.append(None)
        elif pd.isnull(row['FI_CASH' + tag]) and pd.notnull(row['FI_CURRENT_ASSET' + tag]):
            frame.append(row['CURRENT_ASSET2' + tag])
        elif pd.isnull(row['FI_CASH' + tag]) and pd.notnull(row['FI_ACCOUNTS_RECEIVABLES' + tag]):
            frame.append(0)
        elif pd.isnull(row['FI_CASH' + tag]) and pd.notnull(row['FI_CURRENT_LIABILITY' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_CASH' + tag])
    data['CASH2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_ACCOUNTS_RECEIVABLES' + tag] < 0:
            frame.append(None)
        elif pd.isnull(row['FI_ACCOUNTS_RECEIVABLES' + tag]) and pd.notnull(row['FI_CASH' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_ACCOUNTS_RECEIVABLES' + tag])
    data['TRADE_DEBTOR2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if pd.isnull(row['FI_INVENTORIES' + tag]) and pd.notnull(row['FI_CASH' + tag]):
            frame.append(0)
        elif pd.isnull(row['FI_INVENTORIES' + tag]) and pd.notnull(row['FI_ACCOUNTS_RECEIVABLES' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_INVENTORIES' + tag])
    data['INVENTORIES2' + tag] = pd.DataFrame(frame)

yoysales1 = []
for index, row in data.iterrows():
    if pd.isnull(row['SALES_T-1']) or row['SALES_T-1'] == 0:
        yoysales1.append(0)
    else: 
        yoysales1.append((row['SALES_T'] - row['SALES_T-1']) / row['SALES_T-1'])
    
yoysales2 = []
for index, row in data.iterrows():
    if pd.isnull(row['SALES_T-2']) or row['SALES_T-2'] == 0:
        yoysales2.append(0)
    else: 
        yoysales2.append((row['SALES_T-1'] - row['SALES_T-2']) / row['SALES_T-2'])
        
yoysales3 = []
for index, row in data.iterrows():
    if pd.isnull(row['SALES_T-3']) or row['SALES_T-3'] == 0:
        yoysales3.append(0)
    else: 
        yoysales3.append((row['SALES_T-2'] - row['SALES_T-3']) / row['SALES_T-3'])

yoysales4 = []
for index, row in data.iterrows():
    if pd.isnull(row['SALES_T-4']) or row['SALES_T-4'] == 0:
        yoysales4.append(0)
    else: 
        yoysales4.append((row['SALES_T-3'] - row['SALES_T-4']) / row['SALES_T-4'])

yoysales5 = []
for index, row in data.iterrows():
    if pd.isnull(row['SALES_T-5']) or row['SALES_T-5'] == 0:
        yoysales5.append(0)
    else: 
        yoysales5.append((row['SALES_T-4'] - row['SALES_T-5']) / row['SALES_T-5'])

data['YOYSALES1'] = pd.DataFrame(yoysales1)
data['YOYSALES2'] = pd.DataFrame(yoysales2)
data['YOYSALES3'] = pd.DataFrame(yoysales3)
data['YOYSALES4'] = pd.DataFrame(yoysales4)
data['YOYSALES5'] = pd.DataFrame(yoysales5)

average_sales_growth = []
for index, row in data.iterrows():
    if pd.notnull(row['YOYSALES1']) and pd.notnull(row['YOYSALES2']):
        average_sales_growth.append((row['YOYSALES1'] + row['YOYSALES2']) / 2)
    elif pd.notnull(row['YOYSALES1']) and pd.isnull(row['YOYSALES2']):
        average_sales_growth.append(row['YOYSALES1'])
    else:
        average_sales_growth.append(None)     
data['AVERAGE_SALES_GROWTH'] = pd.DataFrame(average_sales_growth)

average_sales_growth_V2 = []
for index, row in data.iterrows():
    if pd.notnull(row['YOYSALES1']) and pd.notnull(row['YOYSALES2']) and pd.notnull(row['YOYSALES3']) and pd.notnull(row['YOYSALES4']) and pd.notnull(row['YOYSALES5']):
        average_sales_growth_V2.append((row['YOYSALES1'] + row['YOYSALES2'] + row['YOYSALES3'] + row['YOYSALES4'] + row['YOYSALES5']) / 5)
    elif pd.notnull(row['YOYSALES1']) and pd.notnull(row['YOYSALES2']) and pd.notnull(row['YOYSALES3']) and pd.notnull(row['YOYSALES4']) and pd.isnull(row['YOYSALES5']):
        average_sales_growth_V2.append((row['YOYSALES1'] + row['YOYSALES2'] + row['YOYSALES3'] + row['YOYSALES4']) / 4)
    elif pd.notnull(row['YOYSALES1']) and pd.notnull(row['YOYSALES2']) and pd.notnull(row['YOYSALES3']) and pd.isnull(row['YOYSALES4']) and pd.isnull(row['YOYSALES5']):
        average_sales_growth_V2.append((row['YOYSALES1'] + row['YOYSALES2'] + row['YOYSALES3']) / 3)
    elif pd.notnull(row['YOYSALES1']) and pd.notnull(row['YOYSALES2']) and pd.isnull(row['YOYSALES3']) and pd.isnull(row['YOYSALES4']) and pd.isnull(row['YOYSALES5']):
        average_sales_growth_V2.append((row['YOYSALES1'] + row['YOYSALES2']) / 2)
    elif pd.notnull(row['YOYSALES1']) and pd.isnull(row['YOYSALES2']) and pd.isnull(row['YOYSALES3']) and pd.isnull(row['YOYSALES4']) and pd.isnull(row['YOYSALES5']):
        average_sales_growth_V2.append(row['YOYSALES1'])
    else:
        average_sales_growth_V2.append(None)     
data['AVERAGE_SALES_GROWTH_V2'] = pd.DataFrame(average_sales_growth_V2)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_LONG_TERM_DEBT' + tag] < 0:
            frame.append(None)
        elif pd.isnull(row['FI_LONG_TERM_DEBT' + tag]) and pd.notnull(row['FI_SHORT_TERM_BORROWING' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_LONG_TERM_DEBT' + tag])
    data['LONG_DEBT2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_SHORT_TERM_BORROWING' + tag] < 0:
            frame.append(None)
        elif pd.isnull(row['FI_SHORT_TERM_BORROWING' + tag]) and pd.notnull(row['FI_LONG_TERM_DEBT' + tag]):
            frame.append(0)
        elif pd.isnull(row['FI_SHORT_TERM_BORROWING' + tag]) and pd.notnull(row['FI_INTEREST_EXPENSE' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_SHORT_TERM_BORROWING' + tag])
    data['SHORT_DEBT2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if pd.isnull(row['FI_INTEREST_EXPENSE' + tag]) and pd.notnull(row['FI_SHORT_TERM_BORROWING' + tag]):
            frame.append(0)
        else:
            frame.append(row['FI_INTEREST_EXPENSE' + tag])        
    data['INTEREST2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_SHAREHOLDER_FUND' + tag] < 0:
            frame.append(None)
        else:
            frame.append(row['TOTAL_SHAREHOLDER_FUND' + tag])
    data['SHAREHOLDER2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_ACCOUNT_RECEIVABLE_TURNOVER' + tag] < 0:
            frame.append(None)
        else:
            frame.append(row['FI_ACCOUNT_RECEIVABLE_TURNOVER' + tag])
    data['RECEIVABLE_PERIOD2' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['TOTAL_ASSET2' + tag] - row['CURRENT_ASSET2' + tag])
    data['NONCURRENT_ASSET' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['TOTAL_LIABILITY2' + tag] - row['CURRENT_LIABILITY2' + tag])
    data['NONCURRENT_LIABILITY' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['REVENUE2' + tag] - row['COGS2' + tag])
    data['GROSSPROFITS' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['PAT2' + tag] - row['TAX2' + tag])
    data['PRETAX_PROFIT' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['EBITA2' + tag] + row['DEPRECIATION2' + tag])
    data['EBITDA' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['CURRENT_ASSET2' + tag] + row['FIXED_ASSET2' + tag] - row['TOTAL_LIABILITY2' + tag])
    data['TANGIBLE_NETWORTH' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['CASH2' + tag] + row['TRADE_DEBTOR2' + tag])
    data['CASH_TRADEDEBTORS' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['CURRENT_LIABILITY2' + tag] - row['CASH2' + tag])
    data['CURRENTLIABILITY_BALANCE' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['CURRENT_ASSET2' + tag] - row['CURRENT_LIABILITY2' + tag])
    data['NET_CURRENTASSETS' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['CASH2' + tag] + row['TRADE_DEBTOR2' + tag] + row['INVENTORIES2' + tag])
    data['CASH_TRADEDEBTORS_INVENTORIES' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['TRADE_DEBTOR2' + tag] + row['INVENTORIES2' + tag])
    data['TRADEDEBTORS_INVENTORIES' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['LONG_DEBT2' + tag] + row['SHORT_DEBT2' + tag])
    data['TOTAL_DEBT' + tag] = pd.DataFrame(frame)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        frame.append(row['INTEREST2' + tag] + row['SHORT_DEBT2' + tag])
    data['INTEREST_SHORT' + tag] = pd.DataFrame(frame)

data['Financial_FSC1'] = (pd.concat([data['REVENUE2_T'], 
                                      data['REVENUE2_T-1'], 
                                      data['REVENUE2_T-2']], axis=1)).mean(axis=1)
data['Financial_FSC1_V2'] = data[['REVENUE2_T','REVENUE2_T-1',
                                  'REVENUE2_T-2','REVENUE2_T-3',
                                  'REVENUE2_T-4','REVENUE2_T-5']].mean(axis=1)

data['Financial_FSC2'] = (pd.concat([data['EBITA2_T'], 
                                      data['EBITA2_T-1'], 
                                      data['EBITA2_T-2']], axis=1)).mean(axis=1)
data['Financial_FSC2_V2'] = data[['EBITA2_T','EBITA2_T-1',
                                  'EBITA2_T-2','EBITA2_T-3',
                                  'EBITA2_T-4','EBITA2_T-5']].mean(axis=1)

data['Financial_FSC3'] = (pd.concat([data['TOTAL_ASSET2_T'], 
                                      data['TOTAL_ASSET2_T-1'], 
                                      data['TOTAL_ASSET2_T-2']], axis=1)).mean(axis=1)
data['Financial_FSC3_V2'] = data[['TOTAL_ASSET2_T','TOTAL_ASSET2_T-1',
                                  'TOTAL_ASSET2_T-2','TOTAL_ASSET2_T-3',
                                  'TOTAL_ASSET2_T-4','TOTAL_ASSET2_T-5']].mean(axis=1)

data['Financial_FSC4'] = (pd.concat([data['CURRENT_ASSET2_T'], 
                                      data['CURRENT_ASSET2_T-1'], 
                                      data['CURRENT_ASSET2_T-2']], axis=1)).mean(axis=1)
data['Financial_FSC4_V2'] = data[['CURRENT_ASSET2_T','CURRENT_ASSET2_T-1',
                                  'CURRENT_ASSET2_T-2','CURRENT_ASSET2_T-3',
                                  'CURRENT_ASSET2_T-4','CURRENT_ASSET2_T-5']].mean(axis=1)

data['Financial_FSC5'] = (pd.concat([data['NONCURRENT_ASSET_T'], 
                                      data['NONCURRENT_ASSET_T-1'], 
                                      data['NONCURRENT_ASSET_T-2']], axis=1)).mean(axis=1)
data['Financial_FSC5_V2'] = data[['NONCURRENT_ASSET_T','NONCURRENT_ASSET_T-1',
                                  'NONCURRENT_ASSET_T-2','NONCURRENT_ASSET_T-3',
                                  'NONCURRENT_ASSET_T-4','NONCURRENT_ASSET_T-5']].mean(axis=1)

data['Financial_FSC6'] = (pd.concat([data['FIXED_ASSET2_T'], 
                                      data['FIXED_ASSET2_T-1'], 
                                      data['FIXED_ASSET2_T-2']], axis=1)).mean(axis=1)
data['Financial_FSC6_V2'] = data[['FIXED_ASSET2_T','FIXED_ASSET2_T-1',
                                  'FIXED_ASSET2_T-2','FIXED_ASSET2_T-3',
                                  'FIXED_ASSET2_T-4','FIXED_ASSET2_T-5']].mean(axis=1)

data['Financial_FSC7'] = (pd.concat([data['FI_OWNERS_EQUITY_T'], 
                                      data['FI_OWNERS_EQUITY_T-1'], 
                                      data['FI_OWNERS_EQUITY_T-2']], axis=1)).mean(axis=1)
data['Financial_FSC7_V2'] = data[['FI_OWNERS_EQUITY_T','FI_OWNERS_EQUITY_T-1',
                                  'FI_OWNERS_EQUITY_T-2','FI_OWNERS_EQUITY_T-3',
                                  'FI_OWNERS_EQUITY_T-4','FI_OWNERS_EQUITY_T-5']].mean(axis=1)

data['Financial_FSC8'] = (pd.concat([data['SALES_T'], 
                                      data['SALES_T-1'], 
                                      data['SALES_T-2']], axis=1)).mean(axis=1)
data['Financial_FSC8_V2'] = data[['SALES_T','SALES_T-1',
                                  'SALES_T-2','SALES_T-3',
                                  'SALES_T-4','SALES_T-5']].mean(axis=1)

data['Financial_FSC9'] = (pd.concat([data['PAT2_T'], 
                                      data['PAT2_T-1'], 
                                      data['PAT2_T-2']], axis=1)).mean(axis=1)
data['Financial_FSC9_V2'] = data[['PAT2_T','PAT2_T-1',
                                  'PAT2_T-2','PAT2_T-3',
                                  'PAT2_T-4','PAT2_T-5']].mean(axis=1)

data['Financial_FSC10'] = (pd.concat([data['NONCURRENT_LIABILITY_T'], 
                                      data['NONCURRENT_LIABILITY_T-1'], 
                                      data['NONCURRENT_LIABILITY_T-2']], axis=1)).mean(axis=1)
data['Financial_FSC10_V2'] = data[['NONCURRENT_LIABILITY_T','NONCURRENT_LIABILITY_T-1',
                                   'NONCURRENT_LIABILITY_T-2','NONCURRENT_LIABILITY_T-3',
                                   'NONCURRENT_LIABILITY_T-4','NONCURRENT_LIABILITY_T-5']].mean(axis=1)

data['Financial_FSC11'] = (pd.concat([data['CURRENT_LIABILITY2_T'], 
                                      data['CURRENT_LIABILITY2_T-1'], 
                                      data['CURRENT_LIABILITY2_T-2']], axis=1)).mean(axis=1)
data['Financial_FSC11_V2'] = data[['CURRENT_LIABILITY2_T','CURRENT_LIABILITY2_T-1',
                                   'CURRENT_LIABILITY2_T-2','CURRENT_LIABILITY2_T-3',
                                   'CURRENT_LIABILITY2_T-4','CURRENT_LIABILITY2_T-5']].mean(axis=1)

data['Financial_FSC12'] = (pd.concat([data['TOTAL_LIABILITY2_T'], 
                                      data['TOTAL_LIABILITY2_T-1'], 
                                      data['TOTAL_LIABILITY2_T-2']], axis=1)).mean(axis=1)
data['Financial_FSC12_V2'] = data[['TOTAL_LIABILITY2_T','TOTAL_LIABILITY2_T-1',
                                   'TOTAL_LIABILITY2_T-2','TOTAL_LIABILITY2_T-3',
                                   'TOTAL_LIABILITY2_T-4','TOTAL_LIABILITY2_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['SALES' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['GROSSPROFITS' + tag] / row['SALES' + tag])
    data['Financial_FP1_1' + tag] = pd.DataFrame(frame)

data['Financial_FP1_1'] = data[['Financial_FP1_1_T','Financial_FP1_1_T-1','Financial_FP1_1_T-2']].mean(axis=1)

data['Financial_FP1_1_V2'] = data[['Financial_FP1_1_T','Financial_FP1_1_T-1','Financial_FP1_1_T-2',
                                   'Financial_FP1_1_T-3','Financial_FP1_1_T-4','Financial_FP1_1_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['REVENUE2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['GROSSPROFITS' + tag] / row['REVENUE2' + tag])
    data['Financial_FP1_2' + tag] = pd.DataFrame(frame)

data['Financial_FP1_2'] = data[['Financial_FP1_2_T','Financial_FP1_2_T-1','Financial_FP1_2_T-2']].mean(axis=1)

data['Financial_FP1_2_V2'] = data[['Financial_FP1_2_T','Financial_FP1_2_T-1','Financial_FP1_2_T-2',
                                   'Financial_FP1_2_T-3','Financial_FP1_2_T-4','Financial_FP1_2_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['SALES' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['PRETAX_PROFIT' + tag] / row['SALES' + tag])
    data['Financial_FP2_1' + tag] = pd.DataFrame(frame)

data['Financial_FP2_1'] = data[['Financial_FP2_1_T','Financial_FP2_1_T-1','Financial_FP2_1_T-2']].mean(axis=1)

data['Financial_FP2_1_V2'] = data[['Financial_FP2_1_T','Financial_FP2_1_T-1','Financial_FP2_1_T-2',
                                   'Financial_FP2_1_T-3','Financial_FP2_1_T-4','Financial_FP2_1_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['REVENUE2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['PRETAX_PROFIT' + tag] / row['REVENUE2' + tag])
    data['Financial_FP2_2' + tag] = pd.DataFrame(frame)
    
data['Financial_FP2_2'] = data[['Financial_FP2_2_T','Financial_FP2_2_T-1','Financial_FP2_2_T-2']].mean(axis=1)

data['Financial_FP2_2_V2'] = data[['Financial_FP2_2_T','Financial_FP2_2_T-1','Financial_FP2_2_T-2',
                                   'Financial_FP2_2_T-3','Financial_FP2_2_T-4','Financial_FP2_2_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_CAPITAL_EMPLOYED' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['PAT2' + tag] / row['FI_CAPITAL_EMPLOYED' + tag])
    data['Financial_FP3' + tag] = pd.DataFrame(frame)
    
data['Financial_FP3'] = data[['Financial_FP3_T','Financial_FP3_T-1','Financial_FP3_T-2']].mean(axis=1)

data['Financial_FP3_V2'] = data[['Financial_FP3_T','Financial_FP3_T-1','Financial_FP3_T-2',
                                 'Financial_FP3_T-3','Financial_FP3_T-4','Financial_FP3_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['GROSSPROFITS' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['EBITDA' + tag] / row['GROSSPROFITS' + tag])
    data['Financial_FP4' + tag] = pd.DataFrame(frame)

data['Financial_FP4'] = data[['Financial_FP4_T','Financial_FP4_T-1','Financial_FP4_T-2']].mean(axis=1)

data['Financial_FP4_V2'] = data[['Financial_FP4_T','Financial_FP4_T-1','Financial_FP4_T-2',
                                 'Financial_FP4_T-3','Financial_FP4_T-4','Financial_FP4_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['GROSSPROFITS' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['EBITA2' + tag] / row['GROSSPROFITS' + tag])
    data['Financial_FP5' + tag] = pd.DataFrame(frame)

data['Financial_FP5'] = data[['Financial_FP5_T','Financial_FP5_T-1','Financial_FP5_T-2']].mean(axis=1)

data['Financial_FP5_V2'] = data[['Financial_FP5_T','Financial_FP5_T-1','Financial_FP5_T-2',
                                 'Financial_FP5_T-3','Financial_FP5_T-4','Financial_FP5_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_ASSET2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['PRETAX_PROFIT' + tag] / row['TOTAL_ASSET2' + tag])
    data['Financial_FP6' + tag] = pd.DataFrame(frame)

data['Financial_FP6'] = data[['Financial_FP6_T','Financial_FP6_T-1','Financial_FP6_T-2']].mean(axis=1)

data['Financial_FP6_V2'] = data[['Financial_FP6_T','Financial_FP6_T-1','Financial_FP6_T-2',
                                 'Financial_FP6_T-3','Financial_FP6_T-4','Financial_FP6_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TANGIBLE_NETWORTH' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['PRETAX_PROFIT' + tag] / row['TANGIBLE_NETWORTH' + tag])
    data['Financial_FP7' + tag] = pd.DataFrame(frame)

data['Financial_FP7'] = data[['Financial_FP7_T','Financial_FP7_T-1','Financial_FP7_T-2']].mean(axis=1)

data['Financial_FP7_V2'] = data[['Financial_FP7_T','Financial_FP7_T-1','Financial_FP7_T-2',
                                 'Financial_FP7_T-3','Financial_FP7_T-4','Financial_FP7_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_RETAINED_EARNINGS' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['PRETAX_PROFIT' + tag] / row['FI_RETAINED_EARNINGS' + tag])
    data['Financial_FP8' + tag] = pd.DataFrame(frame)
    
data['Financial_FP8'] = data[['Financial_FP8_T','Financial_FP8_T-1','Financial_FP8_T-2']].mean(axis=1)

data['Financial_FP8_V2'] = data[['Financial_FP8_T','Financial_FP8_T-1','Financial_FP8_T-2',
                                 'Financial_FP8_T-3','Financial_FP8_T-4','Financial_FP8_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_ASSET2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['PAT2' + tag] / row['TOTAL_ASSET2' + tag])
    data['Financial_FP9' + tag] = pd.DataFrame(frame)

data['Financial_FP9'] = data[['Financial_FP9_T','Financial_FP9_T-1','Financial_FP9_T-2']].mean(axis=1)

data['Financial_FP9_V2'] = data[['Financial_FP9_T','Financial_FP9_T-1','Financial_FP9_T-2',
                                 'Financial_FP9_T-3','Financial_FP9_T-4','Financial_FP9_T-5']].mean(axis=1)


frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TANGIBLE_NETWORTH' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['PAT2' + tag] / row['TANGIBLE_NETWORTH' + tag])
    data['Financial_FP10' + tag] = pd.DataFrame(frame)

data['Financial_FP10'] = data[['Financial_FP10_T','Financial_FP10_T-1','Financial_FP10_T-2']].mean(axis=1)

data['Financial_FP10_V2'] = data[['Financial_FP10_T','Financial_FP10_T-1','Financial_FP10_T-2',
                                  'Financial_FP10_T-3','Financial_FP10_T-4','Financial_FP10_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_RETAINED_EARNINGS' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['PAT2' + tag] / row['FI_RETAINED_EARNINGS' + tag])
    data['Financial_FP11' + tag] = pd.DataFrame(frame)

data['Financial_FP11'] = data[['Financial_FP11_T','Financial_FP11_T-1','Financial_FP11_T-2']].mean(axis=1)

data['Financial_FP11_V2'] = data[['Financial_FP11_T','Financial_FP11_T-1','Financial_FP11_T-2',
                                  'Financial_FP11_T-3','Financial_FP11_T-4','Financial_FP11_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_OWNERS_EQUITY' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['PRETAX_PROFIT' + tag] / row['FI_OWNERS_EQUITY' + tag])
    data['Financial_FP12' + tag] = pd.DataFrame(frame)

data['Financial_FP12'] = data[['Financial_FP12_T','Financial_FP12_T-1','Financial_FP12_T-2']].mean(axis=1)

data['Financial_FP12_V2'] = data[['Financial_FP12_T','Financial_FP12_T-1','Financial_FP12_T-2',
                                  'Financial_FP12_T-3','Financial_FP12_T-4','Financial_FP12_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_OWNERS_EQUITY' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['PAT2' + tag] / row['FI_OWNERS_EQUITY' + tag])
    data['Financial_FP13' + tag] = pd.DataFrame(frame)

data['Financial_FP13'] = data[['Financial_FP13_T','Financial_FP13_T-1','Financial_FP13_T-2']].mean(axis=1)

data['Financial_FP13_V2'] = data[['Financial_FP13_T','Financial_FP13_T-1','Financial_FP13_T-2',
                                  'Financial_FP13_T-3','Financial_FP13_T-4','Financial_FP13_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TANGIBLE_NETWORTH' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['EBITA2' + tag] / row['TANGIBLE_NETWORTH' + tag])
    data['Financial_FP14' + tag] = pd.DataFrame(frame)

data['Financial_FP14'] = data[['Financial_FP14_T','Financial_FP14_T-1','Financial_FP14_T-2']].mean(axis=1)

data['Financial_FP14_V2'] = data[['Financial_FP14_T','Financial_FP14_T-1','Financial_FP14_T-2',
                                  'Financial_FP14_T-3','Financial_FP14_T-4','Financial_FP14_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_RETAINED_EARNINGS' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['EBITA2' + tag] / row['FI_RETAINED_EARNINGS' + tag])
    data['Financial_FP15' + tag] = pd.DataFrame(frame)

data['Financial_FP15'] = data[['Financial_FP15_T','Financial_FP15_T-1','Financial_FP15_T-2']].mean(axis=1)

data['Financial_FP15_V2'] = data[['Financial_FP15_T','Financial_FP15_T-1','Financial_FP15_T-2',
                                  'Financial_FP15_T-3','Financial_FP15_T-4','Financial_FP15_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['CURRENT_LIABILITY2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['CURRENT_ASSET2' + tag] / row['CURRENT_LIABILITY2' + tag])
    data['Financial_FL1' + tag] = pd.DataFrame(frame)

data['Financial_FL1'] = data[['Financial_FL1_T','Financial_FL1_T-1','Financial_FL1_T-2']].mean(axis=1)

data['Financial_FL1_V2'] = data[['Financial_FL1_T','Financial_FL1_T-1','Financial_FL1_T-2',
                                 'Financial_FL1_T-3','Financial_FL1_T-4','Financial_FL1_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['CURRENT_LIABILITY2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['CASH2' + tag] / row['CURRENT_LIABILITY2' + tag])
    data['Financial_FL2' + tag] = pd.DataFrame(frame)

data['Financial_FL2'] = data[['Financial_FL2_T','Financial_FL2_T-1','Financial_FL2_T-2']].mean(axis=1)

data['Financial_FL2_V2'] = data[['Financial_FL2_T','Financial_FL2_T-1','Financial_FL2_T-2',
                                 'Financial_FL2_T-3','Financial_FL2_T-4','Financial_FL2_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_LIABILITY2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['FI_ACCOUNTS_PAYABLE' + tag] / row['TOTAL_LIABILITY2' + tag])
    data['Financial_FL3' + tag] = pd.DataFrame(frame)

data['Financial_FL3'] = data[['Financial_FL3_T','Financial_FL3_T-1','Financial_FL3_T-2']].mean(axis=1)

data['Financial_FL3_V2'] = data[['Financial_FL3_T','Financial_FL3_T-1','Financial_FL3_T-2',
                                 'Financial_FL3_T-3','Financial_FL3_T-4','Financial_FL3_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['CURRENT_LIABILITY2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['CASH_TRADEDEBTORS' + tag] / row['CURRENT_LIABILITY2' + tag])
    data['Financial_FL4' + tag] = pd.DataFrame(frame)

data['Financial_FL4'] = data[['Financial_FL4_T','Financial_FL4_T-1','Financial_FL4_T-2']].mean(axis=1)

data['Financial_FL4_V2'] = data[['Financial_FL4_T','Financial_FL4_T-1','Financial_FL4_T-2',
                                 'Financial_FL4_T-3','Financial_FL4_T-4','Financial_FL4_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['CURRENT_LIABILITY2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['CASH2' + tag] / row['CURRENT_LIABILITY2' + tag])
    data['Financial_FL5' + tag] = pd.DataFrame(frame)

data['Financial_FL5'] = data[['Financial_FL5_T','Financial_FL5_T-1','Financial_FL5_T-2']].mean(axis=1)

data['Financial_FL5_V2'] = data[['Financial_FL5_T','Financial_FL5_T-1','Financial_FL5_T-2',
                                 'Financial_FL5_T-3','Financial_FL5_T-4','Financial_FL5_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['CURRENTLIABILITY_BALANCE' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['GROSSPROFITS' + tag] / row['CURRENTLIABILITY_BALANCE' + tag])
    data['Financial_FL6' + tag] = pd.DataFrame(frame)

data['Financial_FL6'] = data[['Financial_FL6_T','Financial_FL6_T-1','Financial_FL6_T-2']].mean(axis=1)

data['Financial_FL6_V2'] = data[['Financial_FL6_T','Financial_FL6_T-1','Financial_FL6_T-2',
                                 'Financial_FL6_T-3','Financial_FL6_T-4','Financial_FL6_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_RETAINED_EARNINGS' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['CURRENT_LIABILITY2' + tag] / row['FI_RETAINED_EARNINGS' + tag])
    data['Financial_FL7' + tag] = pd.DataFrame(frame)

data['Financial_FL7'] = data[['Financial_FL7_T','Financial_FL7_T-1','Financial_FL7_T-2']].mean(axis=1)

data['Financial_FL7_V2'] = data[['Financial_FL7_T','Financial_FL7_T-1','Financial_FL7_T-2',
                                 'Financial_FL7_T-3','Financial_FL7_T-4','Financial_FL7_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TANGIBLE_NETWORTH' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['CURRENT_LIABILITY2' + tag] / row['TANGIBLE_NETWORTH' + tag])
    data['Financial_FL8' + tag] = pd.DataFrame(frame)

data['Financial_FL8'] = data[['Financial_FL8_T','Financial_FL8_T-1','Financial_FL8_T-2']].mean(axis=1)

data['Financial_FL8_V2'] = data[['Financial_FL8_T','Financial_FL8_T-1','Financial_FL8_T-2',
                                 'Financial_FL8_T-3','Financial_FL8_T-4','Financial_FL8_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['NET_CURRENTASSETS' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['SALES' + tag] / row['NET_CURRENTASSETS' + tag])
    data['Financial_FL9' + tag] = pd.DataFrame(frame)

data['Financial_FL9'] = data[['Financial_FL9_T','Financial_FL9_T-1','Financial_FL9_T-2']].mean(axis=1)

data['Financial_FL9_V2'] = data[['Financial_FL9_T','Financial_FL9_T-1','Financial_FL9_T-2',
                                 'Financial_FL9_T-3','Financial_FL9_T-4','Financial_FL9_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['CURRENT_LIABILITY2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['CASH_TRADEDEBTORS_INVENTORIES' + tag] / row['CURRENT_LIABILITY2' + tag])
    data['Financial_FL10' + tag] = pd.DataFrame(frame)

data['Financial_FL10'] = data[['Financial_FL10_T','Financial_FL10_T-1','Financial_FL10_T-2']].mean(axis=1)

data['Financial_FL10_V2'] = data[['Financial_FL10_T','Financial_FL10_T-1','Financial_FL10_T-2',
                                  'Financial_FL10_T-3','Financial_FL10_T-4','Financial_FL10_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['CURRENTLIABILITY_BALANCE' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['SALES' + tag] / row['CURRENTLIABILITY_BALANCE' + tag])
    data['Financial_FL11' + tag] = pd.DataFrame(frame)

data['Financial_FL11'] = data[['Financial_FL11_T','Financial_FL11_T-1','Financial_FL11_T-2']].mean(axis=1)

data['Financial_FL11_V2'] = data[['Financial_FL11_T','Financial_FL11_T-1','Financial_FL11_T-2',
                                  'Financial_FL11_T-3','Financial_FL11_T-4','Financial_FL11_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['SALES' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['NET_CURRENTASSETS' + tag] / row['SALES' + tag])
    data['Financial_FL12' + tag] = pd.DataFrame(frame)

data['Financial_FL12'] = data[['Financial_FL12_T','Financial_FL12_T-1','Financial_FL12_T-2']].mean(axis=1)

data['Financial_FL12_V2'] = data[['Financial_FL12_T','Financial_FL12_T-1','Financial_FL12_T-2',
                                  'Financial_FL12_T-3','Financial_FL12_T-4','Financial_FL12_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['CURRENT_LIABILITY2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['FI_RETAINED_EARNINGS' + tag] / row['CURRENT_LIABILITY2' + tag])
    data['Financial_FL13' + tag] = pd.DataFrame(frame)

data['Financial_FL13'] = data[['Financial_FL13_T','Financial_FL13_T-1','Financial_FL13_T-2']].mean(axis=1)

data['Financial_FL13_V2'] = data[['Financial_FL13_T','Financial_FL13_T-1','Financial_FL13_T-2',
                                  'Financial_FL13_T-3','Financial_FL13_T-4','Financial_FL13_T-5']].mean(axis=1)

data['Financial_FR1'] = data['AVERAGE_SALES_GROWTH']
data['Financial_FR1_V2'] = data['AVERAGE_SALES_GROWTH_V2']

data['Financial_FR2_1'] = (data['TOTAL_ASSET2_T'] - data['TOTAL_ASSET2_T-1']) / data['TOTAL_ASSET2_T-1']
data['Financial_FR2_2'] = (data['TOTAL_ASSET2_T-1'] - data['TOTAL_ASSET2_T-2']) / data['TOTAL_ASSET2_T-2']
data['Financial_FR2_3'] = (data['TOTAL_ASSET2_T-2'] - data['TOTAL_ASSET2_T-3']) / data['TOTAL_ASSET2_T-3']
data['Financial_FR2_4'] = (data['TOTAL_ASSET2_T-3'] - data['TOTAL_ASSET2_T-4']) / data['TOTAL_ASSET2_T-4']
data['Financial_FR2_5'] = (data['TOTAL_ASSET2_T-4'] - data['TOTAL_ASSET2_T-5']) / data['TOTAL_ASSET2_T-5']

data['Financial_FR3_1'] = (data['PRETAX_PROFIT_T'] - data['PRETAX_PROFIT_T-1']) / data['PRETAX_PROFIT_T-1']
data['Financial_FR3_2'] = (data['PRETAX_PROFIT_T-1'] - data['PRETAX_PROFIT_T-2']) / data['PRETAX_PROFIT_T-2']
data['Financial_FR3_3'] = (data['PRETAX_PROFIT_T-2'] - data['PRETAX_PROFIT_T-3']) / data['PRETAX_PROFIT_T-3']
data['Financial_FR3_4'] = (data['PRETAX_PROFIT_T-3'] - data['PRETAX_PROFIT_T-4']) / data['PRETAX_PROFIT_T-4']
data['Financial_FR3_5'] = (data['PRETAX_PROFIT_T-4'] - data['PRETAX_PROFIT_T-5']) / data['PRETAX_PROFIT_T-5']

data['Financial_FR6_1'] = (data['TOTAL_LIABILITY2_T'] - data['TOTAL_LIABILITY2_T-1']) / data['TOTAL_LIABILITY2_T-1']
data['Financial_FR6_2'] = (data['TOTAL_LIABILITY2_T-1'] - data['TOTAL_LIABILITY2_T-2']) / data['TOTAL_LIABILITY2_T-2']
data['Financial_FR6_3'] = (data['TOTAL_LIABILITY2_T-2'] - data['TOTAL_LIABILITY2_T-3']) / data['TOTAL_LIABILITY2_T-3']
data['Financial_FR6_4'] = (data['TOTAL_LIABILITY2_T-3'] - data['TOTAL_LIABILITY2_T-4']) / data['TOTAL_LIABILITY2_T-4']
data['Financial_FR6_5'] = (data['TOTAL_LIABILITY2_T-4'] - data['TOTAL_LIABILITY2_T-5']) / data['TOTAL_LIABILITY2_T-5']

data['Financial_FR7_1'] = (data['FI_OWNERS_EQUITY_T'] - data['FI_OWNERS_EQUITY_T-1']) / data['FI_OWNERS_EQUITY_T-1']
data['Financial_FR7_2'] = (data['FI_OWNERS_EQUITY_T-1'] - data['FI_OWNERS_EQUITY_T-2']) / data['FI_OWNERS_EQUITY_T-2']
data['Financial_FR7_3'] = (data['FI_OWNERS_EQUITY_T-2'] - data['FI_OWNERS_EQUITY_T-3']) / data['FI_OWNERS_EQUITY_T-3']
data['Financial_FR7_4'] = (data['FI_OWNERS_EQUITY_T-3'] - data['FI_OWNERS_EQUITY_T-4']) / data['FI_OWNERS_EQUITY_T-4']
data['Financial_FR7_5'] = (data['FI_OWNERS_EQUITY_T-4'] - data['FI_OWNERS_EQUITY_T-5']) / data['FI_OWNERS_EQUITY_T-5']

data['Financial_FR11_1'] = (data['SALES_T'] - data['SALES_T-1']) / data['SALES_T-1']
data['Financial_FR11_2'] = (data['SALES_T-1'] - data['SALES_T-2']) / data['SALES_T-2']
data['Financial_FR11_3'] = (data['SALES_T-2'] - data['SALES_T-3']) / data['SALES_T-3']
data['Financial_FR11_4'] = (data['SALES_T-3'] - data['SALES_T-4']) / data['SALES_T-4']
data['Financial_FR11_5'] = (data['SALES_T-4'] - data['SALES_T-5']) / data['SALES_T-5']

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['SHAREHOLDER2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['TOTAL_DEBT' + tag] / row['SHAREHOLDER2' + tag])
    data['Financial_FG1' + tag] = pd.DataFrame(frame)

data['Financial_FG1'] = data[['Financial_FG1_T','Financial_FG1_T-1','Financial_FG1_T-2']].mean(axis=1)

data['Financial_FG1_V2'] = data[['Financial_FG1_T','Financial_FG1_T-1','Financial_FG1_T-2',
                                 'Financial_FG1_T-3','Financial_FG1_T-4','Financial_FG1_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TANGIBLE_NETWORTH' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['FI_TOTAL_LOANS_FROM_BANK' + tag] / row['TANGIBLE_NETWORTH' + tag])
    data['Financial_FG2' + tag] = pd.DataFrame(frame)

data['Financial_FG2'] = data[['Financial_FG2_T','Financial_FG2_T-1','Financial_FG2_T-2']].mean(axis=1)

data['Financial_FG2_V2'] = data[['Financial_FG2_T','Financial_FG2_T-1','Financial_FG2_T-2',
                                 'Financial_FG2_T-3','Financial_FG2_T-4','Financial_FG2_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_ASSET2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['FI_TOTAL_LOANS_FROM_BANK' + tag] / row['TOTAL_ASSET2' + tag])
    data['Financial_FG3' + tag] = pd.DataFrame(frame)

data['Financial_FG3'] = data[['Financial_FG3_T','Financial_FG3_T-1','Financial_FG3_T-2']].mean(axis=1)

data['Financial_FG3_V2'] = data[['Financial_FG3_T','Financial_FG3_T-1','Financial_FG3_T-2',
                                 'Financial_FG3_T-3','Financial_FG3_T-4','Financial_FG3_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['EBITDA' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['TOTAL_DEBT' + tag] / row['EBITDA' + tag])
    data['Financial_FG4' + tag] = pd.DataFrame(frame)

data['Financial_FG4'] = data[['Financial_FG4_T','Financial_FG4_T-1','Financial_FG4_T-2']].mean(axis=1)

data['Financial_FG4_V2'] = data[['Financial_FG4_T','Financial_FG4_T-1','Financial_FG4_T-2',
                                 'Financial_FG4_T-3','Financial_FG4_T-4','Financial_FG4_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_TOTAL_LOANS_FROM_BANK' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['TANGIBLE_NETWORTH' + tag] / row['FI_TOTAL_LOANS_FROM_BANK' + tag])
    data['Financial_FG5' + tag] = pd.DataFrame(frame)

data['Financial_FG5'] = data[['Financial_FG5_T','Financial_FG5_T-1','Financial_FG5_T-2']].mean(axis=1)

data['Financial_FG5_V2'] = data[['Financial_FG5_T','Financial_FG5_T-1','Financial_FG5_T-2',
                                 'Financial_FG5_T-3','Financial_FG5_T-4','Financial_FG5_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_ASSET2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['FI_RETAINED_EARNINGS' + tag] / row['TOTAL_ASSET2' + tag])
    data['Financial_FG6' + tag] = pd.DataFrame(frame)

data['Financial_FG6'] = data[['Financial_FG6_T','Financial_FG6_T-1','Financial_FG6_T-2']].mean(axis=1)

data['Financial_FG6_V2'] = data[['Financial_FG6_T','Financial_FG6_T-1','Financial_FG6_T-2',
                                 'Financial_FG6_T-3','Financial_FG6_T-4','Financial_FG6_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['NONCURRENT_LIABILITY' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['FI_RETAINED_EARNINGS' + tag] / row['NONCURRENT_LIABILITY' + tag])
    data['Financial_FG7' + tag] = pd.DataFrame(frame)

data['Financial_FG7'] = data[['Financial_FG7_T','Financial_FG7_T-1','Financial_FG7_T-2']].mean(axis=1)

data['Financial_FG7_V2'] = data[['Financial_FG7_T','Financial_FG7_T-1','Financial_FG7_T-2',
                                 'Financial_FG7_T-3','Financial_FG7_T-4','Financial_FG7_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['INTEREST_SHORT' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['Gross_Cash_from_Operation' + tag] / row['INTEREST_SHORT' + tag])
    data['Financial_FD1' + tag] = pd.DataFrame(frame)

data['Financial_FD1'] = data[['Financial_FD1_T','Financial_FD1_T-1','Financial_FD1_T-2']].mean(axis=1)

data['Financial_FD1_V2'] = data[['Financial_FD1_T','Financial_FD1_T-1','Financial_FD1_T-2',
                                 'Financial_FD1_T-3','Financial_FD1_T-4','Financial_FD1_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['INTEREST2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['EBITA2' + tag] / row['INTEREST2' + tag])
    data['Financial_FD2' + tag] = pd.DataFrame(frame)

data['Financial_FD2'] = data[['Financial_FD2_T','Financial_FD2_T-1','Financial_FD2_T-2']].mean(axis=1)

data['Financial_FD2_V2'] = data[['Financial_FD2_T','Financial_FD2_T-1','Financial_FD2_T-2',
                                 'Financial_FD2_T-3','Financial_FD2_T-4','Financial_FD2_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_DEBT' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['FI_NET_OPERATING_CF' + tag] / row['TOTAL_DEBT' + tag])
    data['Financial_FD4' + tag] = pd.DataFrame(frame)

data['Financial_FD4'] = data[['Financial_FD4_T','Financial_FD4_T-1','Financial_FD4_T-2']].mean(axis=1)

data['Financial_FD4_V2'] = data[['Financial_FD4_T','Financial_FD4_T-1','Financial_FD4_T-2',
                                 'Financial_FD4_T-3','Financial_FD4_T-4','Financial_FD4_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_TOTAL_LOANS_FROM_BANK' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['EBITDA' + tag] / row['FI_TOTAL_LOANS_FROM_BANK' + tag])
    data['Financial_FD5' + tag] = pd.DataFrame(frame)

data['Financial_FD5'] = data[['Financial_FD5_T','Financial_FD5_T-1','Financial_FD5_T-2']].mean(axis=1)

data['Financial_FD5_V2'] = data[['Financial_FD5_T','Financial_FD5_T-1','Financial_FD5_T-2',
                                 'Financial_FD5_T-3','Financial_FD5_T-4','Financial_FD5_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_DEBT' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['CASH2' + tag] / row['TOTAL_DEBT' + tag])
    data['Financial_FD6' + tag] = pd.DataFrame(frame)

data['Financial_FD6'] = data[['Financial_FD6_T','Financial_FD6_T-1','Financial_FD6_T-2']].mean(axis=1)

data['Financial_FD6_V2'] = data[['Financial_FD6_T','Financial_FD6_T-1','Financial_FD6_T-2',
                                 'Financial_FD6_T-3','Financial_FD6_T-4','Financial_FD6_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['CURRENTLIABILITY_BALANCE' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['EBITA2' + tag] / row['CURRENTLIABILITY_BALANCE' + tag])
    data['Financial_FD7' + tag] = pd.DataFrame(frame)

data['Financial_FD7'] = data[['Financial_FD7_T','Financial_FD7_T-1','Financial_FD7_T-2']].mean(axis=1)

data['Financial_FD7_V2'] = data[['Financial_FD7_T','Financial_FD7_T-1','Financial_FD7_T-2',
                                 'Financial_FD7_T-3','Financial_FD7_T-4','Financial_FD7_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_ASSET2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['INVENTORIES2' + tag] / row['TOTAL_ASSET2' + tag])
    data['Financial_FCA1' + tag] = pd.DataFrame(frame)

data['Financial_FCA1'] = data[['Financial_FCA1_T','Financial_FCA1_T-1','Financial_FCA1_T-2']].mean(axis=1)

data['Financial_FCA1_V2'] = data[['Financial_FCA1_T','Financial_FCA1_T-1','Financial_FCA1_T-2',
                                  'Financial_FCA1_T-3','Financial_FCA1_T-4','Financial_FCA1_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_ASSET2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['TRADEDEBTORS_INVENTORIES' + tag] / row['TOTAL_ASSET2' + tag])
    data['Financial_FCA2' + tag] = pd.DataFrame(frame)

data['Financial_FCA2'] = data[['Financial_FCA2_T','Financial_FCA2_T-1','Financial_FCA2_T-2']].mean(axis=1)

data['Financial_FCA2_V2'] = data[['Financial_FCA2_T','Financial_FCA2_T-1','Financial_FCA2_T-2',
                                  'Financial_FCA2_T-3','Financial_FCA2_T-4','Financial_FCA2_T-5']].mean(axis=1)


data['Financial_FA1_1'] = data[['RECEIVABLE_PERIOD2_T','RECEIVABLE_PERIOD2_T-1','RECEIVABLE_PERIOD2_T-2']].mean(axis=1)
data['Financial_FA1_1_V2'] = data[['RECEIVABLE_PERIOD2_T','RECEIVABLE_PERIOD2_T-1',
                                   'RECEIVABLE_PERIOD2_T-2','RECEIVABLE_PERIOD2_T-3',
                                   'RECEIVABLE_PERIOD2_T-4','RECEIVABLE_PERIOD2_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['SALES' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['TRADE_DEBTOR2' + tag] * 365 / row['SALES' + tag])
    data['Financial_FA1_2' + tag] = pd.DataFrame(frame)

data['Financial_FA1_2'] = data[['Financial_FA1_2_T','Financial_FA1_2_T-1','Financial_FA1_2_T-2']].mean(axis=1)

data['Financial_FA1_2_V2'] = data[['Financial_FA1_2_T','Financial_FA1_2_T-1','Financial_FA1_2_T-2',
                                   'Financial_FA1_2_T-3','Financial_FA1_2_T-4','Financial_FA1_2_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_ASSET2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['SALES' + tag] / row['TOTAL_ASSET2' + tag])
    data['Financial_FA2' + tag] = pd.DataFrame(frame)

data['Financial_FA2'] = data[['Financial_FA2_T','Financial_FA2_T-1','Financial_FA2_T-2']].mean(axis=1)

data['Financial_FA2_V2'] = data[['Financial_FA2_T','Financial_FA2_T-1','Financial_FA2_T-2',
                                 'Financial_FA2_T-3','Financial_FA2_T-4','Financial_FA2_T-5']].mean(axis=1)

data['Financial_FA3_1'] = data[['FI_AVG_PAYABLE_PERIOD_T','FI_AVG_PAYABLE_PERIOD_T-1','FI_AVG_PAYABLE_PERIOD_T-2']].mean(axis=1)
data['Financial_FA3_1_V2'] = data[['FI_AVG_PAYABLE_PERIOD_T','FI_AVG_PAYABLE_PERIOD_T-1',
                                   'FI_AVG_PAYABLE_PERIOD_T-2','FI_AVG_PAYABLE_PERIOD_T-3',
                                   'FI_AVG_PAYABLE_PERIOD_T-4','FI_AVG_PAYABLE_PERIOD_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['SALES' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['FI_ACCOUNTS_PAYABLE' + tag] * 365 / row['SALES' + tag])
    data['Financial_FA3_2' + tag] = pd.DataFrame(frame)

data['Financial_FA3_2'] = data[['Financial_FA3_2_T','Financial_FA3_2_T-1','Financial_FA3_2_T-2']].mean(axis=1)

data['Financial_FA3_2_V2'] = data[['Financial_FA3_2_T','Financial_FA3_2_T-1','Financial_FA3_2_T-2',
                                   'Financial_FA3_2_T-3','Financial_FA3_2_T-4','Financial_FA3_2_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TOTAL_ASSET2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['GROSSPROFITS' + tag] / row['TOTAL_ASSET2' + tag])
    data['Financial_FA4' + tag] = pd.DataFrame(frame)

data['Financial_FA4'] = data[['Financial_FA4_T','Financial_FA4_T-1','Financial_FA4_T-2']].mean(axis=1)

data['Financial_FA4_V2'] = data[['Financial_FA4_T','Financial_FA4_T-1','Financial_FA4_T-2',
                                 'Financial_FA4_T-3','Financial_FA4_T-4','Financial_FA4_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_RETAINED_EARNINGS' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['GROSSPROFITS' + tag] / row['FI_RETAINED_EARNINGS' + tag])
    data['Financial_FA5' + tag] = pd.DataFrame(frame)

data['Financial_FA5'] = data[['Financial_FA5_T','Financial_FA5_T-1','Financial_FA5_T-2']].mean(axis=1)

data['Financial_FA5_V2'] = data[['Financial_FA5_T','Financial_FA5_T-1','Financial_FA5_T-2',
                                 'Financial_FA5_T-3','Financial_FA5_T-4','Financial_FA5_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FIXED_ASSET2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['GROSSPROFITS' + tag] / row['FIXED_ASSET2' + tag])
    data['Financial_FA6' + tag] = pd.DataFrame(frame)

data['Financial_FA6'] = data[['Financial_FA6_T','Financial_FA6_T-1','Financial_FA6_T-2']].mean(axis=1)

data['Financial_FA6_V2'] = data[['Financial_FA6_T','Financial_FA6_T-1','Financial_FA6_T-2',
                                 'Financial_FA6_T-3','Financial_FA6_T-4','Financial_FA6_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TANGIBLE_NETWORTH' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['GROSSPROFITS' + tag] / row['TANGIBLE_NETWORTH' + tag])
    data['Financial_FA7' + tag] = pd.DataFrame(frame)

data['Financial_FA7'] = data[['Financial_FA7_T','Financial_FA7_T-1','Financial_FA7_T-2']].mean(axis=1)

data['Financial_FA7_V2'] = data[['Financial_FA7_T','Financial_FA7_T-1','Financial_FA7_T-2',
                                 'Financial_FA7_T-3','Financial_FA7_T-4','Financial_FA7_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FIXED_ASSET2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['SALES' + tag] / row['FIXED_ASSET2' + tag])
    data['Financial_FA8' + tag] = pd.DataFrame(frame)

data['Financial_FA8'] = data[['Financial_FA8_T','Financial_FA8_T-1','Financial_FA8_T-2']].mean(axis=1)

data['Financial_FA8_V2'] = data[['Financial_FA8_T','Financial_FA8_T-1','Financial_FA8_T-2',
                                 'Financial_FA8_T-3','Financial_FA8_T-4','Financial_FA8_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TANGIBLE_NETWORTH' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['SALES' + tag] / row['TANGIBLE_NETWORTH' + tag])
    data['Financial_FA9' + tag] = pd.DataFrame(frame)

data['Financial_FA9'] = data[['Financial_FA9_T','Financial_FA9_T-1','Financial_FA9_T-2']].mean(axis=1)

data['Financial_FA9_V2'] = data[['Financial_FA9_T','Financial_FA9_T-1','Financial_FA9_T-2',
                                 'Financial_FA9_T-3','Financial_FA9_T-4','Financial_FA9_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_RETAINED_EARNINGS' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['SALES' + tag] / row['FI_RETAINED_EARNINGS' + tag])
    data['Financial_FA10' + tag] = pd.DataFrame(frame)

data['Financial_FA10'] = data[['Financial_FA10_T','Financial_FA10_T-1','Financial_FA10_T-2']].mean(axis=1)

data['Financial_FA10_V2'] = data[['Financial_FA10_T','Financial_FA10_T-1','Financial_FA10_T-2',
                                  'Financial_FA10_T-3','Financial_FA10_T-4','Financial_FA10_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['TRADE_DEBTOR2' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['SALES' + tag] / row['TRADE_DEBTOR2' + tag])
    data['Financial_FA11' + tag] = pd.DataFrame(frame)

data['Financial_FA11'] = data[['Financial_FA11_T','Financial_FA11_T-1','Financial_FA11_T-2']].mean(axis=1)

data['Financial_FA11_V2'] = data[['Financial_FA11_T','Financial_FA11_T-1','Financial_FA11_T-2',
                                  'Financial_FA11_T-3','Financial_FA11_T-4','Financial_FA11_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['FI_OWNERS_EQUITY' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['SALES' + tag] / row['FI_OWNERS_EQUITY' + tag])
    data['Financial_FA12' + tag] = pd.DataFrame(frame)

data['Financial_FA12'] = data[['Financial_FA12_T','Financial_FA12_T-1','Financial_FA12_T-2']].mean(axis=1)

data['Financial_FA12_V2'] = data[['Financial_FA12_T','Financial_FA12_T-1','Financial_FA12_T-2',
                                  'Financial_FA12_T-3','Financial_FA12_T-4','Financial_FA12_T-5']].mean(axis=1)

frame_lst = [ [],[],[],[],[],[] ]
for tag, frame in zip(tag_lst,frame_lst):
    for index, row in data.iterrows():
        if row['SALES' + tag] == 0:
            frame.append(None)
        else:
            frame.append(row['FI_GROSS_CASHFLOW' + tag] / row['SALES' + tag])
    data['Financial_FA13' + tag] = pd.DataFrame(frame)

data['Financial_FA13'] = data[['Financial_FA13_T','Financial_FA13_T-1','Financial_FA13_T-2']].mean(axis=1)

data['Financial_FA13_V2'] = data[['Financial_FA13_T','Financial_FA13_T-1','Financial_FA13_T-2',
                                  'Financial_FA13_T-3','Financial_FA13_T-4','Financial_FA13_T-5']].mean(axis=1)

os.chdir(r'C:\Users\yaphengteh\OneDrive')
data.to_excel('quantitative_factors.xlsx', index=False)
