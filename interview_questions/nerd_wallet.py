"""
Context
As part of the move over to this new vendor, we need to migrate data that currently lives in our old vendor to our new vendor (Iterable)
Luckily, our old vendor provides us with such data (example below)
One major implementation detail: Our old vendor only allowed a top level of attributes and a 1-level dictionary value (if that attribute had child attributes) - we do not have this constraint with our new vendor and so we must unflatten this data
Data is flattened using double underscores __ between parent and child, for every level of nesting

# Old vendor:

{
    "top_level_attribute1": {
        "top_level_attribute2": {
            "parent_attribute__child_A": "value_A",
            "parent_attribute__child_B": "value_B"
        }
    },
    "another_top_level_attribute": "its value"
}

# Iterable (new vendor)

{
    "top_level_attribute": {
        "parent_attribute": {
            "child_A": "value_A",
            "child_B": "value_B"
        }
    },
    "another_top_level_attribute": "its value"
}

Acceptance Criteria
Enable this functionality for both events and users to take old vendor data and store it in our new vendor by
Implementing the following helper method
"""


def unflatten(obj):
    res = {}

    for key, value in obj.items():
        if isinstance(value, dict):
            res[key] = {}
            for flat_key, flat_value in value.items():
                parent, child = flat_key.split("__")
                if parent in res[key]:
                    res[key][parent].update({child: flat_value})
                else:
                    res[key][parent] = {child: flat_value}

        if isinstance(value, str):
            res[key] = value

    return res


def unflatten_recursive(old_obj):
    def recursive(mydict, ans):
        for key, value in mydict.items():
            if isinstance(value, str):
                if "__" in key:
                    parent, child = key.split("__")
                    if parent not in ans:
                        ans[parent] = {}
                    recursive({child: value}, [parent])
                else:
                    ans[key] = value

            elif isinstance(value, dict):
                ans[key] = {}
                recursive(mydict[key], ans[key])

        return ans

    return recursive(old_obj, {})


def unflatten_recursive2(flat_dict):
    def insert_path(d, key, value):
        parts = key.split("__")
        for part in parts[:-1]:
            d = d.setdefault(part, {})
        d[parts[-1]] = value

    result = {}
    for key, value in flat_dict.items():
        if isinstance(value, dict):
            # Recursively unflatten any nested dictionaries
            result[key] = unflatten_recursive(value)
        else:
            insert_path(result, key, value)

    return result


input1 = {
    "top_level_attribute": {
        "parent_attribute__child_A": "value_A",
        "parent_attribute__child_B": "value_B"
    },
    "another_top_level_attribute": "its value"
}

output1 = {
    "top_level_attribute": {
        "parent_attribute": {
            "child_A": "value_A",
            "child_B": "value_B"
        }
    },
    "another_top_level_attribute": "its value"
}

input2 = {
    "top_level_attribute": {
        "mid_level_attribute": {
            "parent_attribute__child_A": "value_A",
            "parent_attribute__child_B": "value_B"
        }
    },
    "another_top_level_attribute": "its value"
}

output2 = {
    "top_level_attribute": {
        "mid_level_attribute": {
            "parent_attribute": {
                "child_A": "value_A",
                "child_B": "value_B"
            }
        }
    },
    "another_top_level_attribute": "its value"
}

assert unflatten_recursive(input1) == output1
assert unflatten_recursive(input2) == output2
