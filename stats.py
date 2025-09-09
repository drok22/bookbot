def get_num_words(text: str):
    num_words = len(text.split())
    return num_words


def get_chars_dict(text: str) -> dict:
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_counts_list(chars: dict) -> dict:
    counts = []
    for key in chars:
        counts.append({"char": key, "num": chars[key]})
    counts.sort(reverse=True, key=sort_on)
    return counts


def sort_on(items: dict) -> int:
    return items["num"]
