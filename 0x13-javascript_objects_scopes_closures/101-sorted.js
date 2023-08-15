#!/usr/bin/node

const dict = require('./101-data').dict;
const totalList = Object.entries(dict);
const vals = Object.values(dict);
const valsUnique = [...new Set(vals)];
const newDict = {};
for (const j in valsUnique) {
  const list = [];
  for (const k in totalList) {
    if (totalList[k][1] === valsUnique[j]) {
      list.unshift(totalList[k][0]);
    }
  }
  newDict[valsUnique[j]] = list;
}
console.log(newDict);
