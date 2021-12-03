import copy, hashlib, sys, sympy, traceback

silence = len(sys.argv) >= 4 and sys.argv[3] == "-"

def parse_num(s):
    if s and s[0] == "-":
        return -parse_num(s[1:])
    s = s.lower()
    if "i" in s:
        a, b = s.split("i")
        return parse_num(a) + sympy.I * parse_num(b)
    elif "e" in s:
        a, b = s.split("e")
        return parse_real(a) * sympy.Integer(10) ** parse_int(b)
    elif "b" in s:
        a, b = s.split("b")
        return sympy.Integer(2) ** parse_int(a) * parse_real(b, 2)
    elif "o" in s:
        a, b = s.split("o")
        return sympy.Integer(8) ** parse_int(a) * parse_real(b, 8)
    elif "x" in s:
        a, b = s.split("x")
        return sympy.Integer(16) ** parse_int(a) * parse_real(b, 16)
    else:
        return parse_real(s)

def parse_real(s, base = 10):
    digits = {
        2: "01",
        8: "01234567",
        10: "0123456789",
        16: "0123456789abcdef"
    }[base]
    if "." in s:
        left, right = s.split(".")
    else:
        left = s
        right = ""
    value = sympy.Integer(0)
    for i, c in enumerate(left[::-1]):
        value += sympy.Integer(base) ** i * digits.index(c)
    for i, c in enumerate(right):
        value += sympy.Integer(base) ** ~i * digits.index(c)
    return value

def parse_int(s):
    return sympy.Integer(s)

class Lexer:
    def __init__(self):
        self.tokens = []
        self.balance = 0
        # sqstring, dqstring, sqstringe, dqstringe, num_or_ident
        self.statetype = self.state = None

    def flush(self):
        if self.statetype == "num_or_ident":
            try:
                self.tokens.append(("number", parse_num(self.state)))
            except:
                self.tokens.append(("identifier", self.state))
        elif self.statetype is None:
            return
        else:
            raise RuntimeError("cannot flush string directly - finish the string")
        self.statetype = None
        self.state = None

    def feed(self, char):
        if self.statetype == "sqstring":
            if char == "'":
                self.tokens.append(("string", eval("'" + self.state.replace("\n", "\\n") + "'")))
                self.statetype = self.state = None
            elif char == "\\":
                self.state += "\\"
                self.statetype = "sqstringe"
            else:
                self.state += char
        elif self.statetype == "dqstring":
            if char == '"':
                self.tokens.append(("string", eval('"' + self.state.replace("\n", "\\n") + '"')))
                self.statetype = self.state = None
            elif char == "\\":
                self.state += "\\"
                self.statetype = "dqstringe"
            else:
                self.state += char
        elif self.statetype == "sqstringe":
            self.state += char
            self.statetype = "sqstring"
        elif self.statetype == "dqstringe":
            self.state += char
            self.statetype = "dqstringe"
        else:
            if char in "\"'()[]{}":
                self.flush()
                if char == "'":
                    self.statetype = "sqstring"
                    self.state = ""
                elif char == '"':
                    self.statetype = "dqstring"
                    self.state = ""
                else:
                    self.tokens.append(("bracket", "(" if char in "([{" else ")"))
                    self.balance += 1 if char in "([{" else -1
            elif char.isspace():
                self.flush()
            else:
                if self.statetype is None:
                    self.statetype = "num_or_ident"
                if self.state is None:
                    self.state = ""
                self.state += char

    def clear(self):
        self.flush()
        if self.balance:
            raise RuntimeError("balance is off; cannot clear yet")
        tokens = self.tokens[:]
        self.tokens[:] = []
        return tokens

def parse(tokens):
    if not tokens:
        return None
    if tokens[0] == ("bracket", "("):
        balance = 1
        tokens.pop(0)
        contents = []
        while True:
            if not tokens:
                raise RuntimeError("unclosed bracket - should be caught by lexer")
            token = tokens.pop(0)
            if token == ("bracket", "("):
                balance += 1
            elif token == ("bracket", ")"):
                balance -= 1
            if balance == 0:
                break
            contents.append(token)
        output = []
        while contents:
            output.append(parse(contents))
        return ("tree", output)
    return tokens.pop(0)

fn_registry = {}

class Function:
    def __init__(self, name, min, max = None):
        self.min = min
        if name is None:
            pass
        elif isinstance(name, str):
            fn_registry[name] = self
        else:
            for n in name:
                fn_registry[n] = self
        if max is None:
            self.max = min
        elif max == ...:
            self.max = float("inf")
        else:
            self.max = max
        self.f = lambda: 0
    def __call__(self, f):
        self.f = f
        return self

