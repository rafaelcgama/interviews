### AFFIRM ###

def shortestUniqueSubstr(name_list):
    result = {}

    for name in name_list:
        result[name] = name

        for i in range(len(name)):
            for j in range(i + 1, len(name)):
                substring = name[i: j]
                add_substring = True
                for name2 in name_list:
                    if (name2 != name) and (substring in name2):
                        add_substring = False
                        break

                if add_substring and len(substring) < len(result[name]):
                    result[name] = substring

    return result


def shortestUniqueSubstr2(name_list):
    def get_substrings(word):
        substrings = set()
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                substrings.add(word[i:j])

        return substrings

    substrings = {word: get_substrings(word) for word in name_list}
    result = {}
    for key, value in substrings.items():
        value_temp = set(value)
        for key2, value2 in substrings.items():
            if key != key2:
                value_temp -= value2
        result[key] = min(value_temp, key=len)

    return result


if __name__ == '__main__':
    name_list = ["cheapair", "cheapoair", "peloton", "pelican"]
