from enum import Enum
from smart_string_constants import (
    SmartStrException,
    StrInitInputType,
)


UNICODE_HIGH_SURROGATE_START = 0xD800
UNICODE_HIGH_SURROGATE_END = 0xDBFF
UNICODE_LOW_SURROGATE_START = 0xDC00
UNICODE_LOW_SURROGATE_END = 0xDFFF

UNICODE_REGIONAL_INDICATOR_START = 0x1F1E6
UNICODE_REGIONAL_INDICATOR_END = 0x1F1FF

UNICODE_FITZPATRICK_MODIFIER_START = 0x1F3FB
UNICODE_FITZPATRICK_MODIFIER_END = 0x1F3FF

UNICODE_HUMAN_EMOJI_VALUES = {
    0x1F385, 0x1F3C2, 0x1F3C3, 0x1F3C4, 0x1F3C7, 0x1F3CA, 0x1F3CB, 0x1F3CC, 0x1F442, 0x1F443,
    0x1F446, 0x1F447, 0x1F448, 0x1F449, 0x1F44A, 0x1F44B, 0x1F44C, 0x1F44D, 0x1F44E, 0x1F44F,
    0x1F450, 0x1F466, 0x1F467, 0x1F468, 0x1F469, 0x1F46E, 0x1F470, 0x1F471, 0x1F472, 0x1F473,
    0x1F474, 0x1F475, 0x1F476, 0x1F477, 0x1F478, 0x1F47C, 0x1F481, 0x1F482, 0x1F483, 0x1F485,
    0x1F486, 0x1F487, 0x1F4AA, 0x1F574, 0x1F575, 0x1F57A, 0x1F590, 0x1F595, 0x1F596,
}


class CodePointType(Enum):
    REGULAR = 0
    REGIONAL_INDICATOR = 1
    HUMAN_EMOJI = 2
    FITZPATRICK_MODIFIER = 3


class CodePointPlaneType(Enum):
    BASIC_MULTILINGUAL_PLANE = 0
    SUPPLEMENTARY_PLANE = 1


