t = 0

m = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}

s = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

for line in lines:
    st = []
    for c in line:
        if c in m:
            st.append(m[c])
        elif c == st[-1]:
            st.pop()
        else:
            t += s[c]
            break

print(t)
