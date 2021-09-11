#!/usr/bin/python
# -*- encoding: utf-8 -*-
# PYTHON 2 WARNING

import sys

ORIGINAL_ENCODING = "big5"

# From https://docs.python.org/2.4/lib/standard-encodings.html
# This is just a fancy way to put things. Usually trying for cp1251 works.
encodings = """ascii big5 big5hkscs cp037 cp424 cp437 cp500 cp737 cp775 cp850 cp852 cp855 cp856 cp857 cp860 cp861 cp862 cp863 cp864 cp865 cp866 cp869 cp874 cp875 cp932 cp949 cp950 cp1006 cp1026 cp1140 cp1250 cp1251 cp1252 cp1253 cp1254 cp1255 cp1256 cp1257 cp1258 euc_jp euc_jis_2004 euc_jisx0213 euc_kr gb2312 gbk gb18030 hz iso2022_jp iso2022_jp_1 iso2022_jp_2 iso2022_jp_2004 iso2022_jp_3 iso2022_jp_ext iso2022_kr latin_1 iso8859_2 iso8859_3 iso8859_4 iso8859_5 iso8859_6 iso8859_7 iso8859_8 iso8859_9 iso8859_10 iso8859_13 iso8859_14 iso8859_15 johab koi8_r koi8_u mac_cyrillic mac_greek mac_iceland mac_latin2 mac_roman mac_turkish ptcp154 shift_jis shift_jis_2004 shift_jisx0213 utf_16 utf_16_be utf_16_le utf_7 utf_8""".strip().split(" ")

ss = sys.stdin.read().decode("utf-8")

print(" ".join(str(ord(c)) for c in ss))
for enc in encodings:
    sys.stdout.write("Trying %s.. " % enc)
    try:
        force_encoded = ss.encode(enc)
        sys.stdout.write("Success!\n")
        sys.stdout.write(force_encoded.decode(ORIGINAL_ENCODING).encode("utf-8"))
        sys.stdout.write("\n")
    except Exception:
        pass

