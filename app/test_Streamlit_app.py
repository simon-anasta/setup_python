# Streamlit app - simple app with close button

import streamlit as st

def main():
    st.title("Simple Streamlit App")
    st.write("This is a simple Streamlit app with a close button.")
    
    if st.button("Close App"):
        st.stop()

if __name__ == "__main__":
    main()

# instead of running with `python .\app\test_Streamlit_app.py`
# run with `streamlit run .\app\test_Streamlit_app.py` to see the app in action.

# also requires Ctrl + C in the terminal to return to non-Streamlit mode.

