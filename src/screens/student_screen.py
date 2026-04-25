import streamlit as st
from src.ui.base_layout import background_dashboard, base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists, create_teacher,teacher_login
from PIL import Image
import numpy as np

def student_screen():
    background_dashboard()
    base_layout()

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

    photo_src = st.camera_input("Position your face in the center") 
    if photo_src:
        np.array(Image.open(photo_src))
    footer_dashboard()
