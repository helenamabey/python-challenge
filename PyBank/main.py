#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


csv_path = "PyBank/Resources/budget_data.csv"
financials = pd.read_csv(csv_path)
#financials.head()


# In[3]:


total_months = financials["Date"].count()
#total_months


# In[4]:


net_total = financials["Profit/Losses"].sum()
#net_total


# In[5]:


financials["Changes"] = financials["Profit/Losses"].shift(1)
#financials.head()


# In[6]:


financials["average_change"] = financials["Profit/Losses"] - financials["Changes"]
#financials.head()


# In[7]:


mean = financials["average_change"].mean()
#mean


# In[8]:


increase = financials["average_change"].max()
#increase


# In[9]:


decrease = financials["average_change"].min()
#decrease


# In[14]:


print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${round(mean, 2)}')
print(f'Greatest Increase in Profits: {financials.loc[financials["average_change"]==increase,"Date"].item()} (${int(increase)})')
print(f'Greatest Decrease in Profits: {financials.loc[financials["average_change"]==decrease,"Date"].item()} (${int(decrease)})')


# In[18]:


with open('PyBank/analysis/final.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f'Total Months: {total_months}\n')
    f.write(f'Total: ${net_total}\n')
    f.write(f'Average Change: ${round(mean, 2)}\n')
    f.write(f'Greatest Increase in Profits: {financials.loc[financials["average_change"]==increase,"Date"].item()} (${int(increase)})\n')
    f.write(f'Greatest Decrease in Profits: {financials.loc[financials["average_change"]==decrease,"Date"].item()} (${int(decrease)})\n')


# In[ ]:




