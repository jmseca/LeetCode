def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    def get_occurences_t(t):
        new_d = {}
        for char in t:
            if char not in new_d:
                new_d[char] = 1
            else:
                new_d[char] += 1
        return new_d

    def same_dict(occur, seen):
        # Granted that they have the same keys
        return all(map(lambda k: seen[k] >= occur[k], list(seen.keys())))

    occurences_t = get_occurences_t(t)
    seen = {char:0 for char in occurences_t}
    s_size = len(s)

    L, R = 0, 0
    window_size = 0
    output = ""

    while R < s_size:
        char = s[R]
        if char in seen:
            seen[char] += 1

            was_inside = same_dict(occurences_t, seen)
            # No need to check L<R
            while same_dict(occurences_t, seen):
                old_char = s[L]
                if old_char in seen:
                    seen[old_char]-=1
                L+=1
            if was_inside and (window_size > R-L+2 or not(window_size)):
                window_size = R-L+2
                output = s[(L-1):(R+1)]

        R += 1

    return output
        
        
s = "aaaaaaaaaaaabbbbbcdd"
t = "abcdd"

print(minWindow(s,t))