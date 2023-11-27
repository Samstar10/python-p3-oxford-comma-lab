def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        joined_item = ', '.join(items[:-1])
        return f"{joined_item}, and {items[-1]}"
