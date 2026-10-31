import streamlit as st

#st.title('우리 회사 챗봇')

page_1 = st.Page('page_1.py')
page_2 = st.Page('page_2.py')
page_3 = st.Page('page_3.py')

pages = st.navigation([page_1, page_2, page_3], position='top')

pages.run()