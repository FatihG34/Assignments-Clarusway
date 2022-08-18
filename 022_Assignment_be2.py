def shortcut(word):
    search = word.replace('a', '').replace('e', '').replace(
        'i', '').replace('o', '').replace('u', '')
    return search


asd = 'a ne yaptın gardaş be bunlar olmaz ki'

print(shortcut(asd))
