#pattern searching algorithm
def pattern_search(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            print(f"Pattern found at index {i}")

text = "ABABCABAB"
pattern = "ABAB"
pattern_search(text, pattern)
