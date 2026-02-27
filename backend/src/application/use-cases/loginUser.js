const AppError = require("../../domain/errors/AppError");

function makeLoginUser({ userRepository, comparePassword, signToken }) {
 return async function loginUser(input) {
  const { email, password } = input;

  if (!email || !password) {
   throw new AppError("email and password are required", 400);
  }

  const normalizedEmail = String(email).trim().toLowerCase();

  const user = await userRepository.findByEmail(normalizedEmail);
  if (!user) {
   throw new AppError("invalid credentials", 401);
  }

  const isPasswordValid = await comparePassword(password, user.passwordHash);
  if (!isPasswordValid) {
   throw new AppError("invalid credentials", 401);
  }

  const publicUser = {
   id: user.id,
   name: user.name,
   email: user.email,
  };

  const token = signToken(publicUser);

  return {
   message: "login successful",
   token,
   user: publicUser,
  };
 };
}

module.exports = makeLoginUser;
