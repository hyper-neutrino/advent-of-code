import { readFileSync } from "fs";

console.log(
    new Set(
        [...readFileSync(process.argv[2], "utf-8")]
            .map((x) => ({ ">": [0, 1], "<": [0, -1], v: [1, 0], "^": [-1, 0] }[x]))
            .filter((x) => x)
            .reduce((x, y) => [...x, [x.at(-1)[0] + y[0], x.at(-1)[1] + y[1]]], [[0, 0]])
            .map(([x, y]) => `${x}/${y}`),
    ).size,
);
