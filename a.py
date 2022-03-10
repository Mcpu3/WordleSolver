words = []
with open('words.txt') as f:
    words_raw = f.readlines()
for word_raw in words_raw:
    words.append(word_raw[:-1])
with open('words.js', 'w') as f:
    for word in words:
        f.write('    ' + '\'' + word + '\'' + ',' + '\n')