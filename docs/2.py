#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 00:39:53 2021

@author: jamesgao
"""
##import packages
import altair as alt
import pandas as pd

##read in the dataset 
df = pd.read_csv('munged_data.csv')
df.head(5)

df=df.loc[df.plug_type=='Entertainment']


df['family']=df["family"].astype(str)

# select_year = alt.selection_single(
#     fields=['hour'], init={'hour': 0},
#     bind=alt.binding_range(min=0, max=23, step=24)
# )

chart_1=alt.Chart(df).mark_boxplot(ticks=True).encode( 
x=alt.X("family:N", title=None, axis=alt.Axis(labels=False, ticks=False), scale=alt.Scale(padding=1)), 
y=alt.Y('usage', scale=alt.Scale(zero=False)), 
color="family:O",
  column=alt.Column('timeframe:N', sort=['Morninig','Afternoon','Evening','Night'], header=alt.Header(orient='bottom'))
).properties(
    width=300,
    height=300)
chart_1.save('altair.html')


