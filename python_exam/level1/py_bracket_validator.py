def bracket_validator(s: str) -> bool:
    lista = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            lista.append(ch)
        elif ch in ')]}':
            if not lista or lista.pop() != pairs[ch]:
                return False
    return len(lista) == 0
