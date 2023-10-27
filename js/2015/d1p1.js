import { readFileSync } from "fs";

console.log([...readFileSync(process.argv[2], "utf-8")].map((x) => (x === "(" ? 1 : x === ")" ? -1 : 0)).reduce((x, y) => x + y));
