import { readFileSync } from "fs";

let x = readFileSync(process.argv[2], "utf-8").trim();

let inc = (s) =>
    s.match(/^z+$/)
        ? "a".repeat(s.length + 1)
        : s[s.length - 1] === "z"
        ? inc(s.slice(0, -1)) + "a"
        : s.slice(0, -1) + String.fromCharCode(s.charCodeAt(s.length - 1) + 1);

while (true) {
    let pass = !x.match(/[iol]/) && new Set(x.matchAll(/(.)\1/g)).size > 1;

    if (pass) {
        pass = false;

        for (let i = 2; i < x.length; i++)
            if (x.charCodeAt(i - 2) === x.charCodeAt(i - 1) - 1 && x.charCodeAt(i - 1) === x.charCodeAt(i) - 1) {
                pass = true;
                break;
            }
    }

    if (pass) {
        console.log(x);
        break;
    }

    x = inc(x);
}
