import { readFileSync } from "fs";

let grid = new Array(1000).fill(0).map(() => new Array(1000).fill(0));

let x = readFileSync(process.argv[2], "utf-8").trim().split(/\n/);

for (let line of x) {
    let [_, ins, x1, y1, x2, y2] = line.match(/^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$/);
    [x1, x2, y1, y2] = [x1, x2, y1, y2].map((x) => parseInt(x));
    for (let x = x1; x <= x2; x++)
        for (let y = y1; y <= y2; y++) grid[x][y] = ins === "turn on" ? grid[x][y] + 1 : ins === "turn off" ? Math.max(grid[x][y] - 1, 0) : grid[x][y] + 2;
}

console.log(grid.flat().reduce((x, y) => x + y));
