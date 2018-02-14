from code_point import (
    CodePoint,
    CodePointType,
    UNICODE_HIGH_SURROGATE_START,
    UNICODE_HIGH_SURROGATE_END,
    UNICODE_LOW_SURROGATE_START,
    UNICODE_LOW_SURROGATE_END,
)
from smart_char import SmartChar
from smart_string_constants import (
    SmartStrException,
    StrRawType,
)


class SmartStr(object):

    def __init__(self, raw_sequence):

        if isinstance(raw_sequence, str):
            self._init_raw_type = StrRawType.UTF_8
            self._raw_utf_8_sequence = raw_sequence
            self._raw_utf_16_sequence = None
            self._characters = []
            self._process_rew_utf_8_str()
        elif isinstance(raw_sequence, unicode):
            self._init_raw_type = StrRawType.UTF_16
            self._raw_utf_8_sequence = None
            self._raw_utf_16_sequence = raw_sequence
            self._characters = []
            self._process_rew_utf_16_str()
        else:
            raise SmartStrException(
                'Illegal Smart String raw sequence type {}.'.format(type(raw_sequence)))

    @property
    def init_raw_type(self):
        """
        The type of the string of the raw sequence that was used to initialize this instance of
        the SmartStr object.
        """
        return self._init_raw_type

    @property
    def characters(self):
        return self._characters

    @property
    def characters_count(self):
        return len(self._characters)

    @property
    def code_points(self):
        str_code_points = []
        for ch in self._characters:
            str_code_points += ch.code_points
        return str_code_points

    @property
    def code_points_count(self):
        str_code_points_count = 0
        for ch in self._characters:
            str_code_points_count += ch.code_points_count
        return str_code_points_count

    def __len__(self):
        return len(self._characters)

    def __getitem__(self, i):
        if i < 0 or i > len(self._characters) - 1:
            raise SmartStrException(
                'Illegal index {} for the Smart String subscript oparator.'.format(i))
        return self.characters[i]

    def __str__(self):
        if not self._raw_utf_8_sequence:
            self._build_utf_8_sequence_from_characters()
        return self._raw_utf_8_sequence

    def __unicode__(self):
        if not self._raw_utf_16_sequence:
            self._build_utf_16_sequence_from_characters()
        return self._raw_utf_16_sequence

    def _build_utf_8_sequence_from_characters(self):
        self._raw_utf_8_sequence = ''.join([str(ch) for ch in self._characters])

    def _build_utf_16_sequence_from_characters(self):
        self._raw_utf_16_sequence = u''.join([unicode(ch) for ch in self._characters])

    def _process_rew_utf_8_str(self):

        current_byte_idx = 0
        previous_code_point = None

        while current_byte_idx < len(self._raw_utf_8_sequence):

            current_byte = self._raw_utf_8_sequence[current_byte_idx]
            current_byte_ordinal = ord(current_byte)

            if current_byte_ordinal < 0x80:
                # The current byte is in the range 00000000 - 01111111.
                # The actual code point is an ascii char that occupies 1 byte.
                current_code_point_bytes_count = 1
                self._validate_utf_8_code_point_consistency(current_byte_idx,
                                                            current_code_point_bytes_count)
            elif current_byte_ordinal < 0xE0:
                # The current byte is in the range 11000000 - 11011111.
                current_code_point_bytes_count = 2
                self._validate_utf_8_code_point_consistency(current_byte_idx,
                                                            current_code_point_bytes_count)
            elif current_byte_ordinal < 0xF0:
                # The current byte is in the range 11100000 - 11101111.
                current_code_point_bytes_count = 3
                self._validate_utf_8_code_point_consistency(current_byte_idx,
                                                            current_code_point_bytes_count)
            elif current_byte_ordinal < 0xF8:
                # The current byte is in the range 11110000 - 11110111.
                current_code_point_bytes_count = 4
                self._validate_utf_8_code_point_consistency(current_byte_idx,
                                                            current_code_point_bytes_count)
            else:
                raise SmartStrException(
                    'UTF-8 str format error. Illegal format for the starting byte of a code point.')

            current_code_point_sequence = self._raw_utf_8_sequence[
                current_byte_idx:current_byte_idx+current_code_point_bytes_count]
            current_code_point = CodePoint(current_code_point_sequence)

            current_byte_idx += current_code_point_bytes_count

            last_code_point_in_str = current_byte_idx == len(self._raw_utf_8_sequence)
            previous_code_point = self._convert_code_points_to_char(previous_code_point,
                                                                    current_code_point,
                                                                    last_code_point_in_str)

    def _validate_utf_8_code_point_consistency(self,
                                               code_point_start_byte_index,
                                               code_point_bytes_count):

        # Make sure that the UTF-8 str has sufficient length to accommodate all the bytes of the
        # code point.
        if code_point_start_byte_index + code_point_bytes_count > len(self._raw_utf_8_sequence):
            raise SmartStrException(
                'UTF-8 str format error. Code point at index {} is of size {}, but the total length of the str is {}.'.format(
                    code_point_start_byte_index, code_point_bytes_count, len(self._raw_utf_8_sequence)))

        # Validate the format of the trailing bytes of the code point.
        for i in range(code_point_start_byte_index + 1,
                       code_point_start_byte_index + code_point_bytes_count):

            current_trailing_byte = self._raw_utf_8_sequence[i]
            current_trailing_byte_ordinal = ord(current_trailing_byte)

            # Make sure that the trailing bytes of the code point have the correct format
            # (10000000 - 10111111).
            if current_trailing_byte_ordinal < 0x80 or current_trailing_byte_ordinal > 0xBF:
                raise SmartStrException(
                    'UTF-8 str format error. Code point trailing byte has a faulty format (byte at index {} of size {}, offset {}).'.format(
                        code_point_start_byte_index, code_point_bytes_count, i - code_point_start_byte_index))

    def _process_rew_utf_16_str(self):

        current_word_idx = 0
        previous_code_point = None

        while current_word_idx < len(self._raw_utf_16_sequence):

            current_word = self._raw_utf_16_sequence[current_word_idx]

            if self._is_utf_16_high_surrogate(current_word):
                current_code_point_words_count = 2
                self._validate_utf_16_code_point_consistency(current_word_idx,
                                                             current_code_point_words_count)
            else:
                current_code_point_words_count = 1
                self._validate_utf_16_code_point_consistency(current_word_idx,
                                                             current_code_point_words_count)

            current_code_point_sequence = self._raw_utf_16_sequence[
                current_word_idx:current_word_idx + current_code_point_words_count]
            current_code_point = CodePoint(current_code_point_sequence)

            current_word_idx += current_code_point_words_count

            last_code_point_in_str = current_word_idx == len(self._raw_utf_16_sequence)
            previous_code_point = self._convert_code_points_to_char(previous_code_point,
                                                                    current_code_point,
                                                                    last_code_point_in_str)

    def _validate_utf_16_code_point_consistency(self,
                                                code_point_start_word_index,
                                                code_point_words_count):

        # Make sure that the UTF-16 str has sufficient length to accommodate all the words of the
        # code point.
        if code_point_start_word_index + code_point_words_count > len(self._raw_utf_16_sequence):
            raise SmartStrException(
                'UTF-16 str format error. Code point at index {} is of size {}, but the total length of the str is {}.'.format(
                    code_point_start_word_index, code_point_words_count, len(self._raw_utf_16_sequence)))

        # If the code point consists of 2 words, verify that those words are a surrogate pair
        # (high surrogate and low surrogate).
        if code_point_words_count == 2:
            # Verify that the first word is a high surrogate.
            first_code_point_word = self._raw_utf_16_sequence[code_point_start_word_index]
            if not self._is_utf_16_high_surrogate(first_code_point_word):
                raise SmartStrException(
                    'UTF-16 str format error. Code point consists of 2 words, but the first word is not a high surrogate (word at index {}).'.format(
                        code_point_start_word_index))
            # Verify that the second word is a low surrogate.
            second_code_point_word = self._raw_utf_16_sequence[code_point_start_word_index + 1]
            if not self._is_utf_16_low_surrogate(second_code_point_word):
                raise SmartStrException(
                    'UTF-16 str format error. Code point consists of 2 words, but the second word is not a low surrogate (word at index {}).'.format(
                        code_point_start_word_index + 1))

    def _convert_code_points_to_char(self,
                                     previous_code_point,
                                     current_code_point,
                                     last_code_point_in_str):
        new_previous_code_point = None
        if self._code_points_form_single_two_code_points_char(previous_code_point, current_code_point):
            # The previous code point and the current code point form a single character together.
            current_smart_char = SmartChar([previous_code_point, current_code_point])
            self.characters.append(current_smart_char)
        else:
            # The previous code point and the current code point do not form a single character
            # together.
            if previous_code_point:
                # The previous code point could be the first code point in a two code points
                # character, but the current code point cannot complete it. Therefore the
                # previous code point will form a character by itself.
                previous_smart_char = SmartChar(previous_code_point)
                self.characters.append(previous_smart_char)

            if (not last_code_point_in_str and
                    self._code_point_can_be_first_in_two_code_points_char(current_code_point)):
                # The current code point can be the first code point in a two code points
                # character, and there is at least one more potential code point in the str
                # to complete the current code point to such character.
                new_previous_code_point = current_code_point
            else:
                # The current code point cannot be the first code point in a two code points
                # character, therefore it will form a character by itself.
                current_smart_char = SmartChar(current_code_point)
                self.characters.append(current_smart_char)

        return new_previous_code_point

    @staticmethod
    def _is_utf_16_high_surrogate(word):
        word_ordinal = ord(word)
        if word_ordinal < UNICODE_HIGH_SURROGATE_START or word_ordinal > UNICODE_HIGH_SURROGATE_END:
            return False
        return True

    @staticmethod
    def _is_utf_16_low_surrogate(word):
        word_ordinal = ord(word)
        if word_ordinal < UNICODE_LOW_SURROGATE_START or word_ordinal > UNICODE_LOW_SURROGATE_END:
            return False
        return True

    @staticmethod
    def _code_points_form_single_two_code_points_char(first_code_point, second_code_point):
        if not first_code_point or not second_code_point:
            return False
        if (first_code_point.code_point_type == CodePointType.REGIONAL_INDICATOR and
                second_code_point.code_point_type == CodePointType.REGIONAL_INDICATOR):
            return True
        if (first_code_point.code_point_type == CodePointType.HUMAN_EMOJI and
                second_code_point.code_point_type == CodePointType.FITZPATRICK_MODIFIER):
            return True
        return False

    @staticmethod
    def _code_point_can_be_first_in_two_code_points_char(code_point):
        if not code_point:
            return False
        if code_point.code_point_type == CodePointType.REGIONAL_INDICATOR:
            return True
        if code_point.code_point_type == CodePointType.HUMAN_EMOJI:
            return True
        return False




