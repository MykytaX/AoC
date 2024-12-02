"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var fs = require("fs");
var lines = fs.readFileSync("2019/2019-1.txt", "utf8").split("\n");
var numbers = lines.map(Number);
// Part One
var sum = 0;
for (var _i = 0, numbers_1 = numbers; _i < numbers_1.length; _i++) {
  var num = numbers_1[_i];
  sum += Math.floor(num / 3) - 2;
}
console.log(sum);
//Part Two
function fuelCalculator(Weight) {
  var fuelReq = Math.floor(Weight / 3) - 2;
  if (fuelReq > 0) {
    var extrafuel = fuelCalculator(fuelReq);
    return fuelReq + extrafuel;
  } else {
    return 0;
  }
}
var fuelsum = 0;
for (var _a = 0, numbers_2 = numbers; _a < numbers_2.length; _a++) {
  var num = numbers_2[_a];
  fuelsum += fuelCalculator(num);
}
console.log(fuelsum);
//# sourceMappingURL=day1.js.map
