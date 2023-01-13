// console.log("Hello microservices!");

const express = require("express");
const app = express();
const port = 3000;

console.log("Starting up!");

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
