import streamlit as st
import fitz

from transformstatement import transform_statement

def main():
    st.title("Resumen Bancario HSBC")

    # Upload PDF file
    pdf_file = st.file_uploader("Elegir Archivo PDF", type="pdf")

    if pdf_file:
        pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
        csv_document = transform_statement(pdf_document)
        st.download_button(
            label="Descargar CSV",
            data=csv_document,
            file_name=f"{pdf_file.name[:-4]}.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()