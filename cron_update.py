import requests

try:
    # Questa chiamata "sveglia" il tuo sito, costringendo il Worker ad aggiornare il database D1
    print("Sveglio il Worker di Lopislab per aggiornare i pronostici...")
    response = requests.get("https://lopislab.com/")
    if response.ok:
        print("Sincronizzazione completata con successo sul sito!")
    else:
        print(f"Il sito ha risposto con errore: {response.status_code}")
except Exception as e:
    print(f"Errore durante la chiamata: {e}")
