import { readFileSync } from "fs";

console.log(
    readFileSync(process.argv[2], "utf-8")
        .trim()
        .split(/\n/)
        .map((x) => x.length - eval(x).length)
        .reduce((x, y) => x + y),
);
