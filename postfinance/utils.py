def dict_to_ordered_qs(in_dict: dict, separator: str) -> str:
    ordered_kv = sorted(in_dict.items(), key=lambda d: str(d[0]))
    return separator.join(["=".join([str(k), str(v)]) for k, v in ordered_kv])
