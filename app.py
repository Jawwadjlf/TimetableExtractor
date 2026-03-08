import streamlit as st
import pdfplumber
import pandas as pd

st.title("Timetable Extractor")

teacher_name = "muhammad jawad rafiq"

uploaded_file = st.file_uploader("Upload Timetable PDF", type="pdf")

if uploaded_file:

    full_text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text.lower()

    lines = full_text.split("\n")

    results = []

    for i in range(len(lines)):
        block = " ".join(lines[i:i+3])   # combine nearby lines

        if teacher_name in block:
            results.append(block)

    if results:

        df = pd.DataFrame(results, columns=["Matched Timetable Rows"])

        st.success(f"Found {len(results)} matches")
        st.dataframe(df)

        st.download_button(
            "Download CSV",
            df.to_csv(index=False),
            "jawad_schedule.csv"
        )

    else:
        st.warning("No matches found")
