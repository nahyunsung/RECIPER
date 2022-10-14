import streamlit as st
import pandas as pd
view = [150, 250, 30]
st.write("# Youtube view")
st.write("## raw")
view
st.write("## bar chart")
st.bar_chart(view)
sview = pd.Series(view)
sview