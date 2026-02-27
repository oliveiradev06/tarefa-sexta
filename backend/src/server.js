require("dotenv").config();
const app = require("./app");
const prisma = require("./infrastructure/db/prismaClient");

const PORT = Number(process.env.PORT || 4000);
const STARTUP_RETRY_DELAY_MS = 3000;

async function start() {
 while (true) {
  try {
   await prisma.$queryRaw`SELECT 1`;
   app.listen(PORT, () => {
    console.log(`API running on http://localhost:${PORT}`);
   });
   break;
  } catch (error) {
   console.error(
    `Failed to connect to DB (${error.message}). Retrying in ${STARTUP_RETRY_DELAY_MS}ms...`,
   );
   await new Promise((resolve) => setTimeout(resolve, STARTUP_RETRY_DELAY_MS));
  }
 }
}

start();
