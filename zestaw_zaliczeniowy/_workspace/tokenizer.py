
import re

class Tokenizer:
    """Konfigurowany tokenizator: HTML strip + case + min length filter."""
    def __init__(self, lower: bool = True, strip_html: bool = True, min_length: int = 1):
        """Zapisuje konfiguracje tokenizacji i waliduje minimalna dlugosc tokenu."""
        if min_length < 1:
            raise ValueError("min_length musi byc >= 1")
        self.lower = lower
        self.strip_html = strip_html
        self.min_length = min_length

    def tokenize(self, text: str) -> list[str]:
        """Tokenizuje tekst z opcjonalnym usuwaniem HTML, lowercase i filtrem dlugosci."""
        if not isinstance(text, str):
            raise TypeError("text musi byc string")
        processed_text = text
        if self.strip_html:
            processed_text = re.sub(r"<[^>]+>", " ", processed_text)
        if self.lower:
            processed_text = processed_text.lower()
        tokens = re.findall(r"\w+", processed_text, flags=re.UNICODE)
        return [token for token in tokens if len(token) >= self.min_length]

    def vocab(self, texts: list[str]) -> set[str]:
        """Zwraca zbior unikalnych tokenow z wszystkich przekazanych tekstow."""
        vocabulary: set[str] = set()
        for text in texts:
            vocabulary.update(self.tokenize(text))
        return vocabulary
