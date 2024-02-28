import re

txt = input()
regex = re.search('^a(b*)$', txt)
if regex:
    print("True")
else:
    print("False")
# символ 'a' за которым следует 0 или больше 'b'