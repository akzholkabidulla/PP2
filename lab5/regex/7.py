import re

message = input()
print(''.join(x.capitalize() or '_' for x in message.split('_')))

# этот код изменяет строку из snake_case to CamelCase
# CamelCase  - стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово внутри фразы пишется с прописной буквы.
# Snake_case - стиль написания, при котором слова разделяются символом подчеркивания _, например: hello_world