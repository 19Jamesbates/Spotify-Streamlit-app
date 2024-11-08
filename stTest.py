import streamlit as st
import subprocess


st.title("My all")
st.header("Test page")

import subprocess

# Try a different port (e.g., 8502)
process = subprocess.Popen([
    "streamlit", "run", "stTest.py",
    "--server.port", "8513",
    "--server.headless", "true"
])
