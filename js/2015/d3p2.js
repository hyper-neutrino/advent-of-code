import { readFileSync } from "fs";

let dirs = [...readFileSync(process.argv[2], "utf-8")].map((x) => ({ ">": [0, 1], "<": [0, -1], v: [1, 0], "^": [-1, 0] }[x])).filter((x) => x);

let vis = new Set(["0/0"]);

let pos = [
    [0, 0],
    [0, 0],
];

for (let [x, y] of dirs) {
    pos[0][0] += x;
    pos[0][1] += y;
    vis.add(pos[0].join("/"));
    pos.reverse();
}

console.log(vis.size);
