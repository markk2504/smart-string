import pytest
from smart_string.code_point import CodePoint, CodePointPlaneType
from smart_string.smart_char import SmartChar, SmartCharType
from smart_string.smart_string_constants import SmartStrException


def perform_test_for_smart_char(input_code_point_structure,
                                expected_smart_char_type,
                                expected_smart_char_plane_type,
                                expected_utf_8_sequence,
                                expected_utf_16_sequence):
    if isinstance(input_code_point_structure, list):
        expected_code_points = input_code_point_structure
        expected_code_points_count = len(input_code_point_structure)
    else:
        expected_code_points = [input_code_point_structure]
        expected_code_points_count = 1

    smart_char = SmartChar(input_code_point_structure)

    assert smart_char.char_type == expected_smart_char_type
    assert smart_char.code_points == expected_code_points
    assert smart_char.code_points_count == expected_code_points_count
    assert smart_char.char_plane_type == expected_smart_char_plane_type
    assert len(smart_char) == expected_code_points_count

    for i in range(expected_code_points_count):
        assert smart_char[i] == expected_code_points[i]

    assert str(smart_char) == expected_utf_8_sequence
    assert unicode(smart_char) == expected_utf_16_sequence

def test_smart_char_single_code_point_input():
    # U+0040 - Commercial At
    code_point = CodePoint(0x0040)
    perform_test_for_smart_char(
        input_code_point_structure=code_point,
        expected_smart_char_type=SmartCharType.SIMPLE,
        expected_smart_char_plane_type=CodePointPlaneType.BASIC_MULTILINGUAL_PLANE,
        expected_utf_8_sequence='\x40',
        expected_utf_16_sequence=u'\u0040')

def test_smart_char_single_code_point_list_input():
    # U+1F020 - Mahjong Tile Eight of Circles
    single_code_point_list = [CodePoint(0x1F020)]
    perform_test_for_smart_char(
        input_code_point_structure=single_code_point_list,
        expected_smart_char_type=SmartCharType.SIMPLE,
        expected_smart_char_plane_type=CodePointPlaneType.SUPPLEMENTARY_PLANE,
        expected_utf_8_sequence='\xF0\x9F\x80\xA0',
        expected_utf_16_sequence=u'\uD83C\uDC20')

def test_smart_char_two_code_points_list_input():
    # U+1F1F3 - Regional Indicator Symbol Letter N + U+1F1FF - Regional Indicator Symbol Letter Z
    # Together those 2 code points form a single graphic symbol - New Zealand flag.
    two_code_points_list = [CodePoint(0x1F1F3), CodePoint(0x1F1FF)]
    perform_test_for_smart_char(
        input_code_point_structure=two_code_points_list,
        expected_smart_char_type=SmartCharType.COMPOSITE,
        expected_smart_char_plane_type=CodePointPlaneType.SUPPLEMENTARY_PLANE,
        expected_utf_8_sequence='\xF0\x9F\x87\xB3\xF0\x9F\x87\xBF',
        expected_utf_16_sequence=u'\uD83C\uDDF3\uD83C\uDDFF')

def test_smart_char_illegal_type_input():
    with pytest.raises(SmartStrException) as exception_info:
        smart_char = SmartChar(123)
    assert exception_info.type is SmartStrException

def test_smart_char_illegal_list_length_input():
    with pytest.raises(SmartStrException) as exception_info:
        smart_char = SmartChar([CodePoint(0x0040), CodePoint(0x1F020), CodePoint(0x1F1F3)])
    assert exception_info.type is SmartStrException

def test_smart_char_illegal_list_object_type_input():
    with pytest.raises(SmartStrException) as exception_info:
        smart_char = SmartChar([CodePoint(0x0040), 123])
    assert exception_info.type is SmartStrException
