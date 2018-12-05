from functools import lru_cache


@lru_cache()
def get_edit_distance(str1, str2):
    if str1 == str2:
        return 0
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)
    last_char_distance = 0 if str1[-1] == str2[-1] else 1
    return min(
        [
            get_edit_distance(str1[:len(str1) - 1], str2) + 1,
            get_edit_distance(str1, str2[:len(str2) - 1]) + 1,
            get_edit_distance(str1[:len(str1) - 1], str2[:len(str2) - 1]) + last_char_distance
        ]
    )
