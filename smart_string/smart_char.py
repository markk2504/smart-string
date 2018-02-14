from smart_string_constants import SmartStrException


class SmartChar(object):

    def __init__(self, code_points):
        if isinstance(code_points, list):
            self._code_points = code_points
        else:
            self._code_points = [code_points]

    @property
    def code_points(self):
        return self._code_points

    @property
    def code_points_count(self):
        return len(self._code_points)

    @property
    def char_type(self):
        return self._code_points[0].code_point_type

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
