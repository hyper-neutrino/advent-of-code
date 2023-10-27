import { readFileSync } from "fs";

let x = readFileSync(process.argv[2], "utf-8").trim().split(/\n/);

let map = {};

for (let line of x) {
    let m = line.match(/^(\S+).+(gain|lose) (\d+).+?(\S+)\.$/);
    (map[m[1]] ??= {})[m[4]] = +m[3] * { gain: 1, lose: -1 }[m[2]];
}

function p(x) {
    if (x.length === 0) return [[]];
    let o = [];
    for (let i = 0; i < x.length; i++) for (let a of p([...x.slice(0, i), ...x.slice(i + 1)])) o.push([x[i], ...a]);
    return o;
}

let max = -Infinity;

for (let o of p(Object.keys(map))) {
    let t = 0;

    for (let i = 0; i < o.length; i++) {
        let a = o[i];
        let b = o[(i + 1) % o.length];
        t += map[a][b] + map[b][a];
    }

    if (t > max) max = t;
}

console.log(max);
