import time

import streamlit as st
from src.database.db import create_subject
from src.database.config import supabase
from src.database.db import enroll_student_to_subject
from src.database.db import create_attendance


def show_attendance_results(df, logs):
    st.write("please review the attendance result before confirming...")
    st.dataframe(df, hide_index=True, width="stretch")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Discard", width="stretch"):
            st.session_state.attendance_result = None
            st.session_state.attendance_images = []
            st.rerun()
    with col2:
        if st.button("Confirm & Log Attendance", type="primary", width="stretch"):
            try:
                create_attendance(logs)
                st.toast("Attendance logged successfully!")
                st.session_state.attendance_images = []
                st.session_state.attendance_result = None
                st.rerun()
            except Exception as e:
                st.error("Syncing attendance failed!")
                st.exception(e)


@st.dialog("Attendance Report")
def attendance_result_dialog(df, logs):
    show_attendance_results(df, logs)
