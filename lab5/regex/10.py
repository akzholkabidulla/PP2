import re

message = input()
print('_'.join(
    re.sub('([A-Z][a-z]+)', r' \1',
    re.sub('([A-Z]+)', r' \1',
    message.replace('-', ' '))).split()).lower())

#.lower(): Этот код приводит всю строку к нижнему регистру.

# этот код изменяет строку из  CamelCase to snake_case 