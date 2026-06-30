IRREGULAR_DECLENSION = {
    "мать": {
        "gender": "f",
        "singular": {"nominative": "мать", "genitive": "матери", "dative": "матери",
                     "accusative": "мать", "instrumental": "матерью", "prepositional": "матери"},
        "plural": {"nominative": "матери", "genitive": "матерей", "dative": "матерям",
                   "accusative": "матерей", "instrumental": "матерями", "prepositional": "матерях"},
    },
    "дочь": {
        "gender": "f",
        "singular": {"nominative": "дочь", "genitive": "дочери", "dative": "дочери",
                     "accusative": "дочь", "instrumental": "дочерью", "prepositional": "дочери"},
        "plural": {"nominative": "дочери", "genitive": "дочерей", "dative": "дочерям",
                   "accusative": "дочерей", "instrumental": "дочерями", "prepositional": "дочерях"},
    },
    "дитя": {
        "gender": "n",
        "singular": {"nominative": "дитя", "genitive": "дитяти", "dative": "дитяти",
                     "accusative": "дитя", "instrumental": "дитятей", "prepositional": "дитяти"},
        "plural": {"nominative": "дети", "genitive": "детей", "dative": "детям",
                   "accusative": "детей", "instrumental": "детьми", "prepositional": "детях"},
    },
    "человек": {
        "gender": "m",
        "singular": {"nominative": "человек", "genitive": "человека", "dative": "человеку",
                     "accusative": "человека", "instrumental": "человеком", "prepositional": "человеке"},
        "plural": {"nominative": "люди", "genitive": "людей", "dative": "людям",
                   "accusative": "людей", "instrumental": "людьми", "prepositional": "людях"},
    },
    "ребёнок": {
        "gender": "m",
        "singular": {"nominative": "ребёнок", "genitive": "ребёнка", "dative": "ребёнку",
                     "accusative": "ребёнка", "instrumental": "ребёнком", "prepositional": "ребёнке"},
        "plural": {"nominative": "ребята", "genitive": "ребят", "dative": "ребятам",
                   "accusative": "ребят", "instrumental": "ребятами", "prepositional": "ребятах"},
    },
    "судья": {
        "gender": "m",
        "singular": {"nominative": "судья", "genitive": "судьи", "dative": "судье",
                     "accusative": "судью", "instrumental": "судьёй", "prepositional": "судье"},
        "plural": {"nominative": "судьи", "genitive": "судей", "dative": "судьям",
                   "accusative": "судей", "instrumental": "судьями", "prepositional": "судьях"},
    },
    "дядя": {
        "gender": "m",
        "singular": {"nominative": "дядя", "genitive": "дяди", "dative": "дяде",
                     "accusative": "дядю", "instrumental": "дядей", "prepositional": "дяде"},
    },
    "путь": {
        "gender": "m",
        "singular": {"nominative": "путь", "genitive": "пути", "dative": "пути",
                     "accusative": "путь", "instrumental": "путём", "prepositional": "пути"},
        "plural": {"nominative": "пути", "genitive": "путей", "dative": "путям",
                   "accusative": "пути", "instrumental": "путями", "prepositional": "путях"},
    },
}

NEUTER_MYA = {"время", "имя", "знамя", "темя", "вымя", "пламя", "племя", "семя", "стремя", "бремя"}

MASC_SOFT = {
    "зверь", "конь", "лось", "гусь", "голубь", "медведь", "лебедь",
    "гость", "червь", "гвоздь", "дождь", "лапоть", "ноготь", "коготь",
    "локоть", "слепень", "шершень", "тюлень", "олень",
    "камень", "корень", "день", "пень", "огонь", "гребень",
    "ячмень", "уровень", "рубль", "циркуль",
}

FEM_SOFT = {
    "ночь", "мышь", "печь", "речь", "вещь", "помощь", "мощь",
    "дверь", "тетрадь", "кровать", "лошадь", "площадь",
    "связь", "грязь", "медь", "жесть", "честь", "грусть",
    "радость", "смелость", "молодость", "старость", "смерть",
    "любовь", "церковь", "морковь", "кровь",
    "жизнь", "болезнь", "песнь", "тень",
    "степь", "цепь", "капель", "акварель",
    "сирень", "модель",
}

STRESSED_A_PL = {
    "дом", "лес", "снег", "луг", "берег", "вечер", "город",
    "голос", "номер", "поезд", "адрес", "парус", "паспорт",
    "профессор", "доктор", "директор", "купол", "колокол",
    "провод", "сторож", "мастер", "якорь", "глаз", "бок",
    "рог", "мех", "сорт", "цвет", "корпус", "остров",
    "флюгер", "кучер", "обшлаг", "рукав", "тормоз",
}

GENITIVE_PL_EXCEPTIONS = {
    "глаз": "глаз", "солдат": "солдат", "гусар": "гусар",
    "драгун": "драгун", "валенок": "валенок", "ботинок": "ботинок",
    "сапог": "сапог", "чулок": "чулок", "носок": "носок",
    "раз": "раз", "аршин": "аршин",
    "грамм": "граммов", "килограмм": "килограммов",
    "апельсин": "апельсинов", "мандарин": "мандаринов",
    "помидор": "помидоров", "томат": "томатов",
    "макароны": "макарон", "деньги": "денег", "дрова": "дров",
    "сани": "саней", "щи": "щей", "чернила": "чернил",
    "консервы": "консервов",
    "сосед": "соседей", "друг": "друзей", "брат": "братьев",
    "сын": "сыновей", "муж": "мужей", "князь": "князей",
    "лист": "листьев", "стул": "стульев", "дерево": "деревьев",
    "крыло": "крыльев", "перо": "перьев", "дно": "доньев",
    "ухо": "ушей", "плечо": "плеч", "яблоко": "яблок",
    "облако": "облаков", "колено": "коленей",
    "чудо": "чудес", "небо": "небес", "платье": "платьев",
    "море": "морей", "поле": "полей", "здание": "зданий",
    "окно": "окон", "стекло": "стёкол", "письмо": "писем",
    "кольцо": "колец", "яйцо": "яиц", "число": "чисел",
    "весло": "вёсел", "ведро": "вёдер", "зеркало": "зеркал",
    "сестра": "сестёр", "звезда": "звёзд",
    "девушка": "девушек", "девочка": "девочек",
    "дедушка": "дедушек", "бабушка": "бабушек",
    "чашка": "чашек", "ложка": "ложек", "бутылка": "бутылок",
    "вилка": "вилок", "тарелка": "тарелок",
    "собака": "собак", "кошка": "кошек", "птица": "птиц",
    "рыба": "рыб", "роща": "рощ", "туча": "туч", "дача": "дач",
    "тысяча": "тысяч",
    "рубль": "рублей", "циркуль": "циркулей",
    "крестьянин": "крестьян", "гражданин": "граждан",
    "англичанин": "англичан", "армянин": "армян",
    "болгарин": "болгар", "татарин": "татар",
    "дворянин": "дворян", "господин": "господ",
    "хозяин": "хозяев", "боярин": "бояр", "барин": "бар",
}


def _get_gender(word):
    w = word.lower().strip()
    if w in NEUTER_MYA:
        return "n"
    if w in ("дядя", "судья", "юноша", "мужчина", "дедушка", "папа", "слуга", "староста", "коллега", "воевода"):
        return "m"
    if w.endswith("а") or w.endswith("я"):
        return "f"
    if w.endswith("о") or w.endswith("е") or w.endswith("ё"):
        return "n"
    if w in MASC_SOFT:
        return "m"
    if w in FEM_SOFT:
        return "f"
    if w.endswith("ь"):
        if w.endswith("ость") or w.endswith("есть") or w.endswith("ознь"):
            return "f"
        if w.endswith("чь") or w.endswith("шь") or w.endswith("щь") or w.endswith("жь"):
            return "f"
        return "m"
    if w[-1].isalpha():
        return "m"
    return "m"


_ANIMALS = {
    "собака", "кошка", "собачка", "кот", "пёс", "корова", "лошадь",
    "конь", "бык", "козёл", "коза", "овца", "баран", "свинья",
    "медведь", "волк", "лиса", "заяц", "тигр", "лев", "слон",
    "птица", "рыба", "змея", "черепаха", "лягушка",
    "котёнок", "котенок", "щенок", "телёнок", "теленок",
    "мышь", "крыса", "белка", "утка", "курица",
}


def _is_animate(word):
    w = word.lower().strip()
    if w in _ANIMALS:
        return True
    anim_suffixes = ("тель", "ик", "ец", "анин", "янин", "арь", "ёр", "ист", "щик", "чик", "льщик", "ник", "ак", "ок", "ун")
    for s in anim_suffixes:
        if w.endswith(s) and len(w) > len(s) + 1:
            return True
    if w in MASC_SOFT and w not in ("дождь", "гвоздь", "лапоть", "ноготь", "локоть", "червь"):
        return True
    return False


_SIB = set("жшщч")
_VEL = set("гкх")
_VOW = set("аеёиоуыэюя")


def _is_likely_plural(word):
    w = word.lower().strip()
    if w in IRREGULAR_DECLENSION:
        return False
    if w.endswith("ы") and len(w) > 2:
        return True
    if w.endswith("и") and len(w) > 2:
        from .pluraliser import IRREGULAR_PLURALS
        if w in IRREGULAR_PLURALS.values():
            return True
        if w.endswith("ии"):
            return False
        return True
    if w.endswith("а") and len(w) > 2:
        from .pluraliser import STRESSED_A_MASC as stressed
        stem = w[:-1]
        if stem in stressed or stem in ("стол", "глаз", "бок", "рог", "мех"):
            return True
        return False
    if w.endswith("я") and len(w) > 2:
        return True
    return False


def decline(word):
    w = word.strip()
    if w.lower() in IRREGULAR_DECLENSION:
        data = IRREGULAR_DECLENSION[w.lower()]
        return {"singular": data["singular"], "plural": data.get("plural", {})}
    gender = _get_gender(w)
    sg = _decline_singular(w, gender)
    pl = _decline_plural(w, gender)
    return {"singular": sg, "plural": pl}


def _decline_singular(word, gender):
    w = word.lower().strip()
    if w in IRREGULAR_DECLENSION:
        return IRREGULAR_DECLENSION[w]["singular"]
    if gender == "m":
        return _sg_masc(w)
    if gender == "n":
        return _sg_neut(w)
    if gender == "f":
        if w.endswith(("а", "я")):
            return _sg_two(w)
        return _sg_three(w)
    return _sg_masc(w)


def _sg_masc(w):
    anim = _is_animate(w)
    if w.endswith("й"):
        s = w[:-1]
        return _case_map(nom=w, gen=s + "я", dat=s + "ю", ins=s + "ем", pre=s + "е", anim=anim)
    if w.endswith("ь"):
        s = w[:-1]
        return _case_map(nom=w, gen=s + "я", dat=s + "ю", ins=s + "ем", pre=s + "е", anim=anim)
    s = w
    ins = s + "ом"
    if s[-1] in _SIB or s.endswith("ц"):
        ins = s + "ем"
    return _case_map(nom=w, gen=s + "а", dat=s + "у", ins=ins, pre=s + "е", anim=anim)


