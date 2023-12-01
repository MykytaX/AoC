/**
 * this is how to parse a file into an array of numbers for each line
 */

import { readFileSync } from "fs";

const input = readFileSync("inputs/2019-day1.txt", "utf8").split("\n");
console.log(input);
``