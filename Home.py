import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image
import os
from send_email import send_email


st.set_page_config(layout='wide')

#-- Variables for files
profile_pic = Image.open('images\profile.jpg')
cv_file = 'images\cv.pdf'
resume = os.path.basename(cv_file)
contact_details = f"""
:phone: 07497716117\n
:email: cmack6189@gmail.com\n
"""



certificates = pd.read_csv('assets\certificates.csv')
experience = pd.read_csv('assets\Book1.csv')


#-- Sidebar
with st.sidebar:
    
    st.title('Craig Mackenzie ')
    st.subheader('Digital C.V.')
    st.caption(contact_details)
    st.download_button('Download my CV in PDF Format',data=resume,file_name=resume, use_container_width=True)

    st.header('Contact Me')

    with st.form(key='contact'):
        name = st.text_input('Name')
        user_email = st.text_input('E-mail Address')
        query = st.text_area('Your Message')
        message = f'''\
    Subject: {user_email} 

        {query}

        '''
        button = st.form_submit_button('Submit')
        if button:
            send_email(message)
            st.info('Email sent succesfuly.')





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

#-- tab section
tab1, tab2, tab3, tab4,= st.tabs(["Work History", "Certificates & Skills", "Other Relevant Info", "Projects"])

with tab1:
    with st.container():
        st.header('Work History')
        
        for i, row in experience.iterrows():

            with st.expander(row['employer'] + ' - ' + row['role']):
                st.caption(row['date'])
                st.write(row['task'])
                st.write(row['task2'])
 

with tab2:
    st.header('Certificates & Skills')
    col3, col4 = st.columns(2, gap='large')

    for i, row in certificates.iterrows():
        if i % 2 == 0:
            with col3:
                st.subheader(row['course'])
                st.caption(f"Issue Date: {row['issue date']}")
                st.caption(f"Issuing Organization: {row['organisation']}")
                st.caption(f"Credential ID: {row['credential id']}")
                st.caption(f"Link To Certificate: {row['certificate link']}")
                st.write(row['desc'])
        else:
            with col4:
                st.subheader(row['course'])
                st.caption(f"Issue Date: {row['issue date']}")
                st.caption(f"Issuing Organization: {row['organisation']}")
                st.caption(f"Credential ID: {row['credential id']}")
                st.caption(f"Link To Certificate: {row['certificate link']}")
                st.write(row['desc'])

with tab3:
    st.write('Coming Soon')

with tab4:
    st.write('also coming soon')