def _sg_neut(w):
    if w in NEUTER_MYA:
        s = w[:-1]
        ext = s + "ен"
        return _case_map(nom=w, gen=ext + "и", dat=ext + "и", ins=ext + "ем", pre=ext + "и", anim=False)
    if w.endswith("ие"):
        s = w[:-2]
        return _case_map(nom=w, gen=s + "ия", dat=s + "ию", ins=s + "ием", pre=s + "ии", anim=False)
    if w.endswith("ье"):
        s = w[:-2]
        return _case_map(nom=w, gen=s + "ья", dat=s + "ью", ins=s + "ьем", pre=s + "ье", anim=False)
    if w.endswith("ё"):
        s = w[:-1]
        return _case_map(nom=w, gen=s + "а", dat=s + "у", ins=s + "ом", pre=s + "е", anim=False)
    if w.endswith("е"):
        s = w[:-1]
        return _case_map(nom=w, gen=s + "я", dat=s + "ю", ins=s + "ем", pre=s + "е", anim=False)
    s = w[:-1]
    ins = s + "ом"
    if s and s[-1] in _SIB:
        ins = s + "ем"
    return _case_map(nom=w, gen=s + "а", dat=s + "у", ins=ins, pre=s + "е", anim=False)


def _sg_two(w):
    if w.endswith("ия"):
        s = w[:-1]
        return _case_map(nom=w, gen=s + "и", dat=s + "и", ins=s + "ей", pre=s + "и", acc=s + "ю")
    if w.endswith("ья"):
        s = w[:-2]
        return _case_map(nom=w, gen=s + "ьи", dat=s + "ье", ins=s + "ьёй", pre=s + "ье", acc=s + "ью")
    if w.endswith("я"):
        s = w[:-1]
        ins = s + "ей"
        if s and s[-1] in _SIB:
            ins = s + "ей"
        return _case_map(nom=w, gen=s + "и", dat=s + "е", ins=ins, pre=s + "е", acc=s + "ю")
    s = w[:-1]
    gen = s + "ы"
    if s and (s[-1] in _VEL or s[-1] in _SIB):
        gen = s + "и"
    ins = s + "ой"
    if s and s[-1] in _SIB:
        ins = s + "ей"
    return _case_map(nom=w, gen=gen, dat=s + "е", ins=ins, pre=s + "е", acc=s + "у")


def _sg_three(w):
    s = w[:-1]
    anim = w in ("мышь", "лошадь")
    return _case_map(nom=w, gen=s + "и", dat=s + "и", ins=s + "ью", pre=s + "и", anim=anim)


def _case_map(nom, gen, dat, ins, pre, anim=False, acc=None):
    a = acc if acc is not None else (gen if anim else nom)
    return {"nominative": nom, "genitive": gen, "dative": dat, "accusative": a, "instrumental": ins, "prepositional": pre}


def _decline_plural(word, gender):
    from .pluraliser import pluralise

    w = word.lower().strip()
    if w in IRREGULAR_DECLENSION and "plural" in IRREGULAR_DECLENSION[w]:
        return IRREGULAR_DECLENSION[w]["plural"]

    nom_pl = pluralise(w)
    if nom_pl is None:
        return {}

    anim = _is_animate(w)
    gen_pl = _gen_pl(w, gender, nom_pl)
    stem = _pl_stem(nom_pl)

    suffix = _pl_suffixes(w, nom_pl)
    dat_pl = stem + suffix[0]
    ins_pl = stem + suffix[1]
    pre_pl = stem + suffix[2]
    acc_pl = gen_pl if anim else nom_pl

    return {"nominative": nom_pl, "genitive": gen_pl, "dative": dat_pl,
            "accusative": acc_pl, "instrumental": ins_pl, "prepositional": pre_pl}


def _pl_stem(nom_pl):
    if nom_pl.endswith(("ы", "и", "а", "я", "е")):
        return nom_pl[:-1]
    return nom_pl