class CodePoint(object):

    def __init__(self, raw_input):

        if isinstance(raw_input, int):
            self._init_raw_type = StrInitInputType.UNICODE_VAL
            self._raw_utf_8_sequence = None
            self._raw_utf_16_sequence = None
            self._unicode_value = self.get_validated_unicode_value(raw_input)
        elif isinstance(raw_input, str):
            self._init_raw_type = StrInitInputType.UTF_8
            self._raw_utf_8_sequence = raw_input
            self._raw_utf_16_sequence = None
            self._unicode_value = self.get_utf_8_code_point_value(raw_input)
        elif isinstance(raw_input, unicode):
            self._init_raw_type = StrInitInputType.UTF_16
            self._raw_utf_8_sequence = None
            self._raw_utf_16_sequence = raw_input
            self._unicode_value = self.get_utf_16_code_point_value(raw_input)
        else:
            raise SmartStrException(
                'Illegal Code Point raw input type {}.'.format(type(raw_input)))

        self._code_point_type = self.get_code_point_type(self._unicode_value)

    @property
    def init_raw_type(self):
        """
        The type of the input that was used to initialize this instance of the CodePoint object.
        """
        return self._init_raw_type

    @property
    def raw_utf_8_length(self):
        if not self._raw_utf_8_sequence:
            self._raw_utf_8_sequence = self.get_utf_8_code_point_sequence(self._unicode_value)
        return len(self._raw_utf_8_sequence)

    @property
    def raw_utf_16_length(self):
        if not self._raw_utf_16_sequence:
            self._raw_utf_16_sequence = self.get_utf_16_code_point_sequence(self._unicode_value)
        return len(self._raw_utf_16_sequence)

    @property
    def unicode_value(self):
        return self._unicode_value

    @property
    def code_point_type(self):
        return self._code_point_type

    @property
    def code_point_plane_type(self):
        plane_type = self.get_code_point_plane_type(self._unicode_value)
        return plane_type

    def __str__(self):
        if not self._raw_utf_8_sequence:
            self._raw_utf_8_sequence = self.get_utf_8_code_point_sequence(self._unicode_value)
        return self._raw_utf_8_sequence

    def __unicode__(self):
        if not self._raw_utf_16_sequence:
            self._raw_utf_16_sequence = self.get_utf_16_code_point_sequence(self._unicode_value)
        return self._raw_utf_16_sequence

    @staticmethod
    def get_validated_unicode_value(unicode_value):
        if unicode_value >= 0x0000 and unicode_value <= 0x10FFFF:
            return unicode_value
        else:
            raise SmartStrException(
                'Int value {} is not a valid value for a Unicode code point'.format(
                    unicode_value))

    @staticmethod
    def get_utf_8_code_point_value(utf_8_raw_sequence):

        utf_8_raw_sequence_len = len(utf_8_raw_sequence)
        if utf_8_raw_sequence_len == 1:
            byte_0_numeric_val = ord(utf_8_raw_sequence[0])
            byte_0_effective_val = byte_0_numeric_val & 0b01111111
            code_point_value = byte_0_effective_val
        elif utf_8_raw_sequence_len == 2:
            byte_0_numeric_val = ord(utf_8_raw_sequence[0])
            byte_1_numeric_val = ord(utf_8_raw_sequence[1])
            byte_0_effective_val = byte_0_numeric_val & 0b00011111
            byte_1_effective_val = byte_1_numeric_val & 0b00111111
            code_point_value = (byte_0_effective_val << 6) + byte_1_effective_val
        elif utf_8_raw_sequence_len == 3:
            byte_0_numeric_val = ord(utf_8_raw_sequence[0])
            byte_1_numeric_val = ord(utf_8_raw_sequence[1])
            byte_2_numeric_val = ord(utf_8_raw_sequence[2])
            byte_0_effective_val = byte_0_numeric_val & 0b00001111
            byte_1_effective_val = byte_1_numeric_val & 0b00111111
            byte_2_effective_val = byte_2_numeric_val & 0b00111111
            code_point_value = ((byte_0_effective_val << 12) +
                                (byte_1_effective_val << 6) +
                                byte_2_effective_val)
        elif utf_8_raw_sequence_len == 4:
            byte_0_numeric_val = ord(utf_8_raw_sequence[0])
            byte_1_numeric_val = ord(utf_8_raw_sequence[1])
            byte_2_numeric_val = ord(utf_8_raw_sequence[2])
            byte_3_numeric_val = ord(utf_8_raw_sequence[3])
            byte_0_effective_val = byte_0_numeric_val & 0b00000111
            byte_1_effective_val = byte_1_numeric_val & 0b00111111
            byte_2_effective_val = byte_2_numeric_val & 0b00111111
            byte_3_effective_val = byte_3_numeric_val & 0b00111111
            code_point_value = ((byte_0_effective_val << 18) +
                                (byte_1_effective_val << 12) +
                                (byte_2_effective_val << 6) +
                                byte_3_effective_val)
        else:
            raise SmartStrException(
                'UTF-8 sequence of length {} does not represent a valid code point.'.format(
                    utf_8_raw_sequence_len))

        return code_point_value

    @staticmethod
    def get_utf_8_code_point_sequence(code_point_unicode_value):

        utf_8_code_point_sequence = ''
        if code_point_unicode_value >= 0x0000 and code_point_unicode_value <= 0x007F:
            byte_0_numeric_val = code_point_unicode_value
            utf_8_code_point_sequence = chr(byte_0_numeric_val)
        elif code_point_unicode_value >= 0x0080 and code_point_unicode_value <= 0x07FF:
            byte_0_numeric_val = 0b11000000 | (code_point_unicode_value >> 6)
            byte_1_numeric_val = 0b10000000 | (code_point_unicode_value & 0b00111111)
            utf_8_code_point_sequence += chr(byte_0_numeric_val)
            utf_8_code_point_sequence += chr(byte_1_numeric_val)
        elif code_point_unicode_value >= 0x0800 and code_point_unicode_value <= 0xFFFF:
            byte_0_numeric_val = 0b11100000 | (code_point_unicode_value >> 12)
            byte_1_numeric_val = 0b10000000 | ((code_point_unicode_value >> 6) & 0b00111111)
            byte_2_numeric_val = 0b10000000 | (code_point_unicode_value & 0b00111111)
            utf_8_code_point_sequence += chr(byte_0_numeric_val)
            utf_8_code_point_sequence += chr(byte_1_numeric_val)
            utf_8_code_point_sequence += chr(byte_2_numeric_val)
        elif code_point_unicode_value >= 0x10000 and code_point_unicode_value <= 0x10FFFF:
            byte_0_numeric_val = 0b11110000 | (code_point_unicode_value >> 18)
            byte_1_numeric_val = 0b10000000 | ((code_point_unicode_value >> 12) & 0b00111111)
            byte_2_numeric_val = 0b10000000 | ((code_point_unicode_value >> 6) & 0b00111111)
            byte_3_numeric_val = 0b10000000 | (code_point_unicode_value & 0b00111111)
            utf_8_code_point_sequence += chr(byte_0_numeric_val)
            utf_8_code_point_sequence += chr(byte_1_numeric_val)
            utf_8_code_point_sequence += chr(byte_2_numeric_val)
            utf_8_code_point_sequence += chr(byte_3_numeric_val)
        else:
            raise SmartStrException(
                'Unicode code point value {} is illegal.'.format(code_point_unicode_value))

        return utf_8_code_point_sequence

    @staticmethod
    def get_utf_16_code_point_value(utf_16_raw_sequence):

        utf_16_raw_sequence_len = len(utf_16_raw_sequence)
        if utf_16_raw_sequence_len == 1:
            code_point_value = ord(utf_16_raw_sequence)
        elif utf_16_raw_sequence_len == 2:
            high_surrogate = utf_16_raw_sequence[0]
            low_surrogate = utf_16_raw_sequence[1]
            code_point_value = (0x10000 +
                                ((ord(high_surrogate) - 0xD800) * 0x400) +
                                (ord(low_surrogate) - 0xDC00))
        else:
            raise SmartStrException(
                'UTF-16 sequence of length {} does not represent a valid code point.'.format(
                    len(utf_16_raw_sequence)))

        return code_point_value

    @staticmethod
    def get_utf_16_code_point_sequence(code_point_unicode_value):

        utf_16_code_point_sequence = u''
        if code_point_unicode_value >= 0x0000 and code_point_unicode_value <= 0xFFFF:
            utf_16_code_point_sequence = unichr(code_point_unicode_value)
        elif code_point_unicode_value >= 0x10000 and code_point_unicode_value <= 0x10FFFF:
            high_surrogate = ((code_point_unicode_value - 0x10000) / 0x400) + 0xD800
            low_surrogate = ((code_point_unicode_value - 0x10000) % 0x400) + 0xDC00
            utf_16_code_point_sequence += unichr(high_surrogate)
            utf_16_code_point_sequence += unichr(low_surrogate)
        else:
            raise SmartStrException(
                'Unicode code point value {} is illegal.'.format(code_point_unicode_value))

        return utf_16_code_point_sequence

    @staticmethod
    def get_code_point_type(code_point_unicode_value):
        if (code_point_unicode_value >= UNICODE_REGIONAL_INDICATOR_START and
                code_point_unicode_value <= UNICODE_REGIONAL_INDICATOR_END):
            code_point_type = CodePointType.REGIONAL_INDICATOR
        elif code_point_unicode_value in UNICODE_HUMAN_EMOJI_VALUES:
            code_point_type = CodePointType.HUMAN_EMOJI
        elif (code_point_unicode_value >= UNICODE_FITZPATRICK_MODIFIER_START and
                  code_point_unicode_value <= UNICODE_FITZPATRICK_MODIFIER_END):
            code_point_type = CodePointType.FITZPATRICK_MODIFIER
        else:
            code_point_type = CodePointType.REGULAR
        return code_point_type

    @staticmethod
    def get_code_point_plane_type(code_point_unicode_value):
        if code_point_unicode_value <= 0xFFFF:
            code_point_plane_type = CodePointPlaneType.BASIC_MULTILINGUAL_PLANE
        else:
            code_point_plane_type = CodePointPlaneType.SUPPLEMENTARY_PLANE
        return code_point_plane_type
