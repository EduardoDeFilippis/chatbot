import streamlit as st
import base64
if "HIDDEN_CODE" in st.secrets:
    encrypted_code = st.secrets["HIDDEN_CODE"]
    # Decodifica la stringa da Base64 a Python normale
    decoded_code = base64.b64decode(encrypted_code).decode("utf-8")
    exec(decoded_code)
else:
    st.error("Codice sorgente protetto. Impossibile avviare l'applicazione.")
