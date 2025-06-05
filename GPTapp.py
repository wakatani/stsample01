#
#
#
from math import exp
import json
from openai import OpenAI
import os
import random
import copy
import streamlit as st

#load_dotenv()

#
# APIキーは環境変数にセットしておく
#
client = OpenAI()

#

st.title("■ Let's study scikit-learn ■")

#
#
import streamlit as st
import os

if 'status' in st.session_state:
    status=st.session_state['status']
else:
    status=0

if 'counter' in st.session_state:
    counter=st.session_state['counter']
else:
    counter=0
st.write("### 問題のページ "+str(status)+"-"+str(counter))
counter +=1
st.session_state['counter']=counter
st.session_state['status']=status

if status==0:
    #st.button("問題 (quiz)")
    lang = st.radio(label='言語を選択してください (Which lang is preferable?)',
                    options=('日本語 (Japanese)', '英語 (English)'),
                    index=None,
                    horizontal=True,
    )
    if lang=="日本語 (Japanese)":
      language="日本語"
    else:
      language="英語"
    status=1
    st.session_state['status']=status
    
elif status==1:
    quiz_st="This is ...."+str(status)+"-"+str(counter)
    answ_st="The answer is ...."+str(status)+"-"+str(counter)
    st.session_state['quiz_st']=quiz_st
    st.session_state['answ_st']=answ_st
    st.write("Q: "+quiz_st)
    status=2
    st.session_state['status']=status
    b=[]
    b.append("1. choice A")
    b.append("2. choice B")
    b.append("3. choice O")
    b.append("4. choice AB")
    st.radio(label='Which is correct?',
             options=(b[0],b[1],b[2],b[3]),
             index=None,
    )

elif status==2:
    quiz_st=st.session_state['quiz_st']
    answ_st=st.session_state['answ_st']
    st.write("Q: "+quiz_st)
    st.write("A: "+answ_st)
    st.button("次へ (next)")
    status=1
    st.session_state['status']=status
  
