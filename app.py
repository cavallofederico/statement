import streamlit as st
from streamlit.components.v1 import components
import fitz

from transformstatement import transform_statement

def main():
    components.html("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-16672731166">
</script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-16672731166');
</script>
                """,width=200, height=200)
    
    st.title("Resumen Bancario HSBC a Excel")
    st.text("Subí tu resumen bancario de HSBC Argentina y obtenelo en Excel (CSV)")
    st.markdown(
        f"""
        <a href='https://cafecito.app/cavallofederico' rel='noopener' target='_blank'><img srcset='https://cdn.cafecito.app/imgs/buttons/button_1.png 1x, https://cdn.cafecito.app/imgs/buttons/button_1_2x.png 2x, https://cdn.cafecito.app/imgs/buttons/button_1_3.75x.png 3.75x' src='https://cdn.cafecito.app/imgs/buttons/button_1.png' alt='Invitame un café en cafecito.app' /></a>
        """,
        unsafe_allow_html=True
    )

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