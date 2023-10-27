import crypto from "crypto";
import { readFileSync } from "fs";

let x = readFileSync(process.argv[2], "utf-8").trim();

for (let i = 1; ; i++) {
    let hash = crypto.createHash("md5");
    hash.update(x + i);

    if (hash.digest().toString("hex").startsWith("00000")) {
        console.log(i);
        break;
    }
}
