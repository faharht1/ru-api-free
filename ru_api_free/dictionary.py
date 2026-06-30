from deep_translator import GoogleTranslator

_translators = {}

def _get_translator(source, target):
    key = (source, target)
    if key not in _translators:
        _translators[key] = GoogleTranslator(source=source, target=target)
    return _translators[key]


def translate(text, source="auto", target="ru"):
    text = text.strip()
    try:
        t = _get_translator(source, target)
        result = t.translate(text)
        if result and result.strip().lower() != text.lower():
            return result.strip()
    except Exception:
        pass
    return None


def translate_en_to_ru(word):
    return translate(word, source="en", target="ru")
