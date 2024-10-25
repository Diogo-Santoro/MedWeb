// scripts.js

// Função para mostrar uma mensagem de alerta ao clicar em um botão
function showAlert() {
    alert("Button clicked!");
}

// Adicione eventos para botões ou outros elementos conforme necessário
document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('alertButton');
    if (button) {
        button.addEventListener('click', showAlert);
    }
});

// Adicione mais funções e interações conforme necessário
