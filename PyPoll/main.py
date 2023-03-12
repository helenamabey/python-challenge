#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


csv_path = "Resources/election_data.csv"
election_results = pd.read_csv(csv_path)


# In[4]:


#election_results.head()


# In[5]:

#total number of votes
total_votes = election_results["Ballot ID"].count()


# In[6]:


#total_votes


# In[7]:

#candidate list
candidates = election_results["Candidate"].unique()


# In[8]:

#votes per candidate
votes = election_results["Candidate"].value_counts()[election_results["Candidate"].unique()]


# In[9]:

#most popular vote
winner = election_results["Candidate"].mode()
#print(winner.item())


# In[10]:

#percentage of votes
percentage = round((votes/total_votes) * 100, 3)


# In[11]:


#for x,y,z in zip(candidates,percentage,votes):
    #print(f'{x}: {y}% ({z})')


# In[12]:
#print to terminal

print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
for x,y,z in zip(candidates,percentage,votes):
    print(f'{x}: {y}% ({z})')
print("-------------------------")
print(f'Winner: {winner.item()}')
print("-------------------------")


# In[ ]:
#export to txt file

with open('analysis/final.txt', 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f'Total Votes: {total_votes}\n')
    f.write("-------------------------\n")
    for x,y,z in zip(candidates,percentage,votes):
        f.write(f'{x}: {y}% ({z})\n')
    f.write("-------------------------\n")
    f.write(f'Winner: {winner.item()}\n')
    f.write("-------------------------")

