def translator(language):
    translations = {
        'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
        'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
        'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }

    def translate_word(word):
        return translations.get(language, {}).get(word, f"[no translation for '{word}']")

    return translate_word  

    
     
spanish_translator = translator("spanish")
print(spanish_translator("hello"))
print(spanish_translator("goodbye"))
print(spanish_translator("thank you"))