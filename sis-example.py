# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
import snowflake.snowpark.functions as F

# Write directly to the app
st.title("🧾 Historic Tax Rates")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)

session = get_active_session()


tax_df = session.table("FINANCIAL_DATA.PUBLIC.CORPORATE_TAX_RATES").select(F.col("COUNTRY"), F.col("YEAR"), F.col("RATE")) # Source Table
countries_df = tax_df.select(F.col("Country")).distinct() # Get Countries for the Drop Down

selected_country = st.selectbox("COUNTRY", countries_df) # Get selected country

# Filter by Selected country
filtered_df = tax_df.filter(F.col("COUNTRY") == selected_country)

# Display Results
st.dataframe(filtered_df, use_container_width=True)
st.line_chart(filtered_df, x="YEAR", y="RATE")
