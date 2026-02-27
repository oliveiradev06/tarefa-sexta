import { useState } from "react";

export default function SignUpPage({ loading, onSubmit, onGoToSignIn }) {
 const [form, setForm] = useState({ name: "", email: "", password: "" });

 function updateField(event) {
  setForm((prev) => ({ ...prev, [event.target.name]: event.target.value }));
 }

 function handleSubmit(event) {
  event.preventDefault();
  onSubmit(form);
 }

 return (
  <div className="mx-auto max-w-md rounded-xl bg-white p-6 shadow">
   <h1 className="text-2xl font-bold">Sign Up</h1>
   <p className="mt-1 text-sm text-slate-600">Crie sua conta</p>

   <form onSubmit={handleSubmit} className="mt-6 space-y-3">
    <input
     name="name"
     value={form.name}
     onChange={updateField}
     placeholder="Name"
     className="w-full rounded border border-slate-300 px-3 py-2"
     required
    />

    <input
     name="email"
     type="email"
     value={form.email}
     onChange={updateField}
     placeholder="Email"
     className="w-full rounded border border-slate-300 px-3 py-2"
     required
    />

    <input
     name="password"
     type="password"
     value={form.password}
     onChange={updateField}
     placeholder="Password"
     className="w-full rounded border border-slate-300 px-3 py-2"
     required
    />

    <button
     type="submit"
     className="w-full rounded bg-slate-900 px-4 py-2 font-semibold text-white disabled:opacity-50"
     disabled={loading}
    >
     {loading ? "Criando..." : "Criar Conta"}
    </button>
   </form>

   <button
    type="button"
    onClick={onGoToSignIn}
    className="mt-4 w-full rounded bg-slate-200 px-4 py-2 font-semibold text-slate-800"
   >
    Ir para Sign In
   </button>
  </div>
 );
}
