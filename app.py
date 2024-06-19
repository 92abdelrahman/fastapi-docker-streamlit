import streamlit as st

import json
import os
import requests
import socket

def start_server():   
    os.system("uvicorn inference_server:app --port 8080 --host 0.0.0.0 --workers 2")
    st.session_state['server_started'] = True
    
def is_port_in_use(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('0.0.0.0', port)) == 0

def inference(input_text):
  req = "http://0.0.0.0:8080?input_text=" + input_text
  res = requests.get(req)
  st.markdown(f'## Output')
  st.write(json.loads(res.text))
 
if 'server_started' not in st.session_state:
    st.session_state['server_started'] = False

if not st.session_state['server_started']:
  start_server()              

st.title('FastAPI Demo')
input_text = st.text_input(
    label="Write something",
    value="text"
)
inference(input_text)
