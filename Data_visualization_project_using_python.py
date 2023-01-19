import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
df_apps=pd.read_csv('data/apps.csv')
# print(df_apps.shape)
# df_apps=df_apps.drop(['Last_Updated','Android_Ver'],axis=1,inplace=True)
# print(df_apps.isna().sum())
df_apps_clean=df_apps.dropna()
# print(df_apps_clean.shape)
duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
df_apps_clean2=df_apps_clean.drop_duplicates(subset=['App','Type','Price'])
# print(df_apps_clean2.shape)
ratings = df_apps_clean2.Content_Rating.value_counts()
# df_ratings=df_apps_clean2.groupby('Content_Rating').count()
# print(df_ratings)
reshaped_df=df_apps_clean2.pivot_table(index='Content_Rating',columns='Type',values='App',aggfunc='count')
# print(reshaped_df)


# Creating Pie chart with the plotly
fig = px.pie(labels=ratings.index,values=ratings.values,title="Pie chart representation ofContent Rating",names=ratings.index)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()

# # Creating Line graph with Matplotlib

axis1 = plt.gca() 
axis2 = axis1.twinx()
axis1.set_ylim(bottom=0, top=10000)
axis1.set_ylabel('Free',color="red",fontsize=14)
axis2.set_ylabel('Paid',color="blue",fontsize=14)
axis1.set_xlabel('Content Rating',fontsize=14)
axis1.plot(reshaped_df.index,reshaped_df.Free,color="red")
axis2.plot(reshaped_df.index,reshaped_df.Paid,color="blue")
plt.figure(figsize=(10,20))
plt.title('Content Rating of each App category', fontsize=18)
plt.show()


# # Creating a donut chart using Plotly
fig = px.pie(labels=ratings.index,values=ratings.values,title="Donut chart representation of Content Rating of each App category",names=ratings.index,hole=0.6)
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
fig.show()


# Cleaning the data further

# df_apps_clean2.Installs = df_apps_clean2.Installs.astype(str).str.replace(',', "")
# df_apps_clean2.Installs = pd.to_numeric(df_apps_clean2.Installs)
# df_install=df_apps_clean2.pivot_table(index='Installs',values='App',aggfunc='count')
# print(df_install)
# df_apps_clean2.Price = df_apps_clean2.Price.astype(str).str.replace('$', "")
# df_apps_clean2.Price = pd.to_numeric(df_apps_clean2.Price)
# print(df_apps_clean2.sort_values('Price', ascending=False).head(20))
# df_apps_clean = df_apps_clean2[df_apps_clean2.Price] < 250
# df_apps_clean.sort_values('Price', ascending=False).head(5)
# top10_category=df_apps_clean2.pivot_table(index='Category',values='App',aggfunc='count')
# print(top10_category.shape)
# print(top_10_category.sort_values('App', ascending=True))

# Analyzing the category of apps dominating the market
top_10_category = df_apps_clean2.Category.value_counts()
bar = px.bar(x=top_10_category.index, 
y=top_10_category.values, title=' Trending category of apps in Google Play store')
bar.show()


#  Top Genres trending in the market
stack = df_apps_clean2.Genres.str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')
bar = px.bar(x = num_genres.index, 
             y = num_genres.values,
             title='Top Genres of the apps trending in the market',
             hover_name=num_genres.index,
             color=num_genres.values,
             color_continuous_scale='Agsunset')
 
bar.update_layout(xaxis_title='Genre',
yaxis_title='Number of Apps',
coloraxis_showscale=False)
 
bar.show()


