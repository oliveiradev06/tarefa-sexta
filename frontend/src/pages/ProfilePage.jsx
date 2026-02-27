export default function ProfilePage({
 user,
 message,
 token,
 loading,
 onCheckSession,
 onLogout,
}) {
 return (
  <div className="mx-auto max-w-2xl rounded-xl bg-white p-6 shadow">
   <h1 className="text-2xl font-bold">Sessão Autenticada</h1>
   <p className="mt-1 text-sm text-slate-600">Usuário logado com sucesso</p>

   <div className="mt-6 grid gap-3 rounded bg-slate-50 p-4 text-sm">
    <p>
     <strong>Status:</strong> {message || "Ready"}
    </p>
    <p>
     <strong>Token:</strong> {token || "Não informado"}
    </p>
    <p>
     <strong>User:</strong>{" "}
     {user ? JSON.stringify(user) : "No authenticated user"}
    </p>
   </div>

   <div className="mt-6 flex flex-wrap gap-3">
    <button
     type="button"
     onClick={onCheckSession}
     className="rounded bg-blue-600 px-4 py-2 text-sm font-semibold text-white disabled:opacity-50"
     disabled={loading}
    >
     Validar Sessão
    </button>

    <button
     type="button"
     onClick={onLogout}
     className="rounded bg-red-600 px-4 py-2 text-sm font-semibold text-white disabled:opacity-50"
     disabled={loading}
    >
     Logout
    </button>
   </div>
  </div>
 );
}
