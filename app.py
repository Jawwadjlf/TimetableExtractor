import streamlit as st
import pdfplumber
import pandas as pd

st.title("Timetable Extractor")

teacher = "Muhammad Jawad Rafiq"

uploaded_file = st.file_uploader("Upload Timetable PDF", type="pdf")

if uploaded_file:

    rows = []

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            tables = page.extract_tables()

            for table in tables:
                for row in table:
                    if row:
                        text = " ".join([str(cell) for cell in row if cell])

                        if teacher.lower() in text.lower():
                            rows.append(row)

    if rows:

        df = pd.DataFrame(rows)

        st.success(f"{len(rows)} classes found")
        st.dataframe(df)

        st.download_button(
            "Download CSV",
            df.to_csv(index=False),
            "jawad_schedule.csv"
        )

    else:
        st.warning("No schedule found for this teacher.")
