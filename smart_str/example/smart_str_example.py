from smart_str.smart_str import SmartStr

byte_str_utf_8_space = '\x20'

byte_str_utf_8_latin_capital_letter_n = '\x4E'
byte_str_utf_8_hebrew_letter_tet = '\xD7\x98'
byte_str_utf_8_black_scissors = '\xE2\x9C\x82'
byte_str_utf_8_grinning_face = '\xF0\x9F\x98\x80'

byte_str_utf_8_national_flag_symbol_l = '\xF0\x9F\x87\xB1'
byte_str_utf_8_national_flag_symbol_v = '\xF0\x9F\x87\xBB'
byte_str_utf_8_latvian_flag = byte_str_utf_8_national_flag_symbol_l + byte_str_utf_8_national_flag_symbol_v

byte_str_utf_8_woman = '\xF0\x9F\x91\xA9'
byte_str_utf_8_fitzpatrick_type_5 = '\xF0\x9F\x8F\xBE'
byte_str_utf_8_dark_woman = byte_str_utf_8_woman + byte_str_utf_8_fitzpatrick_type_5

utf_8_str = (
    byte_str_utf_8_latin_capital_letter_n +  # 1 character, 1 code point,  1 byte
    byte_str_utf_8_space +                   # 1 character, 1 code point,  1 byte
    byte_str_utf_8_hebrew_letter_tet +       # 1 character, 1 code point,  2 bytes
    byte_str_utf_8_space +                   # 1 character, 1 code point,  1 byte
    byte_str_utf_8_black_scissors +          # 1 character, 1 code point,  3 bytes
    byte_str_utf_8_space +                   # 1 character, 1 code point,  1 byte
    byte_str_utf_8_grinning_face +           # 1 character, 1 code point,  4 bytes
    byte_str_utf_8_space +                   # 1 character, 1 code point,  1 byte
    byte_str_utf_8_national_flag_symbol_l +  # 1 character, 1 code point,  4 bytes
    byte_str_utf_8_space +                   # 1 character, 1 code point,  1 byte
    byte_str_utf_8_national_flag_symbol_v +  # 1 character, 1 code point,  4 bytes
    byte_str_utf_8_space +                   # 1 character, 1 code point,  1 byte
    byte_str_utf_8_latvian_flag +            # 1 character, 2 code points, 8 bytes
    byte_str_utf_8_space +                   # 1 character, 1 code point,  1 byte
    byte_str_utf_8_woman +                   # 1 character, 1 code point,  4 bytes
    byte_str_utf_8_space +                   # 1 character, 1 code point,  1 byte
    byte_str_utf_8_fitzpatrick_type_5 +      # 1 character, 1 code point,  4 bytes
    byte_str_utf_8_space +                   # 1 character, 1 code point,  1 byte
    byte_str_utf_8_dark_woman                # 1 character, 2 code points, 8 bytes
)


unicode_str_utf_16_space = u'\u0020'

unicode_str_utf_16_latin_capital_letter_n = u'\u004E'
unicode_str_utf_16_hebrew_letter_tet = u'\u05D8'
unicode_str_utf_16_black_scissors = u'\u2702'
unicode_str_utf_16_grinning_face = u'\uD83D\uDE00'

unicode_str_utf_16_national_flag_symbol_l = u'\uD83C\uDDF1'
unicode_str_utf_16_national_flag_symbol_v = u'\uD83C\uDDFB'
unicode_str_utf_16_latvian_flag = unicode_str_utf_16_national_flag_symbol_l + unicode_str_utf_16_national_flag_symbol_v

unicode_str_utf_16_woman = u'\uD83D\uDC69'
unicode_str_utf_16_fitzpatrick_type_5 = u'\uD83C\uDFFE'
unicode_str_utf_16_dark_woman = unicode_str_utf_16_woman + unicode_str_utf_16_fitzpatrick_type_5

