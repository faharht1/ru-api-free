# ru-api-free

Free REST API for conjugating Russian verbs in all tenses (present, past, future). \
Translate words from any language to Russian — if it's a verb, you get full conjugation.

## Quick Start

### Run the server

```bash
pip install ru-api-free
ru-api-free
```

Open **http://localhost:8000** for API docs, or **http://localhost:8000/site** for the web UI.

---

## API Endpoints

### 1. Translate + Conjugate (most useful)

Auto-detect any language, translate to Russian, then conjugate if it's a verb.

```
GET /translate?text={word}&source=auto&target=ru
```

| Param | Default | Description |
|---|---|---|
| `text` | — | Word to translate (required) |
| `source` | `auto` | Source language code (`en`, `de`, `fr`, `es`, `pl`, `uk`…) |
| `target` | `ru` | Target language code |

**Examples:**

```
/translate?text=speak          # English → Russian + conjugate
/translate?text=sprechen&source=de  # German → Russian + conjugate
/translate?text=house          # English → Russian (noun, no conjugation)
/translate?text=читать&source=ru&target=en  # Russian → English translation only
```

**JavaScript (use on your website):**

```javascript
async function conjugate(word) {
  const res = await fetch(`/translate?text=${encodeURIComponent(word)}&source=auto&target=ru`);
  return await res.json();
}

// Usage
conjugate('speak').then(data => {
  console.log(data.verb);        // "говорить"
  console.log(data.tenses);      // { present: {...}, past: {...}, future: {...} }
});
```

**Python:**

```python
import requests

r = requests.get("http://localhost:8000/translate", params={"text": "speak"})
data = r.json()
print(data["verb"])             # "говорить"
print(data["tenses"]["present"])  # {"я": "говорю", "ты": "говоришь", ...}
```

**cURL:**

```bash
curl "http://localhost:8000/translate?text=speak"
```

### 2. Direct Conjugation (Russian verb only)

```
GET /conjugate?verb={verb}
```

```bash
curl "http://localhost:8000/conjugate?verb=читать"
```

```javascript
fetch("/conjugate?verb=говорить").then(r => r.json()).then(console.log);
```

### 3. List all verbs

```
GET /verbs
```

Returns all 190+ Russian verbs in the database with aspect and reflexive info.

### 4. Search verbs

```
GET /search?q={query}
```

```bash
curl "http://localhost:8000/search?q=чит"
```

### 5. Conjugation exceptions

```
GET /exceptions              # All exceptions
GET /exceptions/{verb}       # Exceptions for one verb
```

---

## Response Format

A conjugation response looks like:

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

## Python Library

You can also use the library directly without running a server:

```python
from ru_api_free import conjugate, translate

# Conjugate directly
result, status = conjugate("читать")
print(result["tenses"]["present"]["я"])  # "читаю"

# Translate (no server needed)
russian = translate("speak", source="auto", target="ru")
print(russian)  # "говорить"
```

---

## Self-Hosting

```bash
pip install ru-api-free
ru-api-free
# or: uvicorn ru_api_free.main:app --host 0.0.0.0 --port 8000
```

The API has CORS enabled for all origins — use it directly from any website.

## License

MIT
"# ru-api-free" 
