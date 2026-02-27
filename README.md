# Fullstack Auth (Docker + Clean Architecture)

Projeto separado em:

- `frontend/`: React + TailwindCSS (telas Sign In e Sign Up)
- `backend/`: Node.js + Express + Prisma + MySQL + JWT
- `docker-compose.yml`: sobe banco + backend + frontend

## Subir tudo com Docker

Pré-requisito: Docker + Docker Compose instalados.

```bash
docker compose up --build
```

Serviços:

- Frontend: `http://localhost:8080`
- Backend API: `http://localhost:4000`
- MySQL: `localhost:3307`

As migrações são aplicadas automaticamente com Prisma no boot do backend:

- `prisma migrate deploy`

Para derrubar:

```bash
docker compose down
```

Para derrubar limpando dados do banco:

```bash
docker compose down -v
```

## Rodar sem Docker (opcional)

Backend:

```bash
cd backend
cp .env.example .env
npm install
npm run prisma:generate
npm run prisma:migrate
npm run dev
```

Frontend:

```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```

## Endpoints de autenticação

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`
- `POST /api/auth/logout`

## Estrutura (Uncle Bob / Clean)

No backend, o fluxo foi separado em camadas:

- `domain/`: regras centrais e erros de domínio
- `application/`: casos de uso (`registerUser`, `loginUser`, `getMe`)
- `infrastructure/`: repositório Prisma e providers (JWT/hash)
- `interfaces/`: controllers e middlewares HTTP
- `container.js`: composição de dependências

## Prisma

- Schema: `backend/prisma/schema.prisma`
- Migration inicial: `backend/prisma/migrations/202602270001_init`
