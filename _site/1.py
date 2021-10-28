#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 21:36:46 2021

@author: jamesgao
"""
##import packages needed
import plotly.express as px
import pandas as pd 

##read in the dataset 
df = pd.read_csv('munged_data.csv')
df.head(5)
df=df.loc[df.plug_type=='Entertainment']
df=df.groupby(['family','year_month','weekday','plug_type'])['usage'].mean().reset_index()
##For this plot, I'd like to do an interactive bar plot for the entertainment 
##usage for households 4, 5 and 6

df['family']=df["family"].astype(str)

fig = px.bar(df, x="weekday", y="usage", color="family",
  animation_frame="year_month", barmode='group',
  category_orders={"weekday": ["Monday","Tuesday","Wednesday","Thursday", "Friday", "Saturday", "Sunday"],
                   "year_month":['2012_6','2012_7','2012_8','2012_9','2012_10','2012_11','2012_12','2013_1']},
  labels={"weekday":"Weekdays",
          "usage":"Consumption",
          "family":"Households"},
  title="Weekday Consumption of Entertainment in Each Month"
                )
fig.write_html('plotly.html')