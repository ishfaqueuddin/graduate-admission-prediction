import streamlit as st
import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('gapml-pickle.pkl','rb'))
                
def main():
  st.markdown("<h4 style='text-align: center; font-weight: bold; background-color:#0068ff; color: white;'>Graduate Admission Predictor</h4>", unsafe_allow_html=True)
  #st.markdown("<h4 style='text-align: center; color: White;background-color:#DA291C'>(Made for Bangladeshi Students)</h4>", unsafe_allow_html=True)
  st.markdown('#')

  cgpa = st.slider("CGPA",0.0,4.0)
  gre = st.slider("GRE Score",0,340)
  toefl = st.slider("TOEFL Score",0,120)

  #sop = st.slider("SOP Score",0.0,5.0,step=0.5)  
  #lor = st.slider("LOR Score",0.0,5.0,step=0.5)
  
  uni_rating = st.slider("University Rating",1,5)
  research = st.slider("Research Experience (0 = NO, 1 = YES)",0,1)
  
  #uni_rating = st.selectbox(
  #   "University Rating",
  #  ('1', '2', '3', '4', '5'))

  #research = st.radio(
  #  "Research Experience (0 = NO, 1 = YES)",
  #   ('0', '1'))
  

  inputs = [[cgpa,gre,toefl,uni_rating,research]]

  if st.button('Predict'):
    result = model.predict(inputs)
    updated_res = result.flatten().astype(float)
    updated_res = ((updated_res*100)-2)
    updated_res = int(updated_res)

    st.info('Admission Probability: {}%'.format(updated_res))

  st.markdown('#')
  st.markdown("<h4 style='text-align: center; font-weight: bold; color: white; background-color:#0068ff'>Developed by 181006912 & 181008412</h4>", unsafe_allow_html=True)


if __name__ =='__main__':
  main()
