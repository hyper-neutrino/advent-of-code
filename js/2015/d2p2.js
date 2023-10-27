import { readFileSync } from "fs";

console.log(
    readFileSync(process.argv[2], "utf-8")
        .trim()
        .split(/\n/)
        .map((line) => line.split(/x/).map((x) => parseInt(x)))
        .map(([x, y, z]) => 2 * Math.min(x + y, y + z, z + x) + x * y * z)
        .reduce((x, y) => x + y),
);
