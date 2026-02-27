const express = require("express");
const cors = require("cors");
const cookieParser = require("cookie-parser");
const authRoutes = require("./routes/authRoutes");
const errorHandler = require("./interfaces/http/middleware/errorHandler");

const app = express();

app.use(
 cors({
  origin: process.env.CORS_ORIGIN,
  credentials: true,
 }),
);
app.use(express.json());
app.use(cookieParser());

app.get("/api/health", (_req, res) => {
 res.json({ status: "ok" });
});

app.use("/api/auth", authRoutes);

app.use(errorHandler);

module.exports = app;
