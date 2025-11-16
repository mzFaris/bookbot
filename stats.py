def get_num_words(str):
    return len(str.split())

def get_each_char_count(str):
    result = {}
    for c in str.lower():
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result

def sort_num(dict):
    return dict["num"]

def sort_by_num_counts(dict):
    dict.sort(reverse=True, key=sort_num)
    return dict
