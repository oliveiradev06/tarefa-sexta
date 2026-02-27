function buildCookieOptions() {
 return {
  httpOnly: true,
  sameSite: "lax",
  secure: process.env.NODE_ENV === "production",
  maxAge: 24 * 60 * 60 * 1000,
 };
}

function makeAuthController({ registerUser, loginUser, getMe }) {
 return {
  async register(req, res, next) {
   try {
    const result = await registerUser(req.body);
    res.cookie("token", result.token, buildCookieOptions());
    return res.status(201).json(result);
   } catch (error) {
    return next(error);
   }
  },

  async login(req, res, next) {
   try {
    const result = await loginUser(req.body);
    res.cookie("token", result.token, buildCookieOptions());
    return res.json(result);
   } catch (error) {
    return next(error);
   }
  },

  async me(req, res, next) {
   try {
    const result = await getMe(req.user.id);
    return res.json(result);
   } catch (error) {
    return next(error);
   }
  },

  logout(_req, res) {
   res.clearCookie("token");
   return res.json({ message: "logout successful" });
  },
 };
}

module.exports = makeAuthController;
