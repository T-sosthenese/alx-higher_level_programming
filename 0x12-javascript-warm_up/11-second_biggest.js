#!/usr/bin/node

const arrayNums = [];

const lengthNumbers = process.argv.length;
if (lengthNumbers === 2 || lengthNumbers === 3) {
  console.log(0);
} else {
  for (let i = 2; i < lengthNumbers; i++) {
    arrayNums.push(process.argv[i]);
  }
  arrayNums.sort().reverse();
  console.log(arrayNums[1]);
}
