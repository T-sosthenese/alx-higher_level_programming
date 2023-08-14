#!/usr/bin/node

const arrayNums = [];

const lengthNumbers = process.argv.length;
if (lengthNumbers < 4) {
  console.log(0);
} else {
  for (let i = 2; i < lengthNumbers; i++) {
    arrayNums.push(process.argv[i]);
  }
  arrayNums.sort().reverse();
  console.log(arrayNums[1]);
}
