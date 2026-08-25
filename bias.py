def mitigate_bias(answer):

    replacements = {
        "man": "person",
        "woman": "person",
        "black": "person",
        "white": "person",
        "rich": "person",
        "poor": "person"
    }

    result = answer

    for word, replacement in replacements.items():

        result = result.replace(
            word,
            replacement
        )

        result = result.replace(
            word.capitalize(),
            replacement
        )

    return result
