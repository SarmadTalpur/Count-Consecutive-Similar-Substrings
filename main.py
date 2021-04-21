def count_squares(s):
    count = 0
    # calculating half of string, so we can make maximum substrings of that length for searching
    half = len(s) // 2
    # using loop to keep decreasing length of substring until 0
    while half > 0:
        for i in range(len(s) // half):
            # substring starts from 0 and goes on till half of original string
            # keep checking substring with the remaining string ahead
            if s[i + half:i + half * 2] == (s[i:i + half]):
                # if substring and string matches, iterate the counter variable
                count = count + 1
        # when substring of max length is checked completely, we decrease substring length
        half = half - 1
    return count


test = "12312333"
print(count_squares(test))