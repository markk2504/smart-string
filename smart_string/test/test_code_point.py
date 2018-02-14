from smart_string.code_point import CodePoint, CodePointType, CodePointPlaneType
from smart_string.smart_string_constants import StrRawType


def perform_test_for_utf_8_input_sequence(utf_8_input_sequence,
                                          expected_unicode_value,
                                          expected_code_point_type,
                                          expected_code_point_plane_type,
                                          expected_utf_16_sequence):

    code_point = CodePoint(utf_8_input_sequence)

    assert code_point.init_raw_type == StrRawType.UTF_8
    assert str(code_point) == utf_8_input_sequence
    assert code_point.raw_utf_8_length == len(utf_8_input_sequence)

    assert code_point.unicode_value == expected_unicode_value
    assert code_point.code_point_type == expected_code_point_type
    assert code_point.code_point_plane_type == expected_code_point_plane_type

    assert unicode(code_point) == expected_utf_16_sequence
    assert code_point.raw_utf_16_length == len(expected_utf_16_sequence)

def perform_test_for_utf_16_input_sequence(utf_16_input_sequence,
                                           expected_unicode_value,
                                           expected_code_point_type,
                                           expected_code_point_plane_type,
                                           expected_utf_8_sequence):

    code_point = CodePoint(utf_16_input_sequence)

    assert code_point.init_raw_type == StrRawType.UTF_16
    assert unicode(code_point) == utf_16_input_sequence
    assert code_point.raw_utf_16_length == len(utf_16_input_sequence)

    assert code_point.unicode_value == expected_unicode_value
    assert code_point.code_point_type == expected_code_point_type
    assert code_point.code_point_plane_type == expected_code_point_plane_type

    assert str(code_point) == expected_utf_8_sequence
    assert code_point.raw_utf_8_length == len(expected_utf_8_sequence)

def test_code_point_utf_8_one_byte():
    # Code point U+004E - Latin Capital Letter N
    perform_test_for_utf_8_input_sequence(
        utf_8_input_sequence='\x4E',
        expected_unicode_value=0x004E,
        expected_code_point_type=CodePointType.REGULAR,
        expected_code_point_plane_type=CodePointPlaneType.BASIC_MULTILINGUAL_PLANE,
        expected_utf_16_sequence=u'\u004E')

def test_code_point_utf_8_two_bytes():
    # Code point U+05D8 - Hebrew Letter Tet
    perform_test_for_utf_8_input_sequence(
        utf_8_input_sequence='\xD7\x98',
        expected_unicode_value=0x05D8,
        expected_code_point_type=CodePointType.REGULAR,
        expected_code_point_plane_type=CodePointPlaneType.BASIC_MULTILINGUAL_PLANE,
        expected_utf_16_sequence=u'\u05D8')

def test_code_point_utf_8_three_bytes():
    # Code point U+2702 - Black Scissors
    perform_test_for_utf_8_input_sequence(
        utf_8_input_sequence='\xE2\x9C\x82',
        expected_unicode_value=0x2702,
        expected_code_point_type=CodePointType.REGULAR,
        expected_code_point_plane_type=CodePointPlaneType.BASIC_MULTILINGUAL_PLANE,
        expected_utf_16_sequence=u'\u2702')

def test_code_point_utf_8_four_bytes():
    # Code point U+1F600 - Grinning Face
    perform_test_for_utf_8_input_sequence(
        utf_8_input_sequence='\xF0\x9F\x98\x80',
        expected_unicode_value=0x1F600,
        expected_code_point_type=CodePointType.REGULAR,
        expected_code_point_plane_type=CodePointPlaneType.SUPPLEMENTARY_PLANE,
        expected_utf_16_sequence=u'\uD83D\uDE00')

def test_code_point_utf_16_one_word():
    # Code point U+304F - Hiragana Letter Ku
    perform_test_for_utf_16_input_sequence(
        utf_16_input_sequence=u'\u304F',
        expected_unicode_value=0x304F,
        expected_code_point_type=CodePointType.REGULAR,
        expected_code_point_plane_type=CodePointPlaneType.BASIC_MULTILINGUAL_PLANE,
        expected_utf_8_sequence='\xE3\x81\x8F')

def test_code_point_utf_16_two_words():
    # Code point U+1F3FB - Emoji Modifier Fitzpatrick Type-1-2
    perform_test_for_utf_16_input_sequence(
        utf_16_input_sequence=u'\uD83C\uDFFB',
        expected_unicode_value=0x1F3FB,
        expected_code_point_type=CodePointType.FITZPATRICK_MODIFIER,
        expected_code_point_plane_type=CodePointPlaneType.SUPPLEMENTARY_PLANE,
        expected_utf_8_sequence='\xF0\x9F\x8F\xBB')
