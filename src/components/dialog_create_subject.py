import streamlit as st
from src.database.db import create_subject


@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.write("Enter the details of new subject")
    sub_id = st.text_input("subject Code", placeholder="BTCS301-18")
    sub_name = st.text_input("Subject Name", placeholder="Data Structure")
    Sub_section = st.text_input("Section", placeholder="A")

    if st.button("Create Subject Now", type="primary", width="stretch"):
        if sub_id and sub_name and Sub_section:
            try:
                create_subject(
                    sub_id, sub_name, Sub_section, teacher_id
                )  # subject_code, name, section, teacher_id
                st.toast("Subject created successfully!") 
            except Exception as e:
                st.error(f"Error:{str(e)}")
        else:
            st.warning("Please fill all the fields")
