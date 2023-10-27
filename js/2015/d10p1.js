import { readFileSync } from "fs";

let x = readFileSync(process.argv[2], "utf-8").trim();

for (let i = 0; i < 40; i++) {
    let o = [];

    for (let ch of x)
        if (o.at(-1)?.[0] === ch) o.at(-1)[1]++;
        else o.push([ch, 1]);

    x = o.map(([x, y]) => y + x).join("");
}

console.log(x.length);
