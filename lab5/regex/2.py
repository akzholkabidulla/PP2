import re

txt = input()
regex = re.search('^a(b){2,3}&',txt)
if regex:
    print("True")
else:
    print("False")

# символ 'a' за которым следует два или три 'b'