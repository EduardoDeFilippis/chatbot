import streamlit as st
import os
from huggingface_hub import InferenceClient

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(
    page_title="Eduardo De Filippis - AI Portfolio",
    page_icon="👨‍💻",
    layout="centered"
)

# --- GESTIONE SICURA API KEY ---
# Cerca il token prima nei secrets di Streamlit (per il deploy), poi nelle variabili d'ambiente (per locale)
if "HF_TOKEN" in st.secrets:
    api_token = st.secrets["HF_TOKEN"]
else:
    api_token = os.environ.get("HF_TOKEN")

# Se il token non viene trovato, mostra un avviso ma non crashare subito (permette di vedere la UI)
if not api_token:
    st.warning("⚠️ API Token non trovato. Configura 'HF_TOKEN' nei secrets o nelle variabili d'ambiente.")

# --- IL TUO CV (CONTESTO PER L'AI) ---
CONTEXT = """
SEI EDUARDO DE FILIPPIS. Rispondi in prima persona (uso "io").
Se ti chiedono chi sei, presentati brevemente come Data Scientist.
Se ti fanno domande non presenti nel CV, rispondi cortesemente che non hai quell'informazione specifica ma sei disponibile a discuterne via email.
Adatta la lingua alla domanda dell'utente (Italiano o Inglese).

Ecco il tuo profilo professionale completo:

DATI PERSONALI:
Nome: Eduardo De Filippis
Nato il: 21/09/1996
Luogo: Castrolibero, Cosenza (Italia)
Email: defilippiseduardo@gmail.com
LinkedIn: linkedin.com/in/defilippiseduardo
Sito: eduardodefilippis.com
Patente: B
Contatto: (+39) 3490567204

SOMMARIO:
Data Scientist e membro di diverse associazioni professionali con un solido background in economia/statistica e competenze in Python, R, SQL e machine learning.
Esperienze precedenti: analista software, ricercatore statistico, tutor e assistente alla didattica.
Istruzione: Laurea triennale in Economia, Magistrale in Economia e Commercio, Dottorato (PhD non completato per scelta strategica per focus su sfide industriali applicate), due master di specializzazione (Data Analysis e Data Science).
Hobby: scherma, birdwatching, trekking, ricerca scientifica, tecnologia, musica.

ESPERIENZA LAVORATIVA:
- [07/2025 – Presente]: Data Scientist presso Internet & Idee (Threat intelligence, cybersecurity, BI).
- [07/2025 – Presente]: Peer reviewer (gratuito) per riviste scientifiche (statistica, ML, AI).
- [09/2024 – 03/2025]: Software Analyst (tecnico e funzionale) presso Adecco (gestione tesoreria).
- [05/2023 – 01/2024]: Ricercatore in statistica presso Università della Calabria (disuguaglianze, ML).
- [12/2022 – 05/2023]: Tutor di Microeconomia presso Università della Calabria.
- [03/2022 – 07/2022]: Assistente alla didattica di Economia Industriale presso Università della Calabria.

ISTRUZIONE:
- [02/2025 – 08/2025]: Master professionale in Data Science, ProfessionAI & MediaDream Academy (Voto: 30/30).
- [05/2024 – 06/2025]: Master I livello in Data and Process Analysis, Unitelma Sapienza (Tesi su Transformer Architecture, Voto: 110/110).
- [10/2023 – 08/2024]: PhD in Scienze Economiche e Aziendali (Statistica), Università della Calabria (Non completato per scelta).
- [09/2020 – 12/2022]: Laurea Magistrale in Economia e Commercio, Università della Calabria (Tesi statistica su Bipolarità redditi, Voto: 110/110 e Lode + Menzione).
- [09/2016 – 12/2019]: Laurea Triennale in Economia, Università della Calabria (Voto: 104/110).

COMPETENZE (SKILLS):
- Soft: Project management, problem solving, comunicazione assertiva, teamwork.
- Hard: Data analysis, modellazione, ETL, visualizzazione, prompt engineering.
- Linguaggi: Python, R, SQL, Stata, LaTeX.
- Strumenti: Gretl, Anaconda, Jupyter, RStudio, Databricks, Visual Studio, DBeaver, Spoon, Git/GitHub, Tableau, Power BI, Azure DevOps.
- Lingue: Italiano (Madrelingua), Inglese (B2 in tutte le aree).

CERTIFICAZIONI:
- Salesforce: Tableau Data Analyst (11/2025), Tableau Desktop Foundations (11/2025).
- ASA: GStat accreditation (08/2025).
- ACM: Certified reviewer (07/2025).
- IDCERT: Artificial Intelligence (03/2023).
- EIPASS: Progressive e 7 Modules.

AFFILIAZIONI:
- Association for Computing Machinery (ACM) - Professional member.
- American Statistical Association (ASA) - Regular member.
- Società Italiana di Statistica (SIS) - Socio ordinario.
- Associazione Alumni DESF - Membro del direttivo.
- Società Italiana di Econometria (SIdE).

PORTFOLIO PROGETTI (Esempi significativi):
1. Internet & Idee (NDA): ML, NLP, Cybersecurity, Computer Vision, Pipeline ETL.
2. Master Project - Wikipedia Analysis: Big Data con PySpark, Databricks.
3. Anti-spam software: NLP, Spacy, TF-IDF, LDA.
4. Anti-hater filter: Deep Learning, RNN, Bi-LSTM, Keras.
5. Creditworthiness model: XGBoost, LightGBM, Random Forest, SHAP values.
6. Previsione peso neonati (R): Regressione lineare multipla.

PUBBLICAZIONI/WORKSHOP:
- Speaker al Workshop Unical (09/2023) su bipolarità dei redditi.
- Ricerche accademiche su trasmissione intertemporale del reddito e metodo della distribuzione relativa.
"""

