import streamlit as st
import os

#Page Config
THRESHOLD = 5
PAGE_TITLE = "Wash Log"
LOTIONS_AT = "lotion_at"
COUNT_KEY = "today_count"

#INIT Session state

if COUNT_KEY not in st.session_state:
    st.session_state[COUNT_KEY] = 0

#UI
st.set_page_config(page_title = PAGE_TITLE, page_icon = "soap", layout = "centered")

st.title("Wash Log")
st.write("Track hand washing so you dont get craked skin!")
col1, col2 = st.columns([2,1])
with col1:
    st.metric("Today", st.session_state[COUNT_KEY])
with col2:
    if st.button("1 WASH", type = "primary", use_container_width = True):
        st.session_state[COUNT_KEY] += 1
        st.rerun()

#Lotion alerts
if st.session_state[COUNT_KEY] > 0 and (st.session_state[COUNT_KEY] % THRESHOLD == 0):
    st.balloons()

#Footer
st.markdown("---")
st.caption("**No Data stored** | Made by JMeade")

