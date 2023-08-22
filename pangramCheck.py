def pangramCheck(s):
    # Write your code here
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    s_normalized = set(s.lower().replace(" ", ""))
    if alphabet.issubset(s_normalized):
        return "pangram"
    else:
        return "not pangram"
