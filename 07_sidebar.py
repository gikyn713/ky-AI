streamlit as st
from PIL import Image



st.sidebar.title("사이드바")
st.sidebar.heather("")
user_id=st.sidebar.text_input("")
user_pw=st.sidebar.text_input("pw입력",value='abcd',type='password')

st.sidebar.heather("셀렉트박스")
sel_opt=['진주 귀걸이를 한 소녀','']
user_opt=st.sidebar.selecrbox("")
st.sidebar.write("")


st.title("")
folder ='D:\AI hee\data\'
Image_files=['Vermeer.png','GOgh.png',]

sel_img_index = sel_opt.index(user_opt)

img_file = Image_files[]
img_local = Image_open(r'D:/AI_hee/data/'+img_file)
st.image(img_local,caption=user_opt)