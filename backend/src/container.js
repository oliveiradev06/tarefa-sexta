const prisma = require("./infrastructure/db/prismaClient");
const PrismaUserRepository = require("./infrastructure/repositories/PrismaUserRepository");
const {
 hashPassword,
 comparePassword,
} = require("./infrastructure/security/passwordHasher");
const { signToken } = require("./infrastructure/security/tokenProvider");
const makeRegisterUser = require("./application/use-cases/registerUser");
const makeLoginUser = require("./application/use-cases/loginUser");
const makeGetMe = require("./application/use-cases/getMe");
const makeAuthController = require("./interfaces/http/controllers/authController");

const userRepository = new PrismaUserRepository(prisma);

const registerUser = makeRegisterUser({
 userRepository,
 hashPassword,
 signToken,
});

const loginUser = makeLoginUser({
 userRepository,
 comparePassword,
 signToken,
});

const getMe = makeGetMe({ userRepository });

const authController = makeAuthController({ registerUser, loginUser, getMe });

module.exports = {
 authController,
};
