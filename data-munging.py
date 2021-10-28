# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##import packages 
import pandas as pd
import numpy as np
import datetime
import matplotlib as plt
import os 
import glob

##choose directory 
os.chdir('/Users/jamesgao/Desktop/ANLY 503/A5/data/')
path=os.getcwd()
households=['04','05','06']

##specify all the columns in the final data which is used in plot
full_merged_data=pd.DataFrame(columns=['family','timeframe','hour','day','weekday','year_month','date','plug_type','usage'])
weekday_reset={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
for house in households:
    path='/Users/jamesgao/Desktop/ANLY 503/A5/data/'
    abs_path=path +'/'+house

    if house=='04':
        category=['01','02','03','04','05','06','07','08']
        ##give each folder a name as the doc file suggests
        category_name=["Fridge","Kitchen appliances","Lamp","Stereo and laptop","Freezer","Tablet","Entertainment","Microwave"]
    elif house=='05':
        category=['01','02','03','04','05','06','07','08']
        category_name=["Tablet","Coffee machine","Fountain","Microwave","Fridge","Entertainment","PC","Kettle"]
    elif house=='06':
        category=['01','02','03','04','05','06','07']
        category_name=["Lamp","Laptop","Router","Coffee machine","Entertainment","Fridge","Kettle"]
    merged_data=pd.DataFrame(columns=['timeframe','hour','day','weekday','year_month','plug_type','usage','date','family'])

    for folder in category:
        path=abs_path+'/'+folder+'/'
        files=glob.glob(os.path.join(path,"*.csv"))
        print(path)

        daily_data=pd.DataFrame(columns=['hour','day','weekday','year_month','plug_type','usage','date'])
        for f in files:
            print('Location:', f)
            file_name=f.split("/")[-1]
            print('File Name:',file_name)
            df=pd.read_csv(f,header=None)
            if len(f.split('/')[-1].split(".")[0])==10:
                date=datetime.datetime.strptime(f.split('/')[-1].split(".")[0], '%Y-%m-%d')
                df['date']=date
                df['usage']=df[0]  
                df=df.reset_index() 
                df=df.loc[df.usage>=0]
                df=df.drop(columns=0)
                df.columns=['time','date','usage']
                df["hour"] = df["time"]//3600
                df=df.groupby(['date','hour'])['usage'].sum().reset_index()
                df['plug_type']=category_name[int(folder)-1]
                df['weekday']=date.weekday()
                df['weekday'].astype(int)
                df['weekday'].replace(weekday_reset, inplace=True)
                df['day']=date.day
                df['year_month']=str(date.year)+"_"+str(date.month)
                df=df[['hour','day','weekday','year_month','plug_type','usage','date']]
                daily_data=pd.concat([daily_data,df],axis=0)
            else:
                print(f.split('/')[-1].split(".")[0])

        print(daily_data.head())
        daily_data['timeframe']='morning'
        daily_data.loc[((daily_data.hour>=6) & (daily_data.hour<13)),'timeframe'] = 'Morning'
        daily_data.loc[((daily_data.hour>=13) & (daily_data.hour<19)),'timeframe'] = 'Afternoon'
        daily_data.loc[((daily_data.hour>=19) & (daily_data.hour<24)),'timeframe'] = 'Evening'
        daily_data.loc[((daily_data.hour>=0) & (daily_data.hour<6)),'timeframe'] = 'Night'
        merged_data=pd.concat([merged_data,daily_data],axis=0)
        # merged_data.info()
    merged_data['family']=house

    full_merged_data=pd.concat([full_merged_data,merged_data],axis=0)
 
full_merged_data.to_csv('munged_data.csv',index=False)
    
    
        