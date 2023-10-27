import { readFileSync } from "fs";

let x = readFileSync(process.argv[2], "utf-8").trim().split(/\n/);

let map = {};

for (let line of x) {
    let [a, _, b, __, c] = line.split(/\s+/);
    (map[a] ??= {})[b] = +c;
    (map[b] ??= {})[a] = +c;
}

function p(x) {
    if (x.length === 0) return [[]];
    let o = [];
    for (let i = 0; i < x.length; i++) for (let a of p([...x.slice(0, i), ...x.slice(i + 1)])) o.push([x[i], ...a]);
    return o;
}

let max = -Infinity;

for (let path of p(Object.keys(map))) {
    let t = 0;
    for (let i = 1; i < path.length; i++) t += map[path[i - 1]][path[i]];
    if (t > max) max = t;
}

console.log(max);
