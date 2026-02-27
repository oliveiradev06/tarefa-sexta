import { useState } from "react";
import SignInPage from "./pages/SignInPage";
import SignUpPage from "./pages/SignUpPage";
import ProfilePage from "./pages/ProfilePage";
import { fetchMe, signIn, signOut, signUp } from "./services/authApi";

export default function App() {
 const [page, setPage] = useState("signin");
 const [token, setToken] = useState("");
 const [user, setUser] = useState(null);
 const [message, setMessage] = useState("");
 const [loading, setLoading] = useState(false);

 async function handleSignIn(payload) {
  setLoading(true);
  setMessage("");

  try {
   const data = await signIn(payload);

   setToken(data.token || "");
   setUser(data.user || null);
   setMessage(data.message || "Success");
   setPage("profile");
  } catch (error) {
   setMessage(error.message);
  } finally {
   setLoading(false);
  }
 }

 async function handleSignUp(payload) {
  setLoading(true);
  setMessage("");

  try {
   const data = await signUp(payload);
   setToken(data.token || "");
   setUser(data.user || null);
   setMessage(data.message || "Success");
   setPage("profile");
  } catch (error) {
   setMessage(error.message);
  } finally {
   setLoading(false);
  }
 }

 async function handleMe() {
  setLoading(true);
  setMessage("");

  try {
   const data = await fetchMe(token);
   setUser(data.user || null);
   setMessage("Session is valid");
  } catch (error) {
   setMessage(error.message);
  } finally {
   setLoading(false);
  }
 }

 async function handleLogout() {
  setLoading(true);
  setMessage("");

  try {
   await signOut();
   setUser(null);
   setToken("");
   setMessage("Logged out");
   setPage("signin");
  } catch (error) {
   setMessage(error.message);
  } finally {
   setLoading(false);
  }
 }

 return (
  <main className="min-h-screen bg-slate-100 p-6 text-slate-900">
   {page === "signin" && (
    <SignInPage
     loading={loading}
     onSubmit={handleSignIn}
     onGoToSignUp={() => setPage("signup")}
    />
   )}

   {page === "signup" && (
    <SignUpPage
     loading={loading}
     onSubmit={handleSignUp}
     onGoToSignIn={() => setPage("signin")}
    />
   )}

   {page === "profile" && (
    <ProfilePage
     user={user}
     message={message}
     token={token}
     loading={loading}
     onCheckSession={handleMe}
     onLogout={handleLogout}
    />
   )}
  </main>
 );
}