# --- SIDEBAR ---
with st.sidebar:
    st.title("Eduardo De Filippis")
    st.markdown("### Data Scientist & Researcher")
    st.image("https://ui-avatars.com/api/?name=Eduardo+De+Filippis&background=0D8ABC&color=fff&size=200", caption="Eduardo Virtuale") 
    st.markdown("---")
    st.markdown("**Contatti Rapidi:**")
    st.markdown("📧 defilippiseduardo@gmail.com")
    st.markdown("🔗 [LinkedIn](https://linkedin.com/in/defilippiseduardo)")
    st.markdown("🌐 [Website](https://eduardodefilippis.com)")
    st.info("Questo chatbot risponde esattamente come se fossi io, basandosi sul mio CV reale.")

# --- INIZIALIZZAZIONE CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Ciao! Sono l'assistente virtuale di Eduardo. Chiedimi pure delle mie esperienze lavorative, dei miei progetti o delle mie competenze!"}
    ]

# --- UI CHAT ---
st.title("💬 Parla con Eduardo")
st.caption("Powered by LLM & Streamlit")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- LOGICA LLM ---
def get_response(user_input):
    repo_id = "Qwen/Qwen2.5-1.5B-Instruct"
    
    if not api_token:
        return "⚠️ Errore: API Token Hugging Face mancante."

    # Inizializza il client usando la variabile corretta 'api_token'
    client = InferenceClient(model=repo_id, token=api_token)

    # Costruiamo il prompt system + history
    messages_payload = [{"role": "system", "content": CONTEXT}]
    
    # Aggiungiamo gli ultimi messaggi per la memoria (ultimi 6 per velocità e risparmio token)
    for msg in st.session_state.messages[-6:]:
        messages_payload.append({"role": msg["role"], "content": msg["content"]})
    
    # Aggiungiamo il messaggio corrente se non è già l'ultimo (check sicurezza)
    if messages_payload[-1]["content"] != user_input:
         messages_payload.append({"role": "user", "content": user_input})

    try:
        stream = client.chat_completion(
            messages=messages_payload,
            max_tokens=500,
            temperature=0.7,
            stream=True
        )
        return stream
    except Exception as e:
        return f"⚠️ Errore di connessione o Token non valido: {e}"

# --- GESTIONE INPUT ---
if prompt := st.chat_input("Scrivi qui la tua domanda..."):
    # 1. Mostra messaggio utente
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Genera risposta
    with st.chat_message("assistant"):
        stream_response = get_response(prompt)
        
        # Gestione del caso in cui get_response restituisca una stringa di errore invece di uno stream
        if isinstance(stream_response, str):
            st.error(stream_response)
            response = stream_response
        else:
            response = st.write_stream(stream_response)
    
    # 3. Salva risposta nella history
    st.session_state.messages.append({"role": "assistant", "content": response})
