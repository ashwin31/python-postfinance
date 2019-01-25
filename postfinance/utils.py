import re

ITEM_REGEXP = re.compile("^(ITEM[A-Za-z].+)([0-9]+)$", re.IGNORECASE)


def _sort_func(d):
    key = str(d[0])
    re_match = ITEM_REGEXP.match(key)
    if re_match:
        fn, i = re_match.groups(0)
        return fn, int(i)
    return key, 0


def dict_to_ordered_qs(in_dict: dict, separator: str) -> str:
    ordered_kv = sorted(in_dict.items(), key=_sort_func)
    return separator.join(["=".join([str(k), str(v)]) for k, v in ordered_kv])
