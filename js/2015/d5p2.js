import { readFileSync } from "fs";

console.log(
    readFileSync(process.argv[2], "utf-8")
        .trim()
        .split(/\n/)
        .filter((x) => x.match(/(.)(.).*\1\2/) && x.match(/(.).\1/)).length,
);
