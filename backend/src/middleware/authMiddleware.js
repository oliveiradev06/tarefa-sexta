const { verifyToken } = require("../infrastructure/security/tokenProvider");

function requireAuth(req, res, next) {
 const authHeader = req.headers.authorization;
 const tokenFromHeader = authHeader?.startsWith("Bearer ")
  ? authHeader.split(" ")[1]
  : null;

 const token = tokenFromHeader || req.cookies.token;

 if (!token) {
  return res.status(401).json({ message: "Unauthorized: token missing" });
 }

 try {
  const payload = verifyToken(token);
  req.user = payload;
  return next();
 } catch (error) {
  return res.status(401).json({ message: "Unauthorized: invalid token" });
 }
}

module.exports = { requireAuth };
