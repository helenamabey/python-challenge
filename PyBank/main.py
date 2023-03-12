#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


csv_path = "Resources/budget_data.csv"
financials = pd.read_csv(csv_path)
#financials.head()


# In[3]:

#total number of months
total_months = financials["Date"].count()



# In[4]:

#net total of profit and losses
net_total = financials["Profit/Losses"].sum()



# In[5]:

#create column to calculate change month over month
financials["Changes"] = financials["Profit/Losses"].shift(1)



# In[6]:

#calculate change month over month
financials["average_change"] = financials["Profit/Losses"] - financials["Changes"]
#financials.head()


# In[7]:

#average change
mean = financials["average_change"].mean()



# In[8]:

#greatest increase in profits
increase = financials["average_change"].max()



# In[9]:

#greatest decrease in profits
decrease = financials["average_change"].min()



# In[14]:

#print to terminal
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${round(mean, 2)}')
print(f'Greatest Increase in Profits: {financials.loc[financials["average_change"]==increase,"Date"].item()} (${int(increase)})')
print(f'Greatest Decrease in Profits: {financials.loc[financials["average_change"]==decrease,"Date"].item()} (${int(decrease)})')


# In[18]:

#export to txt file
with open('analysis/final.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f'Total Months: {total_months}\n')
    f.write(f'Total: ${net_total}\n')
    f.write(f'Average Change: ${round(mean, 2)}\n')
    f.write(f'Greatest Increase in Profits: {financials.loc[financials["average_change"]==increase,"Date"].item()} (${int(increase)})\n')
    f.write(f'Greatest Decrease in Profits: {financials.loc[financials["average_change"]==decrease,"Date"].item()} (${int(decrease)})\n')


# In[ ]:




