import streamlit as st
from utils import *
from streamlit_card import card
st.set_page_config(layout="wide")

st.header("Book recommendation system")
top_20:pd.DataFrame = get_top_20_Books()
st.subheader("Top Books")

col1,col2,col3,col4 = st.columns(4)



with col1:
    for row in range(0,5):
        img_url = top_20.iloc[row]['Image-URL-L']
        hasClicked = card(
            title=str(top_20.iloc[row]['Book-Title_x']),
            text=str(top_20.iloc[row]["Year-Of-Publication_x"]),
            image=img_url
        )
with col2:
    for row in range(5,10):
        img_url = top_20.iloc[row]['Image-URL-L']
        hasClicked = card(
            title=str(top_20.iloc[row]['Book-Title_x']),
            text=str(top_20.iloc[row]["Year-Of-Publication_x"]),
            image=img_url
        )
with col3:
    for row in range(10,15):
        img_url = top_20.iloc[row]['Image-URL-L']
        hasClicked = card(
            title=str(top_20.iloc[row]['Book-Title_x']),
            text=str(top_20.iloc[row]["Year-Of-Publication_x"]),
            image=img_url
        )

with col4:
    for row in range(15,20):
        img_url = top_20.iloc[row]['Image-URL-L']
        hasClicked = card(
            title=str(top_20.iloc[row]['Book-Title_x']),
            text=str(top_20.iloc[row]["Year-Of-Publication_x"]),
            image=img_url
        )

st.balloons()

