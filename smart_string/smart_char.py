from enum import Enum
from code_point import CodePoint
from smart_string_constants import SmartStrException


class SmartCharType(Enum):
    # The char consists of a single unicode code point.
    SIMPLE = 0
    # The char consists of two unicode code points.
    COMPOSITE = 1


class SmartChar(object):
    """
    This class represents a single graphic character. It can be a simple character like tha
    latin letter 'a' (single unicode code point), or a more complicated one like the Latvian
    national flag symbol (two unicode code points), but in both cases the character has a
    single graphic symbol representation.
    """

    def __init__(self, code_points):
        if isinstance(code_points, list):
            self._validate_list_input(code_points)
            self._code_points = code_points
        else:
            self._validate_non_list_input(code_points)
            self._code_points = [code_points]

    @property
    def char_type(self):
        if len(self._code_points) == 1:
            return SmartCharType.SIMPLE
        else:
            return SmartCharType.COMPOSITE

    @property
    def code_points(self):
        return self._code_points

    @property
    def code_points_count(self):
        return len(self._code_points)

    @property
    def char_plane_type(self):
        return self._code_points[0].code_point_plane_type

    def __len__(self):
        return len(self._code_points)

    def __getitem__(self, i):
        if i < 0 or i > len(self._code_points) - 1:
            raise SmartStrException(
                'Illegal index {} for the Smart Char subscript operator.'.format(i))
        return self._code_points[i]

    def __str__(self):
        smart_char_str = ''.join([str(code_point) for code_point in self._code_points])
        return smart_char_str

    def __unicode__(self):
        smart_char_unicode = u''.join([unicode(code_point) for code_point in self._code_points])
        return smart_char_unicode

    @staticmethod
    def _validate_list_input(code_points):
        if len(code_points) > 2:
            raise SmartStrException(
                'The list to initialize the Smart Char object is too long - {} objects.'.format(
                    len(code_points)))
        for code_point in code_points:
            if not isinstance(code_point, CodePoint):
                raise SmartStrException(
                    'Illegal type {} of an object in the list used for the Smart Char initialization.'.format(
                        type(code_point)))
        # TODO - If there are exactly 2 code point objects in the list verify that those objects
        # are consistent with each other to form a valid character.

    @staticmethod
    def _validate_non_list_input(code_point):
        if not isinstance(code_point, CodePoint):
            raise SmartStrException(
                'Illegal type {} for the Smart Char initialization.'.format(type(code_point)))
