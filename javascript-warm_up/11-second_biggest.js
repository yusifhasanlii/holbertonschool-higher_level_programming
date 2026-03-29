#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  const uniqueSorted = args.sort((a, b) => b - a);
  console.log(uniqueSorted[1]);
}
