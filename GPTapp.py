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
    st.button("問題 (quiz)")
    quiz_st="This is ...."+str(status)+"-"+str(counter)
    answ_st="The answer is ...."+str(status)+"-"+str(counter)
    status=1
    st.session_state['status']=status
    st.session_state['quiz_st']=quiz_st
    st.session_state['answ_st']=answ_st

    
elif status==1:
    quiz_st=st.session_state['quiz_st']
    answ_st=st.session_state['answ_st']
    st.write("Q: "+quiz_st)
    st.write("A: "+answ_st)
    status=0
    st.session_state['status']=status
    st.button("次へ (next)")
  
