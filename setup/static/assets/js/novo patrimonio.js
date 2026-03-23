/* IMAGEM ATIVO */
const input = document.getElementById("inputFoto")
const preview = document.getElementById("preview")
const texto = document.getElementById("textoUpload")

input.addEventListener("change", function(){

    const arquivo = this.files[0]

    if(arquivo){
        const leitor = new FileReader()

        leitor.onload = function(e){
            preview.src = e.target.result
            preview.style.display = "block"
            texto.style.display = "none"
        }

        leitor.readAsDataURL(arquivo)
    }

})

/* NOTA FISCAL */
/* NOTA FISCAL */
const campoNota = document.getElementById("input-nota-ativo");
const inputNota = document.getElementById("input-nota");

let arquivoAtual = null;

// Função reutilizável para aplicar a lógica ao input
function configurarInput(input) {
    input.addEventListener("change", function() {
        const arquivo = this.files[0];
        if (arquivo) {
            arquivoAtual = arquivo;
            campoNota.innerHTML = ''; 

            const nomeArquivo = document.createElement("p");
            nomeArquivo.textContent = arquivo.name;

            Object.assign(nomeArquivo.style, {
                width: "100%",
                wordBreak: "break-all",
                overflowWrap: "anywhere",
                textAlign: "center",
                padding: "10px",
                color: "white"
            });

            campoNota.appendChild(nomeArquivo);
        }
    });
}

// Inicializa o primeiro input
configurarInput(inputNota);

// Botão visualizar
function visualizarNota() {
    if (arquivoAtual) {
        const url = URL.createObjectURL(arquivoAtual);
        window.open(url);
    } else {
        alert("Não existe nota anexada! Anexe uma nota válida!");
    }
}

// Botão excluir
function excluirNota() {
    arquivoAtual = null; // Reseta a variável global
    campoNota.innerHTML = ''; // Limpa o container
    
    // Recria o input
    const inputAddNota = document.createElement("input");
    inputAddNota.id = "input-nota";
    inputAddNota.type = "file";
    inputAddNota.accept = "application/pdf";
    // Opcional: oculte o input se você usa a imagem como gatilho (label)
    
    const imgAddNota = document.createElement("img");
    imgAddNota.src = "assets/icones/adicionar imagem.png";
    imgAddNota.style.cursor = "pointer";

    // MUITO IMPORTANTE: Reatribuir o evento ao novo elemento
    configurarInput(inputAddNota);

    campoNota.appendChild(inputAddNota);
    campoNota.appendChild(imgAddNota);
}