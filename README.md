# ru-api-free

Free REST API for conjugating Russian verbs in all tenses (present, past, future).
Translate words from any language to Russian — if it's a verb, you get full conjugation.

**Live API:** `https://ru-api-free.onrender.com`

---

## Quick Start (no installation)

Just use the hosted API directly:

```bash
curl "https://ru-api-free.onrender.com/translate?text=speak"
```

```javascript
// Use on your website
const res = await fetch("https://ru-api-free.onrender.com/translate?text=speak");
const data = await res.json();
console.log(data.verb, data.tenses);
```

```python
import requests

r = requests.get("https://ru-api-free.onrender.com/translate", params={"text": "speak"})
print(r.json()["tenses"]["present"]["я"])  # "говорю"
```

---

## API Endpoints

### 1. Translate + Conjugate

```
GET /translate?text={word}&source=auto&target=ru
```

| Param | Default | Description |
|---|---|---|
| `text` | — | Word to translate (required) |
| `source` | `auto` | Source language code |
| `target` | `ru` | Target language code |

**Examples:**

```bash
# English verb -> Russian + conjugation
curl "https://ru-api-free.onrender.com/translate?text=speak"

# German verb -> Russian + conjugation
curl "https://ru-api-free.onrender.com/translate?text=sprechen&source=de"

# French verb -> Russian + conjugation
curl "https://ru-api-free.onrender.com/translate?text=lire&source=fr"

# Noun -> just translation, no conjugation
curl "https://ru-api-free.onrender.com/translate?text=house"

# Russian -> English (translation only)
curl "https://ru-api-free.onrender.com/translate?text=читать&source=ru&target=en"
```

### 2. Direct Conjugation (Russian verb only)

```
GET /conjugate?verb={verb}
```

```bash
curl "https://ru-api-free.onrender.com/conjugate?verb=читать"
curl "https://ru-api-free.onrender.com/conjugate?verb=говорить"
```

### 3. List all verbs

```
GET /verbs
```

### 4. Search verbs

```
GET /search?q={query}
```

```bash
curl "https://ru-api-free.onrender.com/search?q=чит"
```

### 5. Pluralise (nouns)

Translate any word to Russian and get its plural form. Handles 150+ irregular plurals.

```
GET /pluralise?text={word}&source=auto
```

| Param | Default | Description |
|---|---|---|
| `text` | — | Word to pluralise (required) |
| `source` | `auto` | Source language code |

```bash
curl "https://ru-api-free.onrender.com/pluralise?text=house"
curl "https://ru-api-free.onrender.com/pluralise?text=Haus&source=de"
curl "https://ru-api-free.onrender.com/pluralise?text=дом"
```

```javascript
const res = await fetch("https://ru-api-free.onrender.com/pluralise?text=book");
const data = await res.json();
console.log(data.singular, "→", data.plural);  // "книга → книги"
```

**Response:**
```json
{
  "singular": "дом",
  "plural": "дома",
  "gender": "masculine",
  "original": "house",
  "translated": "дом"
}
```

### 6. Decline (noun cases)

Translate any word to Russian and get all 6 noun cases in singular and plural (nominative, genitive, dative, accusative, instrumental, prepositional).

```
GET /decline?text={word}&source=auto
```

| Param | Default | Description |
|---|---|---|
| `text` | — | Word to decline (required) |
| `source` | `auto` | Source language code |

```bash
curl "https://ru-api-free.onrender.com/decline?text=house"
curl "https://ru-api-free.onrender.com/decline?text=дом"
```

```javascript
const res = await fetch("https://ru-api-free.onrender.com/decline?text=book");
const data = await res.json();
console.log(data.singular.genitive);  // "книги"
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
  }
}
```

### 7. Conjugation exceptions

```
GET /exceptions              # All exceptions
GET /exceptions/{verb}       # Exceptions for one verb
```

---

## Response Format

```json
{
  "verb": "говорить",
  "aspect": "imperfective",
  "conjugation_type": 2,
  "reflexive": false,
  "tenses": {
    "present": {
      "я": "говорю",
      "ты": "говоришь",
      "он/она/оно": "говорит",
      "мы": "говорим",
      "вы": "говорите",
      "они": "говорят"
    },
    "past": {
      "мужской": "говорил",
      "женский": "говорила",
      "средний": "говорило",
      "множественное": "говорили"
    },
    "future": {
      "я": "буду говорить",
      "ты": "будешь говорить",
      "он/она/оно": "будет говорить",
      "мы": "будем говорить",
      "вы": "будете говорить",
      "они": "будут говорить"
    }
  }
}
```

### Language codes

`auto`, `en`, `ru`, `de`, `fr`, `es`, `it`, `pt`, `nl`, `pl`, `uk`, `be`, `bg`, `cs`, `sk`, `sr`, `hr`, `tr`, `ar`, `zh`, `ja`, `ko`

---

## Self-Hosting

```bash
pip install ru-api-free
ru-api-free
# or: uvicorn ru_api_free.main:app --host 0.0.0.0 --port 8000
```

CORS is enabled for all origins — use it directly from any website.

## Python Library (no server needed)

```python
from ru_api_free import conjugate, translate, pluralise, decline

result, status = conjugate("читать")
print(result["tenses"]["present"]["я"])  # "читаю"

russian = translate("speak", source="auto", target="ru")
print(russian)  # "говорить"

info = pluralise("дом")
print(info["singular"], "→", info["plural"])  # "дом → дома"

cases = decline("дом")
print(cases["singular"]["genitive"])  # "дома"
```

## License

MIT
