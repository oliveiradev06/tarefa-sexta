const AppError = require("../../domain/errors/AppError");
const { toPublicUser } = require("../../domain/entities/userEntity");

function makeGetMe({ userRepository }) {
 return async function getMe(userId) {
  const user = await userRepository.findById(userId);

  if (!user) {
   throw new AppError("user not found", 404);
  }

  return { user: toPublicUser(user) };
 };
}

module.exports = makeGetMe;
