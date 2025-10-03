def solution(message, K):
    # If the message fits, return as is
    if len(message) <= K:
        return message

    DOTS = " ..."
    words = message.split()
    cropped = ""
    for word in words:
        # Check if adding the next word and "….." fits within K
        if cropped:
            next_len = len(cropped) + 1 + len(word) + len(DOTS)  # 1 for space, 4 for " ..."
        else:
            next_len = len(word) + len(DOTS)  # No leading space for the first word

        if next_len > K:
            break
        cropped = (cropped + " " + word) if cropped else word
        
    # If no words fit, return just "..."
    return f"{cropped} ..." if cropped else "..."


if __name__ == "__main__":
    print(solution("Hello World", 10))
    # "Hello World ..."

    print(solution("And now here is my secret", 15))
    # "And now ..."

    print(solution("There is an animal with four legs", 15))
    # "There is an ..."

    print(solution("super dog", 4))
    # "..."

    print(solution("how are you", 20))
    # "how are you"