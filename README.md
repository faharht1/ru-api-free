# ru-api-free

Free REST API for Russian morphology: verb conjugation, noun pluralisation, noun case declension, and adjective declension. Translate words from any language to Russian — if it's a verb, you get full conjugation.

**Live API:** `https://ru-api-free.onrender.com`

**Website frontend:** `https://ru-api-free.onrender.com/site`

**PyPI package:** [`ru-api-free`](https://pypi.org/project/ru-api-free/)

**GitHub repo:** [`faharht1/ru-api-free`](https://github.com/faharht1/ru-api-free)

---

## Quick Start

```bash
# Translate + conjugate any verb
curl "https://ru-api-free.onrender.com/translate?text=speak"

# Pluralise a noun
curl "https://ru-api-free.onrender.com/pluralise?text=house"

# Decline a noun (all 6 cases × 2 numbers)
curl "https://ru-api-free.onrender.com/decline?text=book"

# Decline an adjective (all genders × 6 cases)
curl "https://ru-api-free.onrender.com/decline-adjective?text=new"

# Get aspect pair (imperfective ↔ perfective)
curl "https://ru-api-free.onrender.com/aspect-pair?text=speak"
curl "https://ru-api-free.onrender.com/aspect-pair?text=читать"
```

```javascript
const res = await fetch("https://ru-api-free.onrender.com/translate?text=speak");
const data = await res.json();
console.log(data.verb, data.tenses.present["я"]); // "говорить говорю"
```

```python
import requests

r = requests.get("https://ru-api-free.onrender.com/translate", params={"text": "speak"})
print(r.json()["tenses"]["present"]["я"])  # "говорю"
```

---

## API Endpoints

### Endpoint overview

| Endpoint | Description |
|---|---|
| `GET /translate` | Translate any word; if it's a verb, conjugate it |
| `GET /conjugate` | Conjugate a Russian verb directly |
| `GET /verbs` | List all supported Russian verbs |
| `GET /search` | Search verbs by substring |
| `GET /exceptions` | List all conjugation exceptions |
| `GET /exceptions/{verb}` | Get exceptions for a specific verb |
| `GET /pluralise` | Pluralise a noun |
| `GET /decline` | Decline a noun (6 cases × singular/plural) |
| `GET /decline-adjective` | Decline an adjective (2 genders × 6 cases + plural) |
| `GET /aspect-pair` | Get aspect pair (imperfective ↔ perfective) with both conjugated |
| `GET /site` | Interactive web UI |

---

### 1. Translate + Conjugate

```
GET /translate?text={word}&source=auto&target=ru
```

| Param | Default | Description |
|---|---|---|
| `text` | — | Word to translate **(required)** |
| `source` | `auto` | Source language code |
| `target` | `ru` | Target language code |

**Behaviour:**
- If the translated word is a known Russian verb → returns full conjugation table
- If it's a noun / other → returns just the translation
- Supports any language via auto-detect

**Examples:**

```bash
# English verb → conjugation
curl "https://ru-api-free.onrender.com/translate?text=speak"

# German verb → conjugation
curl "https://ru-api-free.onrender.com/translate?text=sprechen&source=de"

# French verb → conjugation
curl "https://ru-api-free.onrender.com/translate?text=lire&source=fr"

# Spanish verb → conjugation
curl "https://ru-api-free.onrender.com/translate?text=hablar&source=es"

# Noun → translation only
curl "https://ru-api-free.onrender.com/translate?text=house"

# Russian → English
curl "https://ru-api-free.onrender.com/translate?text=читать&source=ru&target=en"

# Polish word → translation
curl "https://ru-api-free.onrender.com/translate?text=pić&source=pl"
```

**Response (verb):**
```json
{
  "verb": "говорить",
  "aspect": "imperfective",
  "conjugation_type": 2,
  "reflexive": false,
  "tenses": {
    "present": { "я": "говорю", "ты": "говоришь", "он/она/оно": "говорит", "мы": "говорим", "вы": "говорите", "они": "говорят" },
    "past": { "мужской": "говорил", "женский": "говорила", "средний": "говорило", "множественное": "говорили" },
    "future": { "я": "буду говорить", "ты": "будешь говорить", "он/она/оно": "будет говорить", "мы": "будем говорить", "вы": "будете говорить", "они": "будут говорить" }
  },
  "original": "speak",
  "translated": "говорить",
  "source_lang": "en"
}
```

**Response (noun):**
```json
{
  "original": "house",
  "translated": "дом",
  "source_lang": "en",
  "note": "дом is not a verb in our dictionary"
}
```

---

### 2. Direct Conjugation

```
GET /conjugate?verb={verb}
```

Conjugate a Russian verb directly without translation.

| Param | Description |
|---|---|
| `verb` | Russian infinitive **(required)** |

```bash
curl "https://ru-api-free.onrender.com/conjugate?verb=читать"
curl "https://ru-api-free.onrender.com/conjugate?verb=говорить"
curl "https://ru-api-free.onrender.com/conjugate?verb=мыть"
```

Returns the same response format as `/translate` but without `original`, `translated`, or `source_lang` fields.

---

### 3. List all verbs

```
GET /verbs
```

Returns a JSON object with all supported Russian verbs grouped by conjugation type.

```bash
curl "https://ru-api-free.onrender.com/verbs"
```

---

### 4. Search verbs

```
GET /search?q={query}
```

Search the verb dictionary by substring.

| Param | Description |
|---|---|
| `q` | Search query **(required)** |

```bash
curl "https://ru-api-free.onrender.com/search?q=чит"
curl "https://ru-api-free.onrender.com/search?q=гов"
```

Returns matching verbs with conjugation type, stem, and endings.

---

### 5. Pluralise (nouns)

```
GET /pluralise?text={word}&source=auto
```

Translate any word to Russian and get its plural form. Handles 150+ irregular plurals.

| Param | Default | Description |
|---|---|---|
| `text` | — | Word to pluralise **(required)** |
| `source` | `auto` | Source language code |

```bash
curl "https://ru-api-free.onrender.com/pluralise?text=house"
curl "https://ru-api-free.onrender.com/pluralise?text=Haus&source=de"
curl "https://ru-api-free.onrender.com/pluralise?text=дом"
curl "https://ru-api-free.onrender.com/pluralise?text=книга"
curl "https://ru-api-free.onrender.com/pluralise?text=окно"
```

**Response:**
```json
{
  "singular": "дом",
  "plural": "дома",
  "gender": "masculine",
  "original": "house",
  "translated": "дом",
  "source_lang": "en"
}
```

**Irregulars covered:** человек → люди, ребёнок → дети, друг → друзья, сын → сыновья, брат → братья, муж → мужья, дерево → деревья, лист → листья, стул → стулья, платье → платья, крыло → крылья, перо → перья, ухо → уши, плечо → плечи, колено → колени, яблоко → яблоки, облако → облака, море → моря, поле → поля, сердце → сердца, апельсин → апельсины, помидор → помидоры, сосед → соседи, чертёнок → чертенята, иностранец → иностранцы, славянин → славяне, римлянин → римляне, цыган → цыгане, господин → господа, хозяин → хозяева, шурин → шурья, кум → кумовья, князь → князья — and 120+ more.

---

### 6. Decline (noun cases)

```
GET /decline?text={word}&source=auto&animate=false
```

Translate any word to Russian and get all 6 noun cases in singular and plural.

| Param | Default | Description |
|---|---|---|
| `text` | — | Word to decline **(required)** |
| `source` | `auto` | Source language code |
| `animate` | `false` | If true, accusative = genitive for masculine animate nouns |

```bash
curl "https://ru-api-free.onrender.com/decline?text=house"
curl "https://ru-api-free.onrender.com/decline?text=дом"
curl "https://ru-api-free.onrender.com/decline?text=книга"
curl "https://ru-api-free.onrender.com/decline?text=море"
curl "https://ru-api-free.onrender.com/decline?text=мать"
curl "https://ru-api-free.onrender.com/decline?text=ими"
curl "https://ru-api-free.onrender.com/decline?text=Haus&source=de"
```

**Response:**
```json
{
  "word": "дом",
  "gender": "masculine",
  "declension": "first",
  "singular": {
    "nominative": "дом",
    "genitive": "дома",
    "dative": "дому",
    "accusative": "дом",
    "instrumental": "домом",
    "prepositional": "доме"
  },
  "plural": {
    "nominative": "дома",
    "genitive": "домов",
    "dative": "домам",
    "accusative": "дома",
    "instrumental": "домами",
    "prepositional": "домах"
  },
  "original": "house",
  "translated": "дом",
  "source_lang": "en"
}
```

**Special nouns handled:** путь, дитя, мать, дочь, время, имя, бремя, вымя, знамя, пламя, племя, семя, стремя, темя, and other -мя neuters. Also handles feminine nouns ending in -ь (мышь, дверь, площадь, любовь, etc.).

---

### 7. Decline Adjective

```
GET /decline-adjective?text={adj}&source=auto&animate=false
```

Decline a Russian adjective in all genders and cases. Enter the masculine nominative form.

| Param | Default | Description |
|---|---|---|
| `text` | — | Adjective to decline **(required)** |
| `source` | `auto` | Source language code |
| `animate` | `false` | If true, accusative = genitive for masculine and plural |

```bash
curl "https://ru-api-free.onrender.com/decline-adjective?text=new"
curl "https://ru-api-free.onrender.com/decline-adjective?text=новый"
curl "https://ru-api-free.onrender.com/decline-adjective?text=neu&source=de"
curl "https://ru-api-free.onrender.com/decline-adjective?text=синий"
curl "https://ru-api-free.onrender.com/decline-adjective?text=хороший"
curl "https://ru-api-free.onrender.com/decline-adjective?text=большой"
curl "https://ru-api-free.onrender.com/decline-adjective?text=маленький"
```

**Response:**
```json
{
  "adjective": "новый",
  "type": "hard",
  "forms": {
    "masculine": {
      "nominative": "новый",
      "genitive": "нового",
      "dative": "новому",
      "accusative": "новый",
      "instrumental": "новым",
      "prepositional": "новом"
    },
    "feminine": {
      "nominative": "новая",
      "genitive": "новой",
      "dative": "новой",
      "accusative": "новую",
      "instrumental": "новой",
      "prepositional": "новой"
    },
    "neuter": {
      "nominative": "новое",
      "genitive": "нового",
      "dative": "новому",
      "accusative": "новое",
      "instrumental": "новым",
      "prepositional": "новом"
    },
    "plural": {
      "nominative": "новые",
      "genitive": "новых",
      "dative": "новым",
      "accusative": "новые",
      "instrumental": "новыми",
      "prepositional": "новых"
    }
  },
  "original": "new",
  "translated": "новый",
  "source_lang": "en"
}
```

**Adjective types supported:**

| Type | Ending | Examples |
|---|---|---|
| `hard` | -ый | новый, белый, старый, красный |
| `hard_stressed` | -ой (non-sibilant) | прямой, простой, рябой |
| `soft` | -ий (after soft consonant) | синий, древний, летний |
| `sibilant` | -ий (after ш, ж, ч, щ) | хороший, свежий, горячий |
| `sibilant_stressed` | -ой (after sibilant) | большой, чужой |
| `velar` | -ий (after г, к, х) | маленький, русский, великий |

---

### 8. Aspect Pair

```
GET /aspect-pair?text={verb}&source=auto
```

Enter any verb (in any language) and get its aspect pair — the imperfective ↔ perfective counterpart — with both verbs fully conjugated side by side.

| Param | Default | Description |
|---|---|---|
| `text` | — | Verb to get aspect pair for **(required)** |
| `source` | `auto` | Source language code |

Covers 200+ verb pairs including prefixes (делать → сделать, читать → прочитать), suppletive pairs (говорить → сказать, брать → взять), and suffix pairs (прыгать → прыгнуть).

```bash
curl "https://ru-api-free.onrender.com/aspect-pair?text=speak"
curl "https://ru-api-free.onrender.com/aspect-pair?text=читать"
curl "https://ru-api-free.onrender.com/aspect-pair?text=kaufen&source=de"
curl "https://ru-api-free.onrender.com/aspect-pair?text=сказать"
```

**Response:**
```json
{
  "verb": "говорить",
  "aspect": "imperfective",
  "pair_type": "suppletive",
  "counterpart": "сказать",
  "counterpart_aspect": "perfective",
  "main_verb": { "verb": "говорить", "aspect": "imperfective", "tenses": { ... } },
  "counterpart_verb": { "verb": "сказать", "aspect": "perfective", "tenses": { ... } },
  "note": "Completely different roots (говор- vs скаж-)",
  "original": "speak",
  "translated": "говорить",
  "source_lang": "en"
}
```

**Pair types:**
- `prefix` — perfective formed by adding a prefix (делать → с-делать)
- `suppletive` — different roots/ stems (говорить → сказать)
- `likely_prefix` — inferred from existing data

---

### 9. Exceptions

```
GET /exceptions
GET /exceptions/{verb}
```

List all conjugation exceptions, or get detailed exception info for a specific verb.

```bash
curl "https://ru-api-free.onrender.com/exceptions"
curl "https://ru-api-free.onrender.com/exceptions/брить"
curl "https://ru-api-free.onrender.com/exceptions/гнать"
```

**Exception types returned:**
- `сти` verbs (нести, вести, etc.)
- `чь` verbs (мочь, печь, etc.)
- 1st-conjugation `ить` verbs (брить, стелить)
- 2nd-conjugation `ать`/`ять`/`еть` verbs (гнать, держать, слышать, etc.)
- `овать`→`ую` verbs (требовать, рисовать)
- `нуть` verbs (гибнуть, мёрзнуть)
- `ереть` verbs (тереть, умереть)
- `олать`→`олю` verbs (колоть, полоть)
- `овать`→`ую` with consonant mutation
- `зти`→`ззу` verbs (везти, лезть)
- `сти`→`слу` verbs (расти, цвести)
- `сти`→`сду` verbs (блясти, чести)
- `еречь`→`регу` verbs (беречь, стеречь)
- `ивать`→`ую` verbs
- Miscellaneous (ехать, дать, есть)

---

### 10. Interactive Web UI

```
GET /site
```

Opens a full-featured web interface with tabs for Conjugate, Pluralise, Decline, Decline Adj, and Aspect Pair modes. Includes a language selector dropdown for source language.

```
https://ru-api-free.onrender.com/site
```

---

## Python Library (no server needed)

Install the package and use it directly:

```bash
pip install ru-api-free
```

```python
from ru_api_free import (
    conjugate, search_verbs, list_verbs,
    translate, translate_en_to_ru,
    pluralise, pluralise_with_info,
    decline, decline_with_info,
    decline_adjective, decline_adjective_with_info,
    get_aspect_pair,
    get_exceptions, get_verb_exceptions, EXCEPTION_TYPES,
)
```

### Conjugation

```python
result, status = conjugate("читать")
print(result["tenses"]["present"]["я"])   # читаю
print(result["tenses"]["past"]["женский"])  # читала
print(result["tenses"]["future"]["мы"])    # будем читать
```

### Translation

```python
russian = translate("speak", source="auto", target="ru")
print(russian)  # говорить

# Also returns Russian from English directly
eng = translate_en_to_ru("house")
print(eng)  # дом
```

### Pluralise

```python
info = pluralise("дом")
print(info["singular"], "→", info["plural"])  # "дом → дома"

# With metadata
info2 = pluralise_with_info("книга")
print(info2["gender"])       # feminine
print(info2["plural"])        # книги
print(info2["singular"])      # книга
```

### Noun Declension

```python
cases = decline("дом")
print(cases["singular"]["genitive"])   # дома
print(cases["plural"]["dative"])       # домам

# With metadata
cases2 = decline_with_info("книга")
print(cases2["gender"])               # feminine
print(cases2["declension"])           # second
print(cases2["plural"]["accusative"])  # книги
```

### Adjective Declension

```python
adj = decline_adjective("новый")
print(adj["masculine"]["instrumental"])  # новым
print(adj["feminine"]["accusative"])     # новую
print(adj["plural"]["prepositional"])    # новых

# With type info
adj2 = decline_adjective_with_info("хороший")
print(adj2["type"])   # sibilant
print(adj2["forms"]["feminine"]["genitive"])  # хорошей

### Aspect Pair

```python
pair = get_aspect_pair("читать")
print(pair["perfective"])  # прочитать
print(pair["type"])        # prefix

pair2 = get_aspect_pair("сказать")
print(pair2["imperfective"])  # говорить
print(pair2["type"])          # suppletive
```
```

### Search & List

```python
verbs = list_verbs()  # all verbs by conjugation type
results = search_verbs("чит")
print(results)  # matching verbs
```

### Exceptions

```python
all_exceptions = get_exceptions()
print(all_exceptions.keys())  # exception type names

verb_ex = get_verb_exceptions("брить")
print(verb_ex)
```

---

## Self-Hosting

### Option 1: pip install

```bash
pip install ru-api-free
ru-api-free
# Server starts at http://0.0.0.0:8000
```

### Option 2: Direct uvicorn

```bash
pip install ru-api-free uvicorn
python -m uvicorn ru_api_free.main:app --host 127.0.0.1 --port 5000
```

### Option 3: Render deployment

1. Fork the repo: `https://github.com/faharht1/ru-api-free`
2. Connect to Render as a Web Service
3. **Start command:** `uvicorn ru_api_free.main:app --host 0.0.0.0 --port $PORT`
4. Deploy

CORS is enabled for all origins — use it directly from any website.

---

## Language Codes

```
auto  - Auto-detect
en    - English
ru    - Russian
de    - German
fr    - French
es    - Spanish
it    - Italian
pt    - Portuguese
nl    - Dutch
pl    - Polish
uk    - Ukrainian
be    - Belarusian
bg    - Bulgarian
cs    - Czech
sk    - Slovak
sr    - Serbian
hr    - Croatian
tr    - Turkish
ar    - Arabic
zh    - Chinese
ja    - Japanese
ko    - Korean
```

Pass `source=pl` for Polish words, `source=de` for German words, etc.

---

## CLI Usage

When installed via pip, the `ru-api-free` command starts the server:

```bash
ru-api-free
# Running on http://0.0.0.0:8000
```

Or use `--port` to change the port (check `ru-api-free --help` for options).

CORS is enabled for all origins.

---

## Local Development

```bash
git clone https://github.com/faharht1/ru-api-free.git
cd ru-api-free

# Install in editable mode
pip install -e .

# Start dev server
python -m uvicorn ru_api_free.main:app --host 127.0.0.1 --port 5000 --reload

# Open http://127.0.0.1:5000/site
```

---

## Response Format Summary

All endpoints return JSON. Common fields:

| Field | Description |
|---|---|
| `original` | The original input word (if applicable) |
| `translated` | The Russian translation (if applicable) |
| `source_lang` | Detected or provided source language |
| `note` / `message` | Error or informational message |
| `tenses` | Verb conjugation table (present / past / future) |
| `singular` / `plural` | Noun case tables (decline) or plural (pluralise) |
| `masculine` / `feminine` / `neuter` / `plural` | Adjective case tables |

---

## License

MIT
