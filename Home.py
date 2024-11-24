import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from PIL import Image
from send_email import send_email

st.set_page_config(layout='wide')


#-- Variables for files
port_image = Image.open('images/port.jpg')
number27_image = Image.open('images/number27.png')

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
    I am a versatile IT enthusiast and sales administrator at Highland Industrial Supplies with a strong passion for technology and web development. My journey in IT began with creating animations in Macromedia Flash, evolving into skills in coding and website design. Over the years, I’ve honed my expertise through hands-on projects, including building websites for local businesses such as a tattoo studio, an oil provider, and a forestry surveying company.

Recently, I launched a website for a local restaurant and am working on another project. I’ve also developed Python-based applications like a PDF converter, a web scraper integrated with Google Maps for real estate listings, and the digital CV you are viewing now. Currently, I am creating a dashboard web app to display local news, weather, and tasks.

I’m seeking new challenges in data analysis, website development, or general IT roles where I can bring my technical skills and creative problem-solving abilities to the table.


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
        st.subheader('Digital C.V. Web App')
        st.caption('Python | Streamlit | Pandas')
        st.image(port_image, use_column_width=True)
        st.write(f"I created my digital CV web app using Streamlit, a Python based framework primarily used for creating Machine Learning and Data Science web apps.")
        st.write(f"Most of the data displayed on this web app is stored in .CSV files from which I extracted the data using the Pandas Python library to sort and display the relevant information.")
   
    with col6:
        st.subheader('Number 27 Bar & Kitchen')
        st.caption('Webflow | Figma | Python | Photoshop')
        st.image(number27_image, use_column_width=True)
        st.write(f"My old employer asked me to give their website a facelift and gave me full control over the design. I started from scratch and gave the site a completely new look")
        st.write(f"I created a prototype using Figma. Once I was happy with the design, i moved on to creating the site in Webflow. I wrote a Python script to conver the menu images from pdf to image files, and i used Photoshop for image edits. ")
        st.write(f"When the site was nearly ready, I also implemented a popular online booking system for the restaurant. ")