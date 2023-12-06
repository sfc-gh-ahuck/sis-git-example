# The Snowpark package is required for Python Worksheets. 
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col, coalesce, lit, trim
import pandas as pd

def main(session: snowpark.Session): 
    df = session.create_dataframe([[None, None, ' a ']], schema=['a', 'b', 'c'])
    df = df.with_column('c', trim(df.col('c')))
    pd_df = pd.DataFrame([['a']])

    print(pd_df)
    return df.select(df.a, df.b, df.c, coalesce(df.a, df.b, df.c).as_("COALESCE"))
    