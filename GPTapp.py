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
    prob = st.button("問題 (quiz)")
    if prob:
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
  
# Input
input_program = st.text_area('本当に本当の最初のメッセージ')
input_error = st.text_area('次のメッセージ')
msgFinal=''

# Process
if st.button('結合'):

  msgFinal='結合結果は「'+input_program+'」と「'+input_error+'」でした'
  
# Output
  st.write(msgFinal)
