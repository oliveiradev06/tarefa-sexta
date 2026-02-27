class PrismaUserRepository {
 constructor(prisma) {
  this.prisma = prisma;
 }

 async findByEmail(email) {
  return this.prisma.user.findUnique({
   where: { email },
  });
 }

 async findById(id) {
  return this.prisma.user.findUnique({
   where: { id: Number(id) },
  });
 }

 async create({ name, email, passwordHash }) {
  return this.prisma.user.create({
   data: {
    name,
    email,
    passwordHash,
   },
  });
 }
}

module.exports = PrismaUserRepository;