def op(s):
    return eval(f"lambda x, y: x {s} y")

def monad_vectorize(f):
    def _(x):
        return list(map(_, x)) if isinstance(x, list) else f(x)
    return _

def dyad_vectorize(f):
    def _(x, y):
        if isinstance(x, list):
            if isinstance(y, list):
                return [_(a, b) for a, b in zip(x, y)] + x[len(y):] + y[len(x):]
            else:
                return [_(x, b) for b in y]
        else:
            if isinstance(y, list):
                return [_(a, y) for a in x]
            else:
                return f(x, y)
    return _

def reduce(fn, array, left = True):
    if left:
        k = array[0]
        for q in array[1:]:
            k = fn(k, q)
        return k
    else:
        k = array[-1]
        for q in array[:-1][::-1]:
            k = fn(q, k)
        return k

@Function(("h", "hist", "history"), 1)
def _(x):
    return history[x]

for name, operator, left in [
    ("+", "+", 1),
    ("-", "-", 1),
    ("*", "*", 1),
    ("/", "/", 1),
    ("%", "%", 1),
    ("**", "**", 0),
    ("//", "//", 1),
    ("&&", " and ", 1),
    ("||", " or ", 1),
    ("<<", "<<", 1),
    (">>", ">>", 1)
]:
    Function(name, 2, ...)((lambda o: lambda *x: reduce(o, x))(dyad_vectorize(op(operator))))

@Function("&", 2, ...)
def _(*x):
    return sympy.Integer(reduce(dyad_vectorize(lambda x, y: x & y), list(map(int, x))))

@Function("|", 2, ...)
def _(*x):
    return sympy.Integer(reduce(dyad_vectorize(lambda x, y: x | y), list(map(int, x))))

@Function("^", 2, ...)
def _(*x):
    return sympy.Integer(reduce(dyad_vectorize(lambda x, y: x ^ y), list(map(int, x))))

@Function("=", 2, ...)
def _(*x):
    if len(x) == 2:
        return dyad_vectorize(lambda x, y: x == y)(*x)
    return all(x[0] == k for k in x[1:])

@Function("==", 2, ...)
def _(*x):
    return all(x[0] == k for k in x[1:])

@Function("!=", 2, ...)
def _(*x):
    if len(x) == 2:
        return dyad_vectorize(lambda x, y: x != y)(*x)
    return all(i == j or a != b for i, a in enumerate(x) for j, b in enumerate(x))

@Function("!==", 2, ...)
def _(*x):
    return all(i == j or a != b for i, a in enumerate(x) for j, b in enumerate(x))

for operator in [">", "<", ">=", "<="]:
    Function(operator, 2, ...)((lambda f: lambda *x: dyad_vectorize(f)(*x) if len(x) == 2 else all(f(a, b) for a, b in zip(x, x[1:])))((lambda o: eval(f"lambda x, y: x {o} y"))(operator)))
    Function("!" + operator, 2, ...)((lambda f: lambda *x: all(f(a, b) for a, b in zip(x, x[1:])))((lambda o: eval(f"lambda x, y: x {o} y"))(operator)))

@Function("~", 1)
def _(x):
    return -1 - x

@Function("!", 1)
def _(x):
    return sympy.Integer(not x)

@Function("clear", 0)
def _():
    print("\033[2J\033[H", end = "")

@Function("strip", 1, 2)
def _(x, v = None):
    if v is None:
        return x.strip()
    else:
        if isinstance(x, list):
            while x and x[0] == v:
                x.pop(0)
            while x and x[-1] == v:
                x.pop()
            return x
        else:
            return x.strip(v)

@Function("sub", 3)
def _(a, b, x):
    x = list(x)
    return [b if k == a else k for k in x]

@Function("sum", 1)
def _(x):
    return sum(x)

@Function("product", 1)
def _(x):
    return fn_registry["*"].f(*x)

@Function(("foldl", "reduce"), 2)
def _(f, x):
    o = x[0]
    for k in x[1:]:
        o = f.f(o, k)
    return o

@Function("foldr", 2)
def _(f, x):
    o = x[-1]
    for k in x[:-1][::-1]:
        o = f.f(k, o)
    return o

@Function("cumfoldl", 2)
def _(f, x):
    o = [x[0]]
    for k in x[1:]:
        o.append(f.f(o[-1], k))
    return o

@Function("cumfoldr", 2)
def _(f, x):
    o = [x[-1]]
    for k in x[:-1][::-1]:
        o.append(f.f(k, o[-1]))
    return o

@Function("reverse", 1)
def _(x):
    return x[::-1]

@Function("cumsum", 1, 2)
def _(x, s = None):
    if s is None:
        x = x[:]
        s = x.pop(0)
    o = [s]
    for k in x:
        o.append(o[-1] + k)
    return o

@Function("index", 2)
def _(needle, haystack):
    if isinstance(haystack, list):
        try:
            return haystack.index(needle) + 1
        except:
            return -1
    else:
        return haystack.find(needle) + 1

@Function(("uniquify", "dedup", "deduplicate"), 1)
def _(x):
    try:
        k = set()
        o = []
        for i in x:
            if i not in k:
                k.add(i)
                o.append(i)
        return o
    except:
        pass
    k = []
    hashes = set()
    for i in x:
        try:
            h = hash(i)
            if h not in hashes:
                k.append(i)
                hashes.add(h)
            elif i not in k:
                k.append(i)
        except:
            if i not in k:
                k.append(i)
    return k

@Function(("len", "size", "length"), 1)
def _(x):
    return len(x)

@Function(("at", "#"), 2)
def _(i, x):
    return x[(i - 1) % len(x)]

@Function("slice", 3)
def _(i, j, x):
    i = (i - 1) % len(x) if i is not None else None
    j = (j - 1) % len(x) if j is not None else None
    if i is None or j is None:
        return x[i:j]
    if i <= j:
        return x[i:j]
    else:
        return x[j:i][::-1]

@Function("slices", 4)
def _(i, j, s, x):
    i = (i - 1) % len(x) if i is not None else None
    j = (j - 1) % len(x) if j is not None else None
    if i is None or j is None:
        return x[i:j:s]
    if i <= j:
        return x[i:j:s]
    else:
        return x[j:i:s][::-1]

@Function(("at=", "#="), 3)
def _(i, j, x):
    x[(i - 1) % len(x)] = j
    return j

@Function(("l", "list"), 0, ...)
def _(*x):
    return list(x)

@Function("listify", 1)
def _(x):
    return list(x)

@Function("splat", 2)
def _(f, x):
    return f.f(*x)

@Function("map", 2)
def _(f, x):
    return [f.f(a) for a in x]

@Function("any", 2)
def _(f, x):
    return any(f.f(a) for a in x)

@Function("all", 2)
def _(f, x):
    return all(f.f(a) for a in x)

@Function("anyall", 2)
def _(f, x):
    return x != [] and all(f.f(a) for a in x)

@Function("mapsplat", 2)
def _(f, x):
    return [f.f(*a) for a in x]

@Function("anysplat", 2)
def _(f, x):
    return any(f.f(*a) for a in x)

@Function("allsplat", 2)
def _(f, x):
    return all(f.f(*a) for a in x)

@Function("anyallsplat", 2)
def _(f, x):
    return x != [] and all(f.f(*a) for a in x)

def deepmap(f, x):
    return [deepmap(f, a) for a in x] if isinstance(x, list) else f(x)
Function("deepmap", 2)(deepmap)

@Function("filter", 2)
def _(f, x):
    return [a for a in x if f.f(a)]

@Function("in", 2)
def _(needle, haystack):
    return needle in haystack

@Function("split", 2)
def _(axe, tree):
    if isinstance(tree, list):
        out = [[]]
        for k in tree:
            if k == axe:
                out.append([])
            else:
                out[-1].append(k)
    else:
        return tree.split(axe)

@Function("nfind", 1, 2)
def _(f, n = 0):
    while not f.f(n):
        n += 1
    return n

@Function("md5", 1)
def _(x):
    return hashlib.md5(bytes(x, "utf-8")).hexdigest()

@Function("lines", 1)
def _(x):
    return x.splitlines()

@Function("sort", 1)
def _(x):
    return sorted(list(x))

@Function("num", 1)
@monad_vectorize
def _(x):
    return sympy.Rational(x)

def bind(f, *x):
    if len(x) > f.max:
        raise RuntimeError("binding too many arguments")
    return Function(None, f.min - len(x), f.max - len(x))(lambda *a: f.f(*x, *a))
Function("bind", 1, ...)(bind)

@Function("hpop", 0, 1)
def _(i = -1):
    history.pop(-1)

@Function("concat", 2, ...)
def _(*x):
    if all(isinstance(k, str) for k in x):
        return "".join(x)
    out = []
    for k in x:
        try:
            out.extend(list(k))
        except:
            out.append(k)
    return out

@Function("sconcat", 2, ...)
def _(*x):
    return "".join(map(str, x))

@Function("tighten", 1)
def _(x):
    try:
        return concat(*x)
    except:
        return x

def flat(x):
    if isinstance(x, list):
        return [k for a in x for k in flat(a)]
    return [x]
Function(("flat", "flatten"), 1)(flat)

@Function(("sflat", "sflatten"), 1)
def _(x):
    return "".join(map(str, flat(x)))

@Function("todir", 1)
def _(x):
    return [{
        ">": sympy.Integer(1),
        "<": sympy.Integer(-1),
        "^": -sympy.I,
        "v": sympy.I
    }[k] for k in x]

@Function(("sublists", "chunks"), 2)
def _(x, a):
    o = []
    while a:
        o.append(a[:x])
        a = a[x:]
    return o

@Function(("osublists", "ochunks"), 2)
def _(x, a):
    o = []
    while len(a) >= x:
        o.append(a[:x])
        a = a[1:]
    return o

@Function(("oloopsublists", "oloopchunks"), 2)
def _(x, a):
    a = a[:]
    o = []
    for _ in range(len(a)):
        o.append(a[:x])
        a.append(a.pop(0))
    return o

@Function("count", 2)
def _(needle, haystack):
    return haystack.count(needle)

@Function("ez", 0)
def _():
    print()
    print("\033[92mEZCLAP\033[0m")
    print()

var_registry = {
    "last": lambda: copy.deepcopy(history[-1]),
    "pi": lambda: sympy.pi,
    "e": lambda: sympy.E,
    "null": lambda: None
}

bt = -1

def adv():
    global bt
    if -bt > len(history):
        bt = -1
    bt -= 1
    return history[bt + 1]

def aeval(values, index, scope = None):
    return evaluate(values[index], scope) if len(values) > index else adv()

def evaluate(tree, scope = None, top = False):
    if scope is None: scope = {}
    if tree[0] == "tree":
        contents = tree[1]
        if len(contents) == 0:
            raise RuntimeError("empty bracket pair in invalid position")
        elif contents[0][0] in ["string", "number"]:
            return contents[0][1]
        elif contents[0][1] == ":=":
            if len(contents) < 2:
                raise RuntimeError("too few arguments to `:=`")
            if len(contents) > 3:
                raise RuntimeError("too many arguments to `:=`")
            if contents[1][0] != "identifier":
                raise RuntimeError("cannot assign (`:=`) to a non-identifier")
            val = evaluate(contents[2], scope) if len(contents) >= 2 else history[-1]
            if contents[1][1] in scope:
                scope[contents[1][1]] = val
            else:
                var_registry[contents[1][1]] = (lambda x: lambda: x)(val)
            return val
        elif contents[0][1] == "defn":
            if len(contents) < 4:
                raise RuntimeError("too few arguments to `defn`")
            if contents[1][0] != "identifier":
                raise RuntimeError("cannot define function with non-identifier name")
            func = evaluate(("tree", [("identifier", "lambda"), *contents[2:]]), scope)
            Function(contents[1][1], func.min, func.max)(func.f)
            print(f"\033[36mfunction `{contents[1][1]}` successfully defined\033[0m")
            return
        elif contents[0][1] == "lambda":
            if len(contents) < 3:
                raise RuntimeError("too few arguments to `lambda`")
            if contents[1][0] != "tree":
                contents[1] = ("tree", [contents[1]])
            arguments = []
            for item in contents[1][1]:
                if item[0] == "identifier":
                    if ("direct", item[1]) in arguments:
                        raise RuntimeError(f"duplicate argument name `{item[1]}`")
                    if item[1] == "...":
                        arguments.append(("varargs",))
                    else:
                        arguments.append(("direct", item[1]))
                elif item[0] == "tree":
                    if len(item[1]) != 2 or item[1][0][0] != "identifier":
                        raise RuntimeError("bracketed argument must consist of an identifier and a value")
                    arguments.append(("default", item[1][0][1], evaluate(item[1][1], scope)))
                else:
                    raise RuntimeError("arguments must be an identifier or (identifier, value)")
            if any(x == ("varargs",) for x in arguments[:-2] + arguments[-1:]):
                raise RuntimeError("... argument can only exist in second last slot")
            if len(arguments) >= 2 and arguments[-2] == ("varargs",):
                max_args = float("inf")
            else:
                max_args = len(arguments)
            min_args = 0
            for x in arguments:
                if x[0] == "varargs":
                    break
                if x[0] == "direct":
                    min_args += 1
            @Function(None, min_args, max_args)
            def f(*x):
                x = list(x)
                extras = len(x) - min_args
                subscope = {**scope}
                variable = False
                for arg in arguments:
                    if arg[0] == "varargs":
                        variable = True
                        continue
                    elif arg[0] == "direct":
                        if variable:
                            subscope[arg[1]] = x
                        else:
                            subscope[arg[1]] = x.pop(0)
                    elif arg[0] == "default":
                        if extras > 0:
                            if variable:
                                subscope[arg[1]] = x
                            else:
                                subscope[arg[1]] = x.pop(0)
                                extras -= 1
                        else:
                            subscope[arg[1]] = arg[2]
                for statement in contents[2:]:
                    value = evaluate(statement, subscope)
                return value
            return f
        elif contents[0][1] == "if":
            if len(contents) > 4:
                raise RuntimeError("too many arguments to `if`")
            return aeval(contents, 2, scope) if aeval(contents, 1, scope) else aeval(contents, 3, scope)
        else:
            val = evaluate(contents[0], scope)
        if val is None:
            raise RuntimeError(f"undefined value `{contents[0][1]}`")
        if not isinstance(val, Function):
            if len(contents) >= 2:
                raise RuntimeError(f"{val} is not a function")
            else:
                return val
        if len(contents) - 1 > val.max:
            raise RuntimeError(f"too many arguments to `{contents[0][1]}`")
        arguments = [evaluate(item, scope) for item in contents[1:]]
        if top:
            while len(arguments) < val.min:
                arguments.append(adv())
        if len(arguments) < val.min:
            return bind(val, *arguments)
        return val.f(*arguments)
    else:
        if tree[0] in ["string", "number"]:
            return tree[1]
        if tree[1] in scope:
            return scope[tree[1]]
        if tree[1] in var_registry:
            return var_registry[tree[1]]()
        if tree[1] in fn_registry:
            return fn_registry[tree[1]]
        raise RuntimeError(f"`{tree[1]}` is not defined")

fd = []

if len(sys.argv) >= 2 and sys.argv[1] != "-":
    with open(sys.argv[1], "r") as f:
        data = f.read()
else:
    if not silence:
        print("\033[36mPlease paste your problem data (send an EOF to end inputting)\033[0m")
    data = ""
    while True:
        try:
            data += input() + "\n"
        except:
            break

history = [data]
hcopy = None

if len(sys.argv) >= 3 and sys.argv[2] != "-":
    with open(sys.argv[2], "r") as f:
        fd = f.read().splitlines()

while True:
    if not silence:
        print(f"\033[36mcmd [{len(history)}]: \033[0m", end = "")
    if fd:
        line = fd.pop(0)
        print(line)
    else:
        lexer = Lexer()
        flag = True
        try:
            line = input()
            if line == "\\mute":
                print("\033[92mdisplay off\033[0m")
                silence = True
            elif line == "\\unmute":
                print("\033[92mdisplay on\033[0m")
                silence = False
            elif line == "\\x":
                if silence:
                    print("\033[92mdisplay on\033[0m")
                    silence = False
                else:
                    print("\033[92mdisplay off\033[0m")
                    silence = True
            elif line == "\\save":
                print("\033[92msaving\033[0m")
                hcopy = copy.deepcopy(history)
            elif line == "\\restore":
                if hcopy is None:
                    print("\033[92mno copy saved\033[0m")
                else:
                    print("\033[92mrestoring\033[0m")
                    history = hcopy[:]
            else:
                flag = False
                while True:
                    for char in line:
                        lexer.feed(char)
                    try:
                        tokens = lexer.clear()
                        break
                    except:
                        lexer.feed("\n")
                        line = input()
        except:
            break
        if not flag:
            tree = parse([("bracket", "("), *tokens, ("bracket", ")")])
            try:
                bt = -1
                value = evaluate(tree, top = True)
                if value is None:
                    if not silence:
                        print(f"\033[93mout [{len(history)}]:\033[0m \033[91mno output; history is unaltered\033[0m")
                    pass
                else:
                    data = value
                    history.append(copy.deepcopy(data))
                    if not silence:
                        print(f"\033[93mout [{len(history) - 1}]:")
                        print(data)
                        print("\033[0m", end = "")
            except:
                if not silence:
                    print(f"\033[91merr [{len(history)}] (history is unaltered):")
                    traceback.print_exc()
                    print("\033[0m", end = "")

if silence:
    print(data)
else:
    print()
