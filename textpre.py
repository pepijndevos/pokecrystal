#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

chars = {
"ガ": 0x05,
"ギ": 0x06,
"グ": 0x07,
"ゲ": 0x08,
"ゴ": 0x09,
"ザ": 0x0A,
"ジ": 0x0B,
"ズ": 0x0C,
"ゼ": 0x0D,
"ゾ": 0x0E,
"ダ": 0x0F,
"ヂ": 0x10,
"ヅ": 0x11,
"デ": 0x12,
"ド": 0x13,
"バ": 0x19,
"ビ": 0x1A,
"ブ": 0x1B,
"ボ": 0x1C,
"が": 0x26,
"ぎ": 0x27,
"ぐ": 0x28,
"げ": 0x29,
"ご": 0x2A,
"ざ": 0x2B,
"じ": 0x2C,
"ず": 0x2D,
"ぜ": 0x2E,
"ぞ": 0x2F,
"だ": 0x30,
"ぢ": 0x31,
"づ": 0x32,
"で": 0x33,
"ど": 0x34,
"ば": 0x3A,
"び": 0x3B,
"ぶ": 0x3C,
"べ": 0x3D,
"ぼ": 0x3E,
"パ": 0x40,
"ピ": 0x41,
"プ": 0x42,
"ポ": 0x43,
"ぱ": 0x44,
"ぴ": 0x45,
"ぷ": 0x46,
"ぺ": 0x47,
"ぽ": 0x48,
"ア": 0x80,
"イ": 0x81,
"ウ": 0x82,
"エ": 0x83,
"ォ": 0x84,
"カ": 0x85,
"キ": 0x86,
"ク": 0x87,
"ケ": 0x88,
"コ": 0x89,
"サ": 0x8A,
"シ": 0x8B,
"ス": 0x8C,
"セ": 0x8D,
"ソ": 0x8E,
"タ": 0x8F,
"チ": 0x90,
"ツ": 0x91,
"テ": 0x92,
"ト": 0x93,
"ナ": 0x94,
"ニ": 0x95,
"ヌ": 0x96,
"ネ": 0x97,
"ノ": 0x98,
"ハ": 0x99,
"ヒ": 0x9A,
"フ": 0x9B,
"ホ": 0x9C,
"マ": 0x9D,
"ミ": 0x9E,
"ム": 0x9F,
"メ": 0xA0,
"モ": 0xA1,
"ヤ": 0xA2,
"ユ": 0xA3,
"ヨ": 0xA4,
"ラ": 0xA5,
"ル": 0xA6,
"レ": 0xA7,
"ロ": 0xA8,
"ワ": 0xA9,
"ヲ": 0xAA,
"ン": 0xAB,
"ッ": 0xAC,
"ャ": 0xAD,
"ュ": 0xAE,
"ョ": 0xAF,
"ィ": 0xB0,
"あ": 0xB1,
"い": 0xB2,
"う": 0xB3,
"え": 0xB4,
"お": 0xB5,
"か": 0xB6,
"き": 0xB7,
"く": 0xB8,
"け": 0xB9,
"こ": 0xBA,
"さ": 0xBB,
"し": 0xBC,
"す": 0xBD,
"せ": 0xBE,
"そ": 0xBF,
"た": 0xC0,
"ち": 0xC1,
"つ": 0xC2,
"て": 0xC3,
"と": 0xC4,
"な": 0xC5,
"に": 0xC6,
"ぬ": 0xC7,
"ね": 0xC8,
"の": 0xC9,
"は": 0xCA,
"ひ": 0xCB,
"ふ": 0xCC,
"へ": 0xCD,
"ほ": 0xCE,
"ま": 0xCF,
"み": 0xD0,
"む": 0xD1,
"め": 0xD2,
"も": 0xD3,
"や": 0xD4,
"ゆ": 0xD5,
"よ": 0xD6,
"ら": 0xD7,
"り": 0xD8,
"る": 0xD9,
"れ": 0xDA,
"ろ": 0xDB,
"わ": 0xDC,
"を": 0xDD,
"ん": 0xDE,
"っ": 0xDF,
"ゃ": 0xE0,
"ゅ": 0xE1,
"ょ": 0xE2,
"ー": 0xE3,


"@": 0x50,
"#": 0x54,
"…": 0x75,

"┌": 0x79,
"─": 0x7A,
"┐": 0x7B,
"│": 0x7C,
"└": 0x7D,
"┘": 0x7E,

"№": 0x74,

" ": 0x7F,
"A": 0x80,
"B": 0x81,
"C": 0x82,
"D": 0x83,
"E": 0x84,
"F": 0x85,
"G": 0x86,
"H": 0x87,
"I": 0x88,
"J": 0x89,
"K": 0x8A,
"L": 0x8B,
"M": 0x8C,
"N": 0x8D,
"O": 0x8E,
"P": 0x8F,
"Q": 0x90,
"R": 0x91,
"S": 0x92,
"T": 0x93,
"U": 0x94,
"V": 0x95,
"W": 0x96,
"X": 0x97,
"Y": 0x98,
"Z": 0x99,
"(": 0x9A,
")": 0x9B,
":": 0x9C,
";": 0x9D,
"[": 0x9E,
"]": 0x9F,
"a": 0xA0,
"b": 0xA1,
"c": 0xA2,
"d": 0xA3,
"e": 0xA4,
"f": 0xA5,
"g": 0xA6,
"h": 0xA7,
"i": 0xA8,
"j": 0xA9,
"k": 0xAA,
"l": 0xAB,
"m": 0xAC,
"n": 0xAD,
"o": 0xAE,
"p": 0xAF,
"q": 0xB0,
"r": 0xB1,
"s": 0xB2,
"t": 0xB3,
"u": 0xB4,
"v": 0xB5,
"w": 0xB6,
"x": 0xB7,
"y": 0xB8,
"z": 0xB9,
"Ä": 0xC0,
"Ö": 0xC1,
"Ü": 0xC2,
"ä": 0xC3,
"ö": 0xC4,
"ü": 0xC5,
"'d": 0xD0,
"'l": 0xD1,
"'m": 0xD2,
"'r": 0xD3,
"'s": 0xD4,
"'t": 0xD5,
"'v": 0xD6,
"'": 0xE0,
"-": 0xE3,
"?": 0xE6,
"!": 0xE7,
".": 0xE8,
"&": 0xE9,
"é": 0xEA,
"→": 0xEB,
"♂": 0xEF,
"¥": 0xF0,
"×": 0xF1,
"/": 0xF3,
",": 0xF4,
"♀": 0xF5,
"0": 0xF6,
"1": 0xF7,
"2": 0xF8,
"3": 0xF9,
"4": 0xFA,
"5": 0xFB,
"6": 0xFC,
"7": 0xFD,
"8": 0xFE,
"9": 0xFF
}

