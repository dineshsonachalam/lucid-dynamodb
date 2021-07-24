const express = require("express");
const path = require("path");
const app = express();

app.use(express.static(path.join(__dirname, "LucidDynamodb")));

app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname, "LucidDynamodb", "index.html"));
});

app.get("/*", function(req, res) {
  res.sendFile(path.join(__dirname, "LucidDynamodb", "index.html"), function(err) {
    if (err) {
      res.status(500).send(err);
    }
  });
});

app.listen(3000);