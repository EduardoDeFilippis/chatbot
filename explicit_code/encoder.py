import base64

# Leggi il tuo file app.py originale (quello con tutto il codice)
with open("app.py", "rb") as file:
    codice_originale = file.read()

# Convertilo in una stringa Base64
codice_segreto = base64.b64encode(codice_originale).decode("utf-8")

# Salvalo in un file di testo per poterlo copiare
with open("codice_segreto.txt", "w") as file:
    file.write(codice_segreto)

print("Fatto! Copia il contenuto di 'codice_segreto.txt'")