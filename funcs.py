def certificates():    
    cert_image = Image.open(row['image'])
    st.subheader(row['course'])
    st.image(cert_image, use_column_width=True)
    st.caption(f"Issue Date: {row['issue date']}")
    st.caption(f"Issuing Organization: {row['organisation']}")
    st.caption(f"Credential ID: {row['credential id']}")
    st.caption(f"Link To Certificate: {row['certificate link']}")
    st.write(row['desc'])