import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image
import os

st.set_page_config(layout='wide')

#-- Variables for files
profile_pic = Image.open('images\profile.jpg')
cv_file = 'images\cv.pdf'
file = os.path.basename(cv_file)
contact_details = f"""
:phone: 07497716117\n
:email: cmack6189@gmail.com\n
"""

experience = pd.read_csv('assets\Book1.csv')


#-- Sidebar
with st.sidebar:
    
    st.title('Craig Mackenzie   |')
    st.subheader('Digital C.V.')
    st.caption(contact_details)
    st.download_button('Download my CV in PDF Format',data=file,file_name=file, use_container_width=True)

col1, col2 = st.columns(2, gap='small')

#-- Hero Section
with col1:
    st.image(profile_pic, width=400)

#-- Profile Section
my_profile = '''
    For the past 3 years I have been managing a small hotel in a stunning location on the west coast of Scotland. As this recent position was seasonal, it has allowed me time over the winter to do some travelling, while at the same time developing IT skills I have gained over the years as a hobby. I have completed several online courses in various areas, which you will see listed below, in hopes of moving away from the hospitality industry. 
'''

with col2:
    st.title('Personal Profile')
    st.write(my_profile)


with st.container():
    st.title('Work Experience')
    
    for i, row in experience.iterrows():
        with st.expander(row['employer'] + ' - ' + row['role']):

            st.caption(row['date'])
            st.write(row['task'])
            st.write(row['task2'])
   # with col4:
   # for index, row in df[10:].iterrows():
   #     st.header(row['title'])
   #     st.write(row['description'])
   #     st.image('images/' +row['image'])      
   #     st.write(f"[Source Code]({row['url']})")   