const AppError = require("../../domain/errors/AppError");

function makeRegisterUser({ userRepository, hashPassword, signToken }) {
 return async function registerUser(input) {
  const { name, email, password } = input;

  if (!name || !email || !password) {
   throw new AppError("name, email and password are required", 400);
  }

  if (password.length < 6) {
   throw new AppError("password must be at least 6 characters", 400);
  }

  const normalizedEmail = String(email).trim().toLowerCase();
  const normalizedName = String(name).trim();

  const existingUser = await userRepository.findByEmail(normalizedEmail);
  if (existingUser) {
   throw new AppError("email already in use", 409);
  }

  const passwordHash = await hashPassword(password);
  const user = await userRepository.create({
   name: normalizedName,
   email: normalizedEmail,
   passwordHash,
  });

  const token = signToken({
   id: user.id,
   name: user.name,
   email: user.email,
  });

  return {
   message: "registered successfully",
   token,
   user,
  };
 };
}

module.exports = makeRegisterUser;
