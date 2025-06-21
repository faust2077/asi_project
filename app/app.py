import time
import pandas as pd
import streamlit as st
from model.model import use_model

st.set_page_config(page_title="CalTracker")

def main():
    st.title("CalTracker")

    data = pd.DataFrame({
        "Gender": [None],
        "Age": [None],
        "Duration": [None],
        "Heart_Rate": [None],
        "Body_Temp": [None],
    })

    gender_options = ["male", "female"]

    edited_df = st.data_editor(
        data,
        column_config={
            "Gender": st.column_config.SelectboxColumn("Gender", options=gender_options),
            "Age": st.column_config.NumberColumn("Age", min_value=0, step=1),
            "Duration": st.column_config.NumberColumn("Duration", min_value=0.0, step=0.1, format="%.1f"),
            "Heart_Rate": st.column_config.NumberColumn("Heart_Rate", min_value=0.0, step=0.1, format="%.1f"),
            "Body_Temp": st.column_config.NumberColumn("Body_Temp", min_value=0.0, step=0.1, format="%.1f"),
        },
        num_rows="fixed",
        hide_index=True
    )

    file_name = "user_data.csv"

    if st.button("Calculate calories burned"):
        with st.spinner('Calculation in progress...'):
            edited_df.to_csv(file_name, index=False)
            time.sleep(3)
            df = pd.read_csv(file_name)
            cal = use_model(df)
            st.write("Estimated calories burned: ", cal)

if __name__ == "__main__":
    main()