def _pl_suffixes(word, nom_pl):
    soft_markers = ("й", "ь", "я", "ю", "е", "ё")
    w = word.lower().strip()

    if nom_pl.endswith("а"):
        s = nom_pl[:-1]
        if s and s[-1] in _SIB:
            return "ам", "ами", "ах"
        return "ам", "ами", "ах"

    if nom_pl.endswith("я"):
        return "ям", "ями", "ях"

    if nom_pl.endswith("ы"):
        return "ам", "ами", "ах"

    if nom_pl.endswith("и"):
        s = nom_pl[:-1]
        if s and s[-1] in _SIB:
            return "ам", "ами", "ах"
        if any(w.endswith(m) for m in soft_markers):
            pass
        if w.endswith(("ь", "й")) or (w.endswith("я") and not w.endswith(("а",))):
            return "ям", "ями", "ях"
        if s and s[-1] in _VEL:
            return "ам", "ами", "ах"
        return "ам", "ами", "ах"

    if nom_pl.endswith("е"):
        if w.endswith(("о",)):
            return "ам", "ами", "ах"
        return "ям", "ями", "ях"

    return "ам", "ами", "ах"


def _gen_pl(word, gender, nom_pl):
    w = word.lower().strip()
    if w in GENITIVE_PL_EXCEPTIONS:
        return GENITIVE_PL_EXCEPTIONS[w]

    if gender == "m":
        if w.endswith("й"):
            return w[:-1] + "ев"
        if w.endswith("ь"):
            return w[:-1] + "ей"
        if w.endswith("ин") and len(w) > 4:
            if w.endswith("анин") or w.endswith("янин"):
                return w[:-2]
            return w + "ов"
        if w[-1] in _SIB:
            return w + "ей"
        return w + "ов"

    if gender == "f":
        if w.endswith("а"):
            return _gen_pl_fem_a(w[:-1])
        if w.endswith("я"):
            return _gen_pl_fem_ya(w)
        if w.endswith("ь"):
            return w[:-1] + "ей"
        return w + "ей"

    if gender == "n":
        if w.endswith("о"):
            stem = w[:-1]
            if stem and stem[-1] in _SIB:
                return stem + "ей"
            return stem
        if w.endswith("ие"):
            return w[:-2] + "ий"
        if w.endswith("ье"):
            return w[:-2] + "ий"
        if w.endswith("е"):
            return w[:-1] + "ей"
        if w.endswith("мя"):
            return w[:-2] + "мён" if w != "семя" else w[:-2] + "мян"
        return w + "ов"

    return nom_pl + "ов" if nom_pl else w + "ов"


def _gen_pl_fem_a(stem):
    if not stem:
        return ""
    if stem[-1] in _SIB:
        if len(stem) >= 2 and stem[-1] in "чщ" and stem[-2] not in _VOW:
            return stem + "ей"
        return stem
    if stem.endswith("ц"):
        return stem
    if len(stem) >= 2 and all(c not in _VOW for c in stem[-2:]):
        return stem + "ей"
    return stem


def _gen_pl_fem_ya(w):
    if w.endswith("ия"):
        return w[:-1] + "й"
    stem = w[:-1]
    if not stem:
        return "ь"
    if stem[-1] in _SIB:
        return stem + "ей"
    if stem.endswith("ц"):
        return stem + "ь"
    return stem + "ь"


def decline_with_info(word):
    w = word.strip()
    if _is_likely_plural(w):
        return {"error": True, "message": f"'{w}' appears to be a plural noun. Enter the singular form."}

    gender = _get_gender(w)
    gender_label = {"m": "masculine", "f": "feminine", "n": "neuter"}.get(gender, "unknown")
    is_irregular = w.lower() in IRREGULAR_DECLENSION or w.lower() in GENITIVE_PL_EXCEPTIONS
    result = decline(w)
    if not result.get("plural"):
        return {"error": True, "message": f"Cannot decline '{w}': word is a verb"}
    info = {"word": w, "gender": gender_label, "singular": result["singular"], "plural": result["plural"]}
    if is_irregular:
        info["exception"] = "irregular"
    return info
