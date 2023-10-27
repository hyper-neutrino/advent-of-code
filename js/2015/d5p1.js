import { readFileSync } from "fs";

console.log(
    readFileSync(process.argv[2], "utf-8")
        .trim()
        .split(/\n/)
        .filter((x) => x.match(/([aeiou].*){3,}/) && !x.match(/ab|cd|pq|xy/) && x.match(/(.)\1/)).length,
);