for l in sys.stdin:
    # strip comments
    asm = ""
    comment    = None
    in_quotes  = False
    in_comment = False
    for letter in l:
        if in_comment:
            comment += letter
        elif in_quotes and letter != "\"":
            asm += letter
        elif in_quotes and letter == "\"":
            in_quotes = False
            asm += letter
        elif not in_quotes and letter == "\"":
            in_quotes = True
            asm += letter
        elif not in_quotes and letter != "\"":
            if letter == ";":
                in_comment = True
                comment = ";"
            else:
                asm += letter

    # skip asm with no quotes
    if "\"" not in asm:
        sys.stdout.write(l)
        continue

    # split by quotes
    asms = asm.split("\"")

    # skip asm that actually does use ASCII in quotes
    lowasm = asms[0].lower()
    if "section" in lowasm \
    or "include" in lowasm \
    or "incbin" in lowasm:
        sys.stdout.write(l)
        continue

    even = False
    i = 0
    for token in asms:
        i = i + 1
        if even:
            # token is a string to convert to byte values

            while len(token):
                # read a single UTF-8 codepoint
                char = token[0]
                if ord(char) >= 0xFC:
                    char = char + token[1:6]
                    token = token[6:]
                elif ord(char) >= 0xF8:
                    char = char + token[1:5]
                    token = token[5:]
                elif ord(char) >= 0xF0:
                    char = char + token[1:4]
                    token = token[4:]
                elif ord(char) >= 0xE0:
                    char = char + token[1:3]
                    token = token[3:]
                elif ord(char) >= 0xC0:
                    char = char + token[1:2]
                    token = token[2:]
                else:
                    token = token[1:]

                    # certain apostrophe-letter pairs are only a single byte
                    if char == "'" and \
                        (token[0] == "d" or \
                         token[0] == "l" or \
                         token[0] == "m" or \
                         token[0] == "r" or \
                         token[0] == "s" or \
                         token[0] == "t" or \
                         token[0] == "v"):
                        char = char + token[0]
                        token = token[1:]

                sys.stdout.write("${0:02X}".format(chars[char]))

                if len(token):
                    sys.stdout.write(", ")

        else:
            sys.stdout.write(token)
        even = not even

    if comment != None:
        sys.stdout.write(comment)