utf_16_str = (
    unicode_str_utf_16_latin_capital_letter_n +  # 1 character, 1 code point,  1 word
    unicode_str_utf_16_space +                   # 1 character, 1 code point,  1 word
    unicode_str_utf_16_hebrew_letter_tet +       # 1 character, 1 code point,  1 word
    unicode_str_utf_16_space +                   # 1 character, 1 code point,  1 word
    unicode_str_utf_16_black_scissors +          # 1 character, 1 code point,  1 word
    unicode_str_utf_16_space +                   # 1 character, 1 code point,  1 word
    unicode_str_utf_16_grinning_face +           # 1 character, 1 code point,  2 words
    unicode_str_utf_16_space +                   # 1 character, 1 code point,  1 word
    unicode_str_utf_16_national_flag_symbol_l +  # 1 character, 1 code point,  2 words
    unicode_str_utf_16_space +                   # 1 character, 1 code point,  1 word
    unicode_str_utf_16_national_flag_symbol_v +  # 1 character, 1 code point,  2 words
    unicode_str_utf_16_space +                   # 1 character, 1 code point,  1 word
    unicode_str_utf_16_latvian_flag +            # 1 character, 2 code points, 4 words
    unicode_str_utf_16_space +                   # 1 character, 1 code point,  1 word
    unicode_str_utf_16_woman +                   # 1 character, 1 code point,  2 words
    unicode_str_utf_16_space +                   # 1 character, 1 code point,  1 word
    unicode_str_utf_16_fitzpatrick_type_5 +      # 1 character, 1 code point,  2 words
    unicode_str_utf_16_space +                   # 1 character, 1 code point,  1 word
    unicode_str_utf_16_dark_woman                # 1 character, 2 code points, 4 words
)


def main():
    print
    print '****************************************************************************************'
    print
    print 'Here is a UTF-8 string, represented in python \'str\' object - \'utf_8_str\':'
    print utf_8_str
    print 'It consists of 10 characters separated by spaces - all together 19 characters.'
    print
    print 'If we will check the length of this string by calling \'len(utf_8_str)\' we will get {}. Why ?'.format(len(utf_8_str))
    print 'This is caused by the fact that many Unicode characters represented in UTF-8 occupy more than 1 byte, and calling \'len(utf_8_str)\'\n' \
          'counts the number of bytes in the string, and not the number of the actual characters.'
    print
    print 'The same happens for UTF-16 strings, represented in python \'unicode\' objects.'
    print 'Here is the same UTF-16 string, represented in python \'unicode\' object - \'utf_16_str\':'
    print utf_16_str.encode('utf-8')
    print
    print 'The length of the string is not accordant with the number of the actual characters in the string in this case as well.'
    print 'The string length acquired by calling \'len(utf_16_str)\' is {}, though the number of characters is still 19.'.format(len(utf_16_str))
    print 'Again, calling \'len(utf_16_str)\' will return the number of words in the string, and not the number of the actual characters (word - 2 bytes).\n' \
          'Some characters occupy more than 1 word.'
    print
    print 'To resolve this we are introducing the \'Smart Str\'.'
    print 'The \'Smart Str\' object can be initialized with UTF-8 or UTF-16 string, and provide correct parsing of the string to characters and Unicode code points.\n' \
          'It also provides the ability to convert UTF-8 string to UTF-16 one, and vice versa.'
    print
    print 'Here is \'Smart Str\' object initialized with the same UTF-8 string, and few properties of the object:'
    smart_str = SmartStr(utf_8_str)
    print 'Smart Str: {}'.format(smart_str)
    print 'Str length: {}'.format(len(smart_str))
    print 'Characters count: {}'.format(smart_str.characters_count)
    print 'Code points count: {}'.format(smart_str.code_points_count)
    print 'Accordant UTF-8 str: {}'.format(str(smart_str))
    print 'Accordant UTF-8 str length: {}'.format(smart_str.raw_utf_8_length)
    print u'Accordant UTF-16 str: {}'.format(unicode(smart_str)).encode('utf-8')
    print 'Accordant UTF-16 str length: {}'.format(smart_str.raw_utf_16_length)
    print
    print 'Here are the characters of the Smart Str:'
    print
    for i in range(len(smart_str)):
        smart_char = smart_str[i]
        print 'Char {}: \'{}\''.format(i, smart_char)
        print 'Code points Count: {}'.format(smart_char.code_points_count)
        if smart_char.code_points_count == 1:
            print 'Code Point: {}'.format(smart_char[0].unicode_val_hex_str)
        else:
            print 'Code Points: {}, {}'.format(smart_char[0].unicode_val_hex_str, smart_char[1].unicode_val_hex_str)
        print

    print '****************************************************************************************'
    print


main()
