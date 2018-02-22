tranlite = {
    'а': 'a', 'б':'b', 'в':'v', 'г':'g', 'д':'d', 'е':'e', 'ё':'yo',
    'ж':'zh', 'з':'z', 'и':'i', 'й':'y', 'к':'k', 'л':'l', 'м': 'm',
    'н':'n', 'о': 'o', 'п': 'p', 'р':'r', 'с':'s', 'т':'t', 'у':'u',
    'ф':'f', 'х':'kh', 'ц':'ts', 'ч':'ch', 'ш':'sh', 'щ':'sch', 'ы':'y',
    'э':'e', 'ю':'y', 'я':'ya',
    'А':'A', 'Б':'B', 'В':'V', 'Г':'G', 'Д':'D', 'Е':'E', 'Ё':'YO', 'Ж':'ZH',
    'З':'Z', 'И':'I', 'Й':'Y', 'К':'K', 'Л':'L', 'М':'M', 'Н':'N', 'О':'O', 'П':'P',
    'Р':'R', 'С':'S', 'Т':'T', 'У':'U', 'Ф':'F', 'Х':'KH', 'Ц':'TS', 'Ч':'CH', 'Ш':'SH',
    'Щ':'SCH', 'Ы':'Y', 'Э':'E', 'Ю':'YU', 'Я':'YA', 'ө':'o', 'ң':'n', 'ү':'u', 'Ү':'U',
    'Ө':'O', 'Ң':'N', 'ğ':'g', 'ş':'s', 'ü':'', 'ç':'c', 'ö':'o', 'Ğ':'G', 'Ş':'S',
    'Ü':'', 'Ç':'C', 'Ö':'O',
    ' ': '-', '?':'', '!':'', ',':'', '…':''
}
orig = 'Аэропортко акыркы автобус канчада жөнөйт?'

def translit(word, translit_table):
    converted_word = ''
    for char in word:
        transchar = ''
        if char in translit_table:
            transchar = translit_table[char]
        else:
            transchar = char
        converted_word += transchar
    return converted_word

print(translit(orig,translite))
