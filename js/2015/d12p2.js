import { readFileSync } from "fs";

let x = readFileSync(process.argv[2], "utf-8").trim();

let r = (x) =>
    typeof x === "number"
        ? x
        : typeof x === "object"
        ? (Array.isArray(x) ? x : Object.values(x).includes("red") ? [] : Object.values(x)).map(r).reduce((x, y) => x + y, 0)
        : 0;

console.log(r(JSON.parse(x)));
