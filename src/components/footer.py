import streamlit as st

def footer_home():

    st.markdown(
        f"""
        <div style="display:flex; align-item:center; justify-content:center; margin-top:2rem, gap:6px"> 
           <p style> Created by ❤️ </p>
              <a href="https://github.com/Amrita-creator/Amrita-creator" style="color: #000; text-decoration:none; font-weight:600; margin-left:6px">Amrita</a>    
        </div>


         
        """,
        unsafe_allow_html=True,
    )


def footer_dashboard():

    st.markdown(
        f"""
        <div style="display:flex; align-item:center; justify-content:center; margin-top:2rem, gap:6px"> 
           <p style="font-weight:bold; color:black;"> Created by ❤️ </p>
              <a href="https://github.com/Amrita-creator/Amrita-creator" style="color: #000; text-decoration:none; font-weight:600; margin-left:6px">Amrita</a>    
        </div>


         
        """,
        unsafe_allow_html=True,
    )
