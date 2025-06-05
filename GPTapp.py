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
        like_streamlit = st.checkbox("Streamlitが好きですか？")
        status=1
        st.session_state['like_streamlit']=like_streamlit
        st.session_state['status']=status
        
elif status==1:
  like_streamlit=st.session_state['like_streamlit']
  if like_streamlit:
      level = st.radio("どれくらい好きですか？", ("ちょっと", "まあまあ", "とても"))
      st.write(f"レベル：{level}")
  else:
      st.write("これから好きになるかもしれませんね！"+str(like_streamlit))
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
