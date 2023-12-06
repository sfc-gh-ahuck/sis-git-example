# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
import snowflake.snowpark.functions as F

# Write directly to the app
st.title("🧾 This is a second page")
st.write(
    """Just for demo purposes.
    """
)

session = get_active_session()

st.balloons()
