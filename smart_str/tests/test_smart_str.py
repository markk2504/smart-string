from smart_str import SmartStr
from smart_str import StrInitInputType


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


def perform_test_for_utf_8_input_sequence(utf_8_input_sequence,
                                          expected_characters_count,
                                          expected_code_points_count,
                                          expected_utf_16_sequence):
    smart_str = SmartStr(utf_8_input_sequence)

    assert smart_str.init_raw_type == StrInitInputType.UTF_8
    assert str(smart_str) == utf_8_input_sequence
    assert smart_str.raw_utf_8_length == len(utf_8_input_sequence)

    assert smart_str.characters_count == expected_characters_count
    assert smart_str.code_points_count == expected_code_points_count

    assert unicode(smart_str) == expected_utf_16_sequence
    assert smart_str.raw_utf_16_length == len(expected_utf_16_sequence)

    assert str(smart_str) in repr(smart_str)

def perform_test_for_utf_16_input_sequence(utf_16_input_sequence,
                                           expected_characters_count,
                                           expected_code_points_count,
                                           expected_utf_8_sequence):
    smart_str = SmartStr(utf_16_input_sequence)

    assert smart_str.init_raw_type == StrInitInputType.UTF_16
    assert unicode(smart_str) == utf_16_input_sequence
    assert smart_str.raw_utf_16_length == len(utf_16_input_sequence)

    assert smart_str.characters_count == expected_characters_count
    assert smart_str.code_points_count == expected_code_points_count

    assert str(smart_str) == expected_utf_8_sequence
    assert smart_str.raw_utf_8_length == len(expected_utf_8_sequence)

    assert str(smart_str) in repr(smart_str)


# Tests for UTF-8 input

def test_smart_string_simple_utf_8_input():
    perform_test_for_utf_8_input_sequence(
        utf_8_input_sequence='This is a simple ascii string.',
        expected_characters_count=30,
        expected_code_points_count=30,
        expected_utf_16_sequence=u'This is a simple ascii string.')

def test_smart_string_composite_utf_8_input():
    perform_test_for_utf_8_input_sequence(
        utf_8_input_sequence=utf_8_str,
        expected_characters_count=19,
        expected_code_points_count=21,
        expected_utf_16_sequence=utf_16_str)


# Tests for UTF-16 input

def test_smart_string_composite_utf_16_input():
    perform_test_for_utf_16_input_sequence(
        utf_16_input_sequence=utf_16_str,
        expected_characters_count=19,
        expected_code_points_count=21,
        expected_utf_8_sequence=utf_8_str)
