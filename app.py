import streamlit as st
import pdfplumber
import pandas as pd

st.title("Timetable Extractor")

teacher = "muhammad jawad rafiq"

uploaded_file = st.file_uploader("Upload Timetable PDF", type="pdf")

if uploaded_file:

    lines = []

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            if text:
                lines.extend(text.split("\n"))

    results = []

    for i,line in enumerate(lines):

        if teacher in line.lower():

            context = " | ".join(lines[max(0,i-2): i+3])

            results.append(context)

    if results:

        df = pd.DataFrame(results, columns=["Schedule Context"])

        st.success(f"{len(results)} entries found")
        st.dataframe(df)

        st.download_button(
            "Download CSV",
            df.to_csv(index=False),
            "jawad_schedule.csv"
        )

    else:
        st.warning("No matches found")
