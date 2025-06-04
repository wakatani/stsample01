#
#
import streamlit as st
import os

if !st.session_state['status']:
    status=0
else:
    status=st.session_state['status']
    
st.write("### 問題のページ"+str(status))
status +=1
st.session_state['status']=status

prob = st.button("問題 (quiz)")

if prob:
  like_streamlit = st.checkbox("Streamlitが好きですか？")
  if like_streamlit:
      level = st.radio("どれくらい好きですか？", ("ちょっと", "まあまあ", "とても"))
      st.write(f"レベル：{level}")
  else:
      st.write("これから好きになるかもしれませんね！")


# Input
input_program = st.text_area('本当に本当の最初のメッセージ')
input_error = st.text_area('次のメッセージ')
msgFinal=''

# Process
if st.button('結合'):

  msgFinal='結合結果は「'+input_program+'」と「'+input_error+'」でした'
  
# Output
  st.write(msgFinal)
