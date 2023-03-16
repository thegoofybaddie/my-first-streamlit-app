import streamlit as st
import sklearn
import plotly

st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
  if a == 0 and b == 0 :
    st.success('Phương trình vô số nghiệm')
  elif a == 0 and b!= 0:
    st.success('Phương trình vô nghiệm')
  elif a != 0:
    result = -b/a
    st.success(f'Phương có 1 nghiệm là {result}')
   
    
  
