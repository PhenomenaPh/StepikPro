def triangle_sandbox(word_tokens=16, init_token=1):
    if word_tokens == 4:
        text = str(init_token) * word_tokens
        print(f"{text: ^{16}}")
        return

    elif word_tokens > 4:
        text = str(init_token) * word_tokens
        print(f"{text: ^{16}}")
        triangle_sandbox(word_tokens - 4, init_token + 1)

    text = str(init_token) * word_tokens
    print(f"{text: ^{16}}")


triangle_sandbox()
