const form = document.getElementById("loginForm");
const mensagem = document.getElementById("mensagem");

let tentativas = 0;

form.addEventListener("submit", function(event) {
  event.preventDefault();

  const email = document.getElementById("email").value;
  const senha = document.getElementById("senha").value;

  // Simulação de usuário válido
  const emailCorreto = "admin@gmail.com";
  const senhaCorreta = "12345678";

  if (tentativas >= 5) {
    mensagem.style.color = "red";
    mensagem.textContent = "Conta bloqueada por muitas tentativas.";
    return;
  }

  if (email === emailCorreto && senha === senhaCorreta) {
    mensagem.style.color = "green";
    mensagem.textContent = "Login realizado com sucesso!";
  } else {
    tentativas++;
    mensagem.style.color = "red";
    mensagem.textContent = `Credenciais inválidas. Tentativa ${tentativas}/5`;
  }
});