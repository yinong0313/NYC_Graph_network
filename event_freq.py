#load 1193 links
link_list = dill.load(open('nysd-links.pkd', 'rb'))

# Step 1: histogram
# plot the event frequency for the past 95 months
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt


link_url_all=[]
for num_links in range(len(link_list)):
    link_url,link_date = link_list[num_links]
    link_url_all.append(link_url)

link_date_formated = []
for num_links in range(len(link_list)):
    link_url,link_date = link_list[num_links]
    link_date_formated.append(link_date.strftime("%b-%Y"))
histogram= list(Counter((link_date_formated)).items())

# plot
df = pd.DataFrame(histogram[::-4], columns=['Date', 'Counts'])
axes = df.plot(kind='bar', x='Date')

# Step 2:
