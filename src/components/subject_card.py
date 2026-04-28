import streamlit as st
def subject_card(name, code, section, stats = None, footer_callback= None):
    html = f"""
        <div style ="background-color: white; padding: 20px; border-left: 8px solid #EB459E; border-radius: 20px; margin-bottom: 20px;border: 1px solid black;">
        <h3 style="margin:0;color: #1e293b, font-size:1.5rem ">{name}</h3>
        <p style="color: #64748b; margin:10px 0;"><span style="background-color: #E0E3FF; color: #5865F2; padding: 2px 8px; border-radius: 5px;"> {code} </span> | Section {section}</p>
        """
    if stats:
        html += """<div style = "display:flex; gap: 8px; flex-wrap:wrap;">"""
        for icon, label, value in stats:
            html += f'<div style = "background-color: white; padding: 5px 12px; border-radius: 10px;font-size:0.9rem;">{icon} <b>{value}</b> {label}</div>'
        
        html += "</div>"
    import streamlit as st
def subject_card(name, code, section, stats = None, footer_callback= None):
    html = f"""
        <div style ="background-color: white; padding: 20px; border-left: 8px solid #EB459E; Padding: 25px; border-radius: 20px; margin-bottom: 20px;border: 1px solid black;">
        <h3 style="margin:0,color: #1e293b, font-size:1.5rem ">{name}</h3>
        <p style="color: #64748b; margin:10px 0;"><span style="background-color: #E0E3FF; color: #5865F2; padding: 2px 8px; border-radius: 5px;"> {code} </span> | Section {section}</p>
        """
    if stats:
        html += """<div style="display:flex; gap: 8px; flex-wrap:wrap;">"""
        for icon, label, value in stats:
            html += f'<div style = "background-color: #F6CEED; padding: 5px 12px; border-radius: 10px;font-size:0.9rem;">{icon} <b>{value}</b> {label}</div>'

        html += "</div>"
    html += "</div>"    

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()        
