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
const campoNota = document.getElementById("input-nota-ativo");
const inputNota = document.getElementById("input-nota");

let arquivoAtual = null;

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

configurarInput(inputNota);

function visualizarNota() {
    if (arquivoAtual) {
        const url = URL.createObjectURL(arquivoAtual);
        window.open(url);
    } else {
        alert("Não existe nota anexada! Anexe uma nota válida!");
    }
}

function excluirNota() {
    arquivoAtual = null; 
    campoNota.innerHTML = ''; 
    
    const inputAddNota = document.createElement("input");
    inputAddNota.id = "input-nota";
    inputAddNota.type = "file";
    inputAddNota.accept = "application/pdf";
    
    const imgAddNota = document.createElement("img");
    imgAddNota.src = "assets/icones/adicionar imagem.png";
    imgAddNota.style.cursor = "pointer";

    configurarInput(inputAddNota);

    campoNota.appendChild(inputAddNota);
    campoNota.appendChild(imgAddNota);
}