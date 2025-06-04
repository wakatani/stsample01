#
#
import streamlit as st
import os

st.write("### 簡単なアンケート")

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
