import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Market of used cars. Original data')
st.write('''
         #### Filter the data below to see the ads by manufacturer
         ''')

df = pd.read_csv('vehicles_us.csv')
#cleaning data
df = df.drop_duplicates()
df= df.dropna()
df['model_year']= df['model_year'].astype('int')

df['manufacturer_name'] = df ['model'].apply(lambda x: x.split(' ')[0] if pd.notnull(x) else None)
#-----------------------------------------

manufacturer_choice = df['manufacturer_name'].unique()
make_choice_man = st.selectbox('Select manufacturer:', manufacturer_choice)

df_filtered = df[df['manufacturer_name']== make_choice_man]

(min_year,max_year) = int(df['model_year'].min()), int(df['model_year'].max())

year_range = st.slider('Choose years',value=(min_year,max_year), min_value=min_year,max_value=max_year )

actual_range = list(range(year_range[0],year_range[1]+1))


st.table(df_filtered)

#----------------------------------------
st.header('Price analysis')
st.write("""
###### Let's analyze what influences price the most. We will check now how distribution of price varies depending on condition, cylinders, transmission, and fuel
# """)


list_for_hist =['condition','cylinders','transmission','fuel']

choice_for_hist=st.selectbox('Split for price distribution',list_for_hist)
fig1 = px.histogram(df,x ='price', color = choice_for_hist)
fig1.update_layout(
title="<b> Split of price by {}</b>".format(choice_for_hist))
st.plotly_chart(fig1)

#-----------------------------------
df['age']=2023-df['model_year']
def age_category(x):
    if x<5: return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'  
df['age_category']= df['age'].apply(age_category)

st.write('''
##### Now let's check how price is affected by odometer, paint color, or type of automobile''')
list_for_scatter=('odometer', 'paint_color', 'type')

choice_for_scatter = st.selectbox('Price dependency on', list_for_scatter)
fig2 = px.scatter(df, x='price', y=choice_for_scatter, color='age_category', hover_data=['model_year'])

fig2.update_layout(
title='<b. Price vs {}</b>'.format(choice_for_scatter))
st.plotly_chart(fig2)