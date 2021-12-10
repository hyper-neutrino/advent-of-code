t = []

m = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}

s = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

for line in lines:
    st = []
    for c in line:
        if c in m:
            st.append(m[c])
        elif c == st[-1]:
            st.pop()
        else:
            break
    else:
        v = 0
        for c in st[::-1]:
            v *= 5
            v += s[c]
        t += [v]

t.sort()
print(t[len(t) // 2])
