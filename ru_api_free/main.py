from fastapi import FastAPI, Query, HTTPException, Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .conjugator import conjugate, search_verbs, list_verbs, get_exceptions, get_verb_exceptions, EXCEPTION_TYPES, VERBS
from .dictionary import translate
from .pluraliser import pluralise_with_info
from .declension import decline_with_info
from .adjectives import decline_adjective_with_info

app = FastAPI(
    title="Russian Verb Conjugation API",
    description="Free API for conjugating Russian verbs in all tenses (present, past, future)",
    version="1.5.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import importlib.resources as res

try:
    static_path = res.files("ru_api_free").joinpath("static")
    if static_path.is_dir():
        app.mount("/site", StaticFiles(directory=str(static_path), html=True), name="static")
except Exception:
    pass


LANG_CODES = {
    "auto": "Auto-detect", "en": "English", "ru": "Russian", "de": "German",
    "fr": "French", "es": "Spanish", "it": "Italian", "pt": "Portuguese",
    "nl": "Dutch", "pl": "Polish", "uk": "Ukrainian", "be": "Belarusian",
    "bg": "Bulgarian", "cs": "Czech", "sk": "Slovak", "sr": "Serbian",
    "hr": "Croatian", "tr": "Turkish", "ar": "Arabic", "zh": "Chinese",
    "ja": "Japanese", "ko": "Korean",
}


@app.get("/")
def root():
    return {
        "name": "Russian Verb Conjugation API",
        "version": "1.5.0",
        "description": "Free API for conjugating Russian verbs. Translate from any language + conjugate.",
        "base_url": "https://ru-api-free.onrender.com",
        "docs": "/docs",
        "web_ui": "/site",
        "endpoints": {
            "conjugate": {
                "url": "/conjugate?verb={verb}",
                "method": "GET",
                "description": "Conjugate a Russian verb in all tenses",
                "params": {"verb": "Russian infinitive (e.g., читать, говорить)"},
                "example_request": "/conjugate?verb=читать",
            },
            "translate": {
                "url": "/translate?text={text}&source={lang}&target={lang}",
                "method": "GET",
                "description": "Translate any word to Russian and conjugate if it's a verb",
                "params": {
                    "text": "Word to translate (required)",
                    "source": "Source language code (default: auto)",
                    "target": "Target language code (default: ru)",
                },
                "supported_langs": LANG_CODES,
                "example_requests": {
                    "english_verb": "/translate?text=speak",
                    "german_verb": "/translate?text=sprechen&source=de",
                    "french_noun": "/translate?text=livre&source=fr",
                    "to_english": "/translate?text=читать&source=ru&target=en",
                },
            },
            "verbs": {
                "url": "/verbs",
                "method": "GET",
                "description": "List all available Russian verbs in the database",
                "example_request": "/verbs",
            },
            "search": {
                "url": "/search?q={query}",
                "method": "GET",
                "description": "Search the verb database",
                "params": {"q": "Search query (e.g., чит)"},
                "example_request": "/search?q=чит",
            },
            "exceptions_list": {
                "url": "/exceptions",
                "method": "GET",
                "description": "List all verbs with conjugation exceptions",
                "example_request": "/exceptions",
            },
            "exceptions_verb": {
                "url": "/exceptions/{verb}",
                "method": "GET",
                "description": "Get exceptions for a specific verb",
                "example_request": "/exceptions/бежать",
            },
            "pluralise": {
                "url": "/pluralise?text={word}&source={lang}",
                "method": "GET",
                "description": "Translate a word to Russian and get its plural form",
                "params": {
                    "text": "Word to pluralise (required)",
                    "source": "Source language code (default: auto)",
                },
                "example_requests": {
                    "english_noun": "/pluralise?text=house",
                    "german_noun": "/pluralise?text=Haus&source=de",
                    "russian_noun": "/pluralise?text=дом",
                },
            },
            "decline": {
                "url": "/decline?text={word}&source={lang}",
                "method": "GET",
                "description": "Translate a word to Russian and get all 6 noun cases (nominative, genitive, dative, accusative, instrumental, prepositional) in both singular and plural",
                "params": {
                    "text": "Word to decline (required)",
                    "source": "Source language code (default: auto)",
                },
                "example_requests": {
                    "english_noun": "/decline?text=house",
                    "german_noun": "/decline?text=Haus&source=de",
                    "russian_noun": "/decline?text=дом",
                },
            },
            "decline_adjective": {
                "url": "/decline-adjective?text={adj}&source={lang}",
                "method": "GET",
                "description": "Decline a Russian adjective in all genders and cases. Enter the masculine nominative form (e.g., новый, синий, хороший). Supports auto-translate from any language.",
                "params": {
                    "text": "Adjective to decline (required)",
                    "source": "Source language code (default: auto)",
                    "animate": "If true, accusative = genitive for masculine/plural (default: false)",
                },
                "example_requests": {
                    "english": "/decline-adjective?text=new",
                    "russian": "/decline-adjective?text=новый",
                    "german": "/decline-adjective?text=neu&source=de",
                },
            },
        },
        "code_examples": {
            "javascript_fetch": """// Use on your website
async function conjugate(word) {
  const res = await fetch(`/translate?text=${encodeURIComponent(word)}&source=auto&target=ru`);
  return await res.json();
}
conjugate('speak').then(data => console.log(data));""",
            "curl": """# Conjugate a Russian verb
curl "https://ru-api-free.onrender.com/conjugate?verb=читать"

# Translate from any language + conjugate
curl "https://ru-api-free.onrender.com/translate?text=speak"
curl "https://ru-api-free.onrender.com/translate?text=sprechen&source=de"
curl "https://ru-api-free.onrender.com/translate?text=lire&source=fr"

# Translate without conjugating (noun)
curl "https://ru-api-free.onrender.com/translate?text=house"

# Translate Russian to English
curl "https://ru-api-free.onrender.com/translate?text=читать&source=ru&target=en"

# List all verbs
curl "https://ru-api-free.onrender.com/verbs"

# Search verbs
curl "https://ru-api-free.onrender.com/search?q=чит"

# Pluralise nouns
curl "https://ru-api-free.onrender.com/pluralise?text=house"

# Decline nouns (all cases)
curl "https://ru-api-free.onrender.com/decline?text=house"

# Decline adjectives (all genders and cases)
curl "https://ru-api-free.onrender.com/decline-adjective?text=new\"""",
            "python": """import requests

API = "https://ru-api-free.onrender.com"

# Translate + conjugate
r = requests.get(f"{API}/translate", params={"text": "speak", "source": "auto", "target": "ru"})
print(r.json())

# Just translate a noun (no conjugation)
r = requests.get(f"{API}/translate", params={"text": "house"})
print(r.json()["translated"])

# Direct conjugation
r = requests.get(f"{API}/conjugate", params={"verb": "говорить"})
print(r.json())""",
        },
    }


@app.get("/conjugate")
def get_conjugation(verb: str = Query(..., description="Russian verb in infinitive form (e.g., читать)")):
    result, status_code = conjugate(verb)
    return result


@app.get("/verbs")
def get_all_verbs():
    return {"verbs": list_verbs(), "count": len(list_verbs())}


@app.get("/exceptions")
def get_all_exceptions(exception_type: str = Query(None, description="Filter by exception type (e.g., mut_1sg, conj_class, irregular)")):
    exceptions = get_exceptions()
    if exception_type:
        filtered = {v: d for v, d in exceptions.items() if exception_type in d["types"]}
        return {"exception_type": exception_type, "description": EXCEPTION_TYPES.get(exception_type, ""), "verbs": filtered, "count": len(filtered)}
    return {"exception_types": EXCEPTION_TYPES, "verbs": exceptions, "count": len(exceptions)}


@app.get("/exceptions/{verb}")
def exceptions_for_verb(verb: str = Path(..., description="Russian verb infinitive")):
    exc = get_verb_exceptions(verb.lower().strip())
    if exc is None:
        return {"verb": verb, "exception": None, "message": "This verb follows standard conjugation rules (no exceptions)"}
    return exc


@app.get("/search")
def search(query: str = Query(..., description="Search query for verb (e.g., чит)")):
    results = search_verbs(query)
    return {"query": query, "results": results, "count": len(results)}


@app.get("/translate")
def translate_endpoint(
    text: str = Query(None, description="Text to translate (e.g., read)"),
    english: str = Query(None, description="[deprecated] Use 'text' instead"),
    source: str = Query("auto", description="Source language code (e.g., en, fr, de). Default: auto-detect"),
    target: str = Query("ru", description="Target language code (e.g., ru, en, fr). Default: ru"),
):
    inp = text or english
    if not inp:
        raise HTTPException(status_code=400, detail="Provide 'text' parameter")
    inp = inp.strip()
    translated = translate(inp, source=source, target=target)
    if not translated:
        raise HTTPException(status_code=502, detail="Translation service unavailable")
    if target == "ru" and (_looks_like_verb(translated) or translated in VERBS):
        result, status_code = conjugate(translated)
        result["original"] = inp
        result["source_lang"] = source
        result["target_lang"] = target
        result["translated"] = translated
        if result.get("generated_by_rules"):
            result["note"] = f"Conjugation generated by rules; '{translated}' was not in the exact verb database"
        return result
    return {
        "original": inp,
        "source_lang": source,
        "target_lang": target,
        "translated": translated,
        "is_verb": False,
    }


def _looks_like_verb(word):
    return any(word.endswith(e) for e in ("ть", "ти", "чь", "сти", "зти"))


@app.get("/decline")
def decline_endpoint(
    text: str = Query(None, description="Word to decline (e.g., house, дом)"),
    english: str = Query(None, description="[deprecated] Use 'text' instead"),
    source: str = Query("auto", description="Source language code (e.g., en, de, fr). Default: auto-detect"),
):
    inp = text or english
    if not inp:
        raise HTTPException(status_code=400, detail="Provide 'text' parameter")
    inp = inp.strip()

    is_cyrillic = bool(__import__("re").search(r"[а-яё]", inp))
    if is_cyrillic:
        result = decline_with_info(inp)
        result["original"] = inp
        result["source_lang"] = source
        if result.get("error"):
            result["note"] = result["message"]
        return result

    translated = translate(inp, source=source, target="ru")
    if not translated:
        raise HTTPException(status_code=502, detail="Translation service unavailable")
    result = decline_with_info(translated)
    result["original"] = inp
    result["source_lang"] = source
    result["translated"] = translated
    if result.get("error"):
        result["note"] = "Translated word is a verb, not a noun"
    return result


@app.get("/decline-adjective")
def decline_adjective_endpoint(
    text: str = Query(None, description="Adjective to decline (e.g., new, новый)"),
    english: str = Query(None, description="[deprecated] Use 'text' instead"),
    source: str = Query("auto", description="Source language code (e.g., en, de, fr). Default: auto-detect"),
    animate: bool = Query(False, description="If true, accusative = genitive for masculine and plural"),
):
    inp = text or english
    if not inp:
        raise HTTPException(status_code=400, detail="Provide 'text' parameter")
    inp = inp.strip()

    is_cyrillic = bool(__import__("re").search(r"[а-яё]", inp))
    if is_cyrillic:
        result = decline_adjective_with_info(inp, animate=animate)
        result["original"] = inp
        result["source_lang"] = source
        if result.get("error"):
            result["note"] = result["message"]
        return result

    translated = translate(inp, source=source, target="ru")
    if not translated:
        raise HTTPException(status_code=502, detail="Translation service unavailable")
    result = decline_adjective_with_info(translated, animate=animate)
    result["original"] = inp
    result["source_lang"] = source
    result["translated"] = translated
    if result.get("error"):
        result["note"] = result["message"]
    return result


@app.get("/pluralise")
def pluralise_endpoint(
    text: str = Query(None, description="Word to pluralise (e.g., house, дом)"),
    english: str = Query(None, description="[deprecated] Use 'text' instead"),
    source: str = Query("auto", description="Source language code (e.g., en, de, fr). Default: auto-detect"),
):
    inp = text or english
    if not inp:
        raise HTTPException(status_code=400, detail="Provide 'text' parameter")
    inp = inp.strip()

    is_cyrillic = bool(__import__("re").search(r"[а-яё]", inp))
    if is_cyrillic:
        result = pluralise_with_info(inp)
        result["original"] = inp
        result["source_lang"] = source
        if result["plural"] is None:
            result["note"] = "This is a verb, not a noun"
        return result

    translated = translate(inp, source=source, target="ru")
    if not translated:
        raise HTTPException(status_code=502, detail="Translation service unavailable")
    result = pluralise_with_info(translated)
    result["original"] = inp
    result["source_lang"] = source
    result["translated"] = translated
    if result["plural"] is None:
        result["note"] = "Translated word is a verb, not a noun"
    return result
