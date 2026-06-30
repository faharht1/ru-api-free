from .conjugator import conjugate, search_verbs, list_verbs, get_exceptions, get_verb_exceptions, EXCEPTION_TYPES
from .dictionary import translate, translate_en_to_ru
from .pluraliser import pluralise, pluralise_with_info
from .declension import decline, decline_with_info

__version__ = "1.4.0"
__all__ = [
    "conjugate", "search_verbs", "list_verbs",
    "get_exceptions", "get_verb_exceptions", "EXCEPTION_TYPES",
    "translate", "translate_en_to_ru",
    "pluralise", "pluralise_with_info",
    "decline", "decline_with_info",
]
