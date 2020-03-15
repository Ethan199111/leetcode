# abcabcbd
# abc 
# return abc


def non_repeat_string(s):
    max_length = 0
    start = 0
    end = 0
    left = 0
    st = set()
    for i in range(len(s)):
        while s[i] in st:
            left += 1
            st.remove(s[i])
        st.add(s[i])
        if len(st) > max_length:
            start = left
            end = i
            max_length = len(st)
    return s[start:end + 1]


print(non_repeat_string("abcefabcefg"))
print(non_repeat_string("abcabcdabcde"))
