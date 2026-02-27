import { apiRequest } from "./apiClient";

export function signIn(payload) {
 return apiRequest("/api/auth/login", {
  method: "POST",
  body: JSON.stringify(payload),
 });
}

export function signUp(payload) {
 return apiRequest("/api/auth/register", {
  method: "POST",
  body: JSON.stringify(payload),
 });
}

export function fetchMe(token) {
 const headers = token ? { Authorization: `Bearer ${token}` } : undefined;
 return apiRequest("/api/auth/me", { headers });
}

export function signOut() {
 return apiRequest("/api/auth/logout", { method: "POST" });
}
