import { readFileSync } from "fs";

let x = readFileSync(process.argv[2], "utf-8").trim().split(/\n/);

let data = {};

let get = (x) => {
    if (x.match(/\d+/)) return +x;
    if (x in data) return data[x];
    throw 0;
};

while (x.length > 0) {
    let line = x.shift();

    let m;

    try {
        if ((m = line.match(/^(\S+) -> (.+)$/))) {
            data[m[2]] = get(m[1]);
        } else if ((m = line.match(/^(\S+) (AND|OR|[LR]SHIFT) (\S+) -> (.+)$/))) {
            let x = get(m[1]);
            let y = get(m[3]);

            data[m[4]] = { AND: x & y, OR: x | y, RSHIFT: x >> y, LSHIFT: x << y }[m[2]];
        } else if ((m = line.match(/^NOT (\S+) -> (.+)$/))) {
            data[m[2]] = ~get(m[1]);
        } else {
            console.error("!");
        }
    } catch {
        x.push(line);
    }
}

console.log(data.a);
