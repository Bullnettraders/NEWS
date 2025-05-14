# translator.py

from deep_translator import GoogleTranslator

def translate_text(text, target_language='de'):
    try:
        return GoogleTranslator(source='auto', target=target_language).translate(text)
    except Exception as e:
        print(f"Übersetzungsfehler: {e}")
        return text  # Falls Übersetzung fehlschlägt, Originaltext zurückgeben
