import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image
from send_email import send_email

st.set_page_config(layout='wide')


#-- Variables for files
port_image = Image.open('images/port.jpg')

contact_details = f"""
:phone: 07497 716 117\n
:email: cmack6189@gmail.com\n
"""

certificates = pd.read_csv('assets/certificates.csv')
experience = pd.read_csv('assets/history.csv')

#-- Sidebar
with st.sidebar:
    
    st.title('Craig Mackenzie ')
    st.subheader('Digital C.V.')
    st.caption(contact_details)

    #-- Load CV pdf file and make available for download.
    with open('assets/Craig_Mackenzie_CV.pdf', "rb") as f:
        pdf = f.read() 
    st.download_button('Download C.V. as a PDF File.', data=pdf,file_name='Craig Mackenzie CV', mime='application/octet-stream')
    

    st.header('Get In Touch')
    #-- Contact Form.
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



col1, col2= st.columns([.4,.6], gap='small')

#-- Profile Section

with col1:
    st.header('Craig Mackenzie')
    st.subheader('Digital C.V.')
    st.caption('If you prefer a more traiditional C.V. format, you can download a PDF version of my C.V. in the sidebar to the left.')

my_profile = '''
    For the past 3 years I have been managing a small hotel in a stunning location on the west coast of Scotland. As this recent position was seasonal, it has allowed me time over the winter to do some travelling, while at the same time developing IT skills I have gained over the years as a hobby. I have completed several online courses in various areas, which you will see listed below, in hopes of moving away from the hospitality industry. 

    My interest in IT was first peaked back in the days of Macromedia Flash when some friends and I would create small animations for fun. This lead me on to learning some code such as Action Script and Visual Basic. From there I discovered website design and development which I still practice as a hobby to this day. I have created some small websites for friends businesses over the years, including a Tatto Studio, an oil provider, and spent a lot of my time during lockdown working on a website for a local Forestry Surveying company. 

    In more recent years I have been concentrating on Python. I have found there is very little you can not do with Python. Some of the projects I have made using Python include a .PDF converter, a web scraper for an estate agent that displays properties on Google Maps, and this Digital CV you are viewing now. I am in the process of creating a web app that acts as a dashboard, displaying local news and weather information, and a task tracker.


'''

with col2:
    
    st.write(my_profile)


#-- tab section
tab1, tab2, tab3= st.tabs(["Skills & Certificates", "Employment History", "Projects"])

#-- Work History
with tab2:
    col3, col4, col5 = st.columns([0.5,3,0.5])
    with col4:        
        for i, row in experience.iterrows():
            with st.expander(row['employer'] + ' - ' + row['role']):
                st.caption(row['date'])
                st.write(row['description'])
 
#-- Certificates
with tab1:
    col3, col4 = st.columns(2, gap='large')

    for i, row in certificates.iterrows():
        if i % 2 == 0:
            with col3:
                cert_image = Image.open(row['image'])
                st.subheader(row['course'])
                st.image(cert_image, use_column_width=True)
                st.caption(f"Issue Date: {row['issue date']}")
                st.caption(f"Issuing Organization: {row['organisation']}")
                st.caption(f"Credential ID: {row['credential id']}")
                st.caption(f"Link To Certificate: {row['certificate link']}")
                st.write(row['desc'])
        else:
            with col4:
                cert_image = Image.open(row['image'])
                st.subheader(row['course'])
                st.image(cert_image, use_column_width=True)
                st.caption(f"Issue Date: {row['issue date']}")
                st.caption(f"Issuing Organization: {row['organisation']}")
                st.caption(f"Credential ID: {row['credential id']}")
                st.caption(f"Link To Certificate: {row['certificate link']}")
                st.write(row['desc'])


with tab3:
    col5, col6, col7 = st.columns(3, gap='small')
    with col5:
        st.title('Digital C.V. Web App')
        st.image(port_image, use_column_width=True)
        st.write(f"I created my digital CV web appusing Streamlit which is a Python based framwork primarily used for creating Machine Learning and Data Science web apps.")
        st.write(f"Most of the data displayed on this web app is stored in .CSV files from which I extracted the data using the Pandas Python library to sort and display the relevant information.")