import time

import streamlit as st
from src.ui.base_layout import background_dashboard, base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists, create_teacher,teacher_login
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import predict_attendance
from src.database.db import  get_all_students


def student_dashboard():
    st.header("DASHBOARD HERE")

def student_screen():
    background_dashboard()
    base_layout()

    if "student_data"  in  st.session_state:
        student_dashboard()
        return
    
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        if st.button(
            "Go back to home",
            type="secondary",
            key="loginbackbtn",
            shortcut="control+backspace",
        ):
            st.session_state["login_type"] = None
            st.rerun()
    st.header("Login using faceID", text_alignment="center")
    st.space()
    st.space() 

    show_registration = False 
    photo_src = st.camera_input("Position your face in the center") 
    if photo_src:
        img = np.array(Image.open(photo_src))

        with st.spinner('AI is scanning...'):
            detected, all_ids, num_faces = predict_attendance(img)
            if num_faces == 0:
                st.warning('Faces not found')
            elif num_faces > 1:
                st.warning('Multiple faces found')
            else:
                if detected:  
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id) , None) 

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state_user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f"welcome back!")
                        from time import sleep
                        time.sleep(1)
                        st.rerun()
                    else:
                       st.info('face not recognized! you might be a new studnet')
                       show_registration = True  
    if show_registration:
        with st.container(border = True):
            st.header('register new profile')
            new_name = st.text_input("Enter your name",placeholder='Amrita Chaturvedi')

            st.subheader('Optional: Voice enrollment')
            st.info("Enroll your for voices only attendance")

            audio_data = None
            try:
                audio_data = st.audio_input("Record a short clip of your voice (3-5 seconds)", type = "audio/wav")
            except Exception as e:
                st.error('Audio data failed!')    
            
            if st.button('create account', type = 'primary'):
                if new_name:
                    with st.spinner('Creating your profile...'):
                        student_id = create_student_profile(new_name, audio_data)
                        if student_id:
                            st.success('Profile created successfully! Please login again using faceID')
                        else:
                            st.error('Profile creation failed!')
           
        


    footer_dashboard()