###############################################################

byte_str_utf_8_latin_capital_letter_n = '\x4E'
byte_str_utf_8_hebrew_letter_tet = '\xD7\x98'
byte_str_utf_8_black_scissors = '\xE2\x9C\x82'
byte_str_utf_8_grinning_face = '\xF0\x9F\x98\x80'

byte_str_utf_8_national_flag_symbol_l = '\xF0\x9F\x87\xB1'
byte_str_utf_8_national_flag_symbol_v = '\xF0\x9F\x87\xBB'
byte_str_utf_8_latvian_flag = '\xF0\x9F\x87\xB1\xF0\x9F\x87\xBB'

byte_str_utf_8_woman = '\xF0\x9F\x91\xA9'
byte_str_utf_8_fitzpatrick_type_5 = '\xF0\x9F\x8F\xBE'
byte_str_utf_8_dark_woman = '\xF0\x9F\x91\xA9\xF0\x9F\x8F\xBE'

###############################################################

unicode_str_latin_capital_letter_n = u'\u004E'
unicode_str_hebrew_letter_tet = u'\u05D8'
unicode_str_black_scissors = u'\u2702'
unicode_str_grinning_face = u'\uD83D\uDE00'

unicode_str_national_flag_symbol_l = u'\uD83C\uDDF1'
unicode_str_national_flag_symbol_v = u'\uD83C\uDDFB'
unicode_str_latvian_flag = u'\uD83C\uDDF1\uD83C\uDDFB'

