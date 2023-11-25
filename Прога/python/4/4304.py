def answer(f):
    def decorated(*args, **kwargs):
        result = f(*args, **kwargs)
        return f"Результат функции: {result}"
    return decorated

@answer
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
