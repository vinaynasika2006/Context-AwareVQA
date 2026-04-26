def mitigate_bias(answer):
    biased_words = ["man", "woman", "black", "white", "rich", "poor"]
    for word in biased_words:
        if word in answer.lower():
            answer = answer.replace(word, "person")
    return answer
