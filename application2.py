#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[3]:

import pandas as pd
import numpy as np
import streamlit as st
import pickle as p

p_out = open("C:/Users/91830/Incident_Impact_Prediction_Project/model_rf.pkl", "rb")
model = p.load(p_out)

def welcome():
    return "Welcome All"     
def user_input_features():
    st.header('User Input Features')
    opened_by = st.text_input('Opened_by', )
    category  = st.text_input('Category',)
    caller_id=st.text_input('Caller_ID',)
    subcategory=st.text_input('Subcategory',)
    u_symptom=st.text_input('U_Symptom',)
    incident_state=st.text_input('Incident_State',)
    resolved_by =st.text_input('Resolved_by')
    opened_at_day=st.text_input('Opened_at_day')
    Data = {'Opened by': opened_by, 'category ':category ,
            'Caller ID': caller_id,'Subcategory': subcategory, 'U_Symptom': u_symptom,
             'Incident_State': incident_state,'Resolved_by': resolved_by,
    'Opened_at_day': opened_at_day, 
   }
    features = pd.DataFrame(Data,index=[0])
    return features  
def main():
    st.title("Incident Prediction")
    
    html_temp = """
     <div style ="background-color:yellow;padding:13px">
     <h1 style ="color:black;text-align:center;">Streamlit incident prediction ML App </h1>
     </div>
     """
    level = st.slider("Select the level", 0, 2)
    st.text('Selected: {}'.format(level))
    st.markdown(html_temp, unsafe_allow_html=True)
    df = user_input_features()

    High_html= """ 
     <div style = "background-color:#F4D03F;padding:13px">
     <h2 style = "color:white;text-align:center;">Streamlit incident prediction ML App </h2>
     </div>
     """
    Medium_html= """ 
     <div style ="background-color:#F08080;padding:13px">
     <h3 style ="color:white;text-align:center;">Streamlit incident prediction ML App </h3>
     </div>
     """     
    Low_html= """ 
     <div style ="background-color:#F39C12;padding:13px">
     <h1 style ="color:white;text-align:center;">Streamlit incident prediction ML App </h2>
     </div>
     """                  
    st.subheader('User Input parameters')
    st.write(df)
    result = ""
    if st.button("Predict"):
        result = model.predict(df)
        output=result
        st.success('The prediction is {}'.format(result))                  
        if output == 2:
            st.markdown(High_html,unsafe_allow_html=True)
        elif output == 1:
            st.markdown(Medium_html,unsafe_allow_html=True)  
        else:
            st.markdown(Low_html,unsafe_allow_html=True)   
           
        
       
    
    
if _name=='main_':
        main()
