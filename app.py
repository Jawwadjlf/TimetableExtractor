import streamlit as st
import pdfplumber
import pandas as pd

st.title("Timetable Extractor")

teacher_name = "Muhammad Jawad Rafiq"

uploaded_file = st.file_uploader("Upload Timetable PDF", type="pdf")

if uploaded_file:

    rows = []

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            if text:
                for line in text.split("\n"):
                    if teacher_name.lower() in line.lower():
                        rows.append(line)

    if rows:
        df = pd.DataFrame(rows, columns=["Timetable Rows"])
        st.dataframe(df)

        st.download_button(
            "Download CSV",
            df.to_csv(index=False),
            "schedule.csv"
        )