unicode_str_woman = u'\uD83D\uDC69'
unicode_str_fitzpatrick_type_5 = u'\uD83C\uDFFE'
unicode_str_dark_woman = u'\uD83D\uDC69\uD83C\uDFFE'


s = '\x4E\x20\xD7\x98\x20\xE2\x9C\x82\x20\xF0\x9F\x98\x80\x20\xF0\x9F\x87\xB1\xF0\x9F\x87\xBB\x20\xF0\x9F\x91\xA9\x20\xF0\x9F\x91\xA9\xF0\x9F\x8F\xBE\x20\xF0\x9F\x8F\xBE\x20\xF0\x9F\x91\xA9'

#s = u'\u004E\u0020\u05D8\u0020\u2702\u0020\uD83D\uDE00\u0020\uD83C\uDDF1\uD83C\uDDFB\u0020\uD83D\uDC69\u0020\uD83D\uDC69\uD83C\uDFFE\u0020\uD83C\uDFFE\u0020\uD83D\uDC69'


print '********************************************'

for c in s:
    print c

print '********************************************'

smart_str = SmartStr(s)
for c in smart_str.characters:
    print c

print '********************************************'

print str(smart_str)
print unicode(smart_str)

print smart_str.code_points
for cp in smart_str.code_points:
    print cp

print smart_str.characters_count

for char in smart_str.characters:
    print'-------'
    print char
    #print char.raw_type
    #print char.raw_length
    print char.code_points_count

    print 'Value: 0x%X' % char.code_points[0].unicode_value

    print'---'


uc = u'\uD83D\uDE00\uD83C\uDFFE'
print uc

print unicode_str_dark_woman
