import importlib

langs = {
    "uz": "🇺🇿 O'zbekcha",
    "ru": "🇷🇺 Русский",
    "en": "🇬🇧 English"
}

class Locales:
    @staticmethod
    def getLangs():
        return langs

    @staticmethod
    def getMessage(lang: str, key: str) -> str:
        try:
            messages = importlib.import_module(f'locales.{lang}')
            return getattr(messages, key)
        except (ModuleNotFoundError, AttributeError):
            return key