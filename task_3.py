import requests


def get_symbols() -> dict:
    r = requests.get('https://www.python.org')
    if not r.ok:
        raise Exception('Bad response. Try again later')
    text = r.text
    symbols = dict()
    for c in text:
        if c in symbols:
            symbols[c] += 1
        else:
            symbols[c] = 1
    return symbols


def correct_symbol(c: str) -> str:
    if c == '\n':
        return r'\n'
    elif c == '\r':
        return r'\r'
    elif c == '|':
        return r'&#124;'
    else:
        return c


def fill_readme():
    output = '# Symbols stat table\n\n'
    output += '| Symbol | Amount |\n'
    output += '|--------|--------|\n'
    symbols = sorted(list(get_symbols().items()), key=lambda x: x[1], reverse=True)
    for symbol, amount in symbols:
        output += f"|'{correct_symbol(symbol)}'|{amount}|\n"
    with open('readme.md', 'w') as f:
        f.write(output)


if __name__ == '__main__':
    fill_readme()
    print('readme.md is ready')
