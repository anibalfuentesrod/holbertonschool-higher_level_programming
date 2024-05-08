#!/usr/bin/python3
for alph in range(97, 123):
    if alph == ord('q') or alph == ord('e'):
        continue
    else:
        print("{}".format(chr(alph)), end='')
