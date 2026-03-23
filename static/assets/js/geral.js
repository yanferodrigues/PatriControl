const overlay = document.querySelector(".overlay")
const aside = document.getElementById("aside")

function abrirMenu(btn) {
    overlay.classList.toggle("ativo")
    aside.classList.toggle("ativo")
}

function alterarTema() {
    document.body.classList.toggle("light-mode")
}


