ADJ_ENDINGS = {
    "hard": {
        "masculine": {"nom": "ый", "gen": "ого", "dat": "ому", "ins": "ым", "pre": "ом"},
        "feminine":  {"nom": "ая", "gen": "ой", "dat": "ой", "ins": "ой", "pre": "ой", "acc": "ую"},
        "neuter":    {"nom": "ое", "gen": "ого", "dat": "ому", "ins": "ым", "pre": "ом"},
        "plural":    {"nom": "ые", "gen": "ых", "dat": "ым", "ins": "ыми", "pre": "ых"},
    },
    "soft": {
        "masculine": {"nom": "ий", "gen": "его", "dat": "ему", "ins": "им", "pre": "ем"},
        "feminine":  {"nom": "яя", "gen": "ей", "dat": "ей", "ins": "ей", "pre": "ей", "acc": "юю"},
        "neuter":    {"nom": "ее", "gen": "его", "dat": "ему", "ins": "им", "pre": "ем"},
        "plural":    {"nom": "ие", "gen": "их", "dat": "им", "ins": "ими", "pre": "их"},
    },
    "sibilant": {
        "masculine": {"nom": "ий", "gen": "его", "dat": "ему", "ins": "им", "pre": "ем"},
        "feminine":  {"nom": "ая", "gen": "ей", "dat": "ей", "ins": "ей", "pre": "ей", "acc": "ую"},
        "neuter":    {"nom": "ее", "gen": "его", "dat": "ему", "ins": "им", "pre": "ем"},
        "plural":    {"nom": "ие", "gen": "их", "dat": "им", "ins": "ими", "pre": "их"},
    },
    "sibilant_stressed": {
        "masculine": {"nom": "ой", "gen": "ого", "dat": "ому", "ins": "им", "pre": "ом"},
        "feminine":  {"nom": "ая", "gen": "ой", "dat": "ой", "ins": "ой", "pre": "ой", "acc": "ую"},
        "neuter":    {"nom": "ое", "gen": "ого", "dat": "ому", "ins": "им", "pre": "ом"},
        "plural":    {"nom": "ие", "gen": "их", "dat": "им", "ins": "ими", "pre": "их"},
    },
    "velar": {
        "masculine": {"nom": "ий", "gen": "ого", "dat": "ому", "ins": "им", "pre": "ом"},
        "feminine":  {"nom": "ая", "gen": "ой", "dat": "ой", "ins": "ой", "pre": "ой", "acc": "ую"},
        "neuter":    {"nom": "ое", "gen": "ого", "dat": "ому", "ins": "им", "pre": "ом"},
        "plural":    {"nom": "ие", "gen": "их", "dat": "им", "ins": "ими", "pre": "их"},
    },
    "hard_stressed": {
        "masculine": {"nom": "ой", "gen": "ого", "dat": "ому", "ins": "ым", "pre": "ом"},
        "feminine":  {"nom": "ая", "gen": "ой", "dat": "ой", "ins": "ой", "pre": "ой", "acc": "ую"},
        "neuter":    {"nom": "ое", "gen": "ого", "dat": "ому", "ins": "ым", "pre": "ом"},
        "plural":    {"nom": "ые", "gen": "ых", "dat": "ым", "ins": "ыми", "pre": "ых"},
    },
}

_SIB = set("жшщч")
_VEL = set("гкх")


def decline_adjective(word):
    w = word.lower().strip()
    adj_type, stem = _detect_type(w)
    if adj_type is None:
        return None

    endings = ADJ_ENDINGS[adj_type]
    out = {}
    for gender in ("masculine", "feminine", "neuter", "plural"):
        gend = endings[gender]
        nom = stem + gend["nom"]
        gen = stem + gend["gen"]
        dat = stem + gend["dat"]
        ins = stem + gend["ins"]
        pre = stem + gend["pre"]
        if "acc" in gend:
            acc = stem + gend["acc"]
        else:
            acc = nom
        out[gender] = {
            "nominative": nom,
            "genitive": gen,
            "dative": dat,
            "accusative": acc,
            "instrumental": ins,
            "prepositional": pre,
        }

    return {
        "adjective": w,
        "stem": stem,
        "type": adj_type,
        "forms": out,
    }


def decline_adjective_with_info(word, animate=False):
    w = word.strip().lower()
    r = decline_adjective(w)
    if r is None:
        return {"error": True, "message": f"'{w}' is not a recognisable adjective. Enter the masculine nominative form (e.g., новый, синий)."}
    if animate:
        for gender in ("masculine", "plural"):
            r["forms"][gender]["accusative"] = r["forms"][gender]["genitive"]
    return r


def _detect_type(word):
    w = word.lower().strip()

    if w.endswith("ый"):
        stem = w[:-2]
        if stem and stem[-1] in _VEL:
            return None
        if stem and stem[-1] in _SIB:
            return None
        return "hard", stem

    if w.endswith("ой"):
        stem = w[:-2]
        if stem and stem[-1] in _SIB:
            return "sibilant_stressed", stem
        return "hard_stressed", stem

    if w.endswith("ий"):
        stem = w[:-2]
        if not stem:
            return None, None
        if stem[-1] in _SIB:
            return "sibilant", stem
        if stem[-1] in _VEL:
            return "velar", stem
        if stem.endswith("ь"):
            stem = stem[:-1]
            return "soft", stem
        if _is_possessive(w, stem):
            return "possessive", stem
        return "soft", stem

    return None, None


def _is_possessive(word, stem):
    poss_adj = {"лисий", "волчий", "медвежий", "заячий", "собачий", "кошачий",
                "рыбий", "птичий", "козий", "овечий", "коровий", "лошадиный"}
    if word in poss_adj:
        return True
    if stem.endswith(("ий", "ий")):
        return word.endswith(("ий", "ий")) and not stem[-2:] in _SIB and not stem[-2:] in _VEL
    return False
