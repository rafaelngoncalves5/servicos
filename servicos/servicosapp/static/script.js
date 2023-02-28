var excluirBtn = document.getElementById('excluir-btn')
var confirmaDiv = document.getElementById('confirma-div')

function openModal() {
    if (confirmaDiv.style.display == 'none') {
        confirmaDiv.style.display = 'block'
    } else {
        confirmaDiv.style.display = 'none'
    }
}

excluirBtn.addEventListener('click', () => openModal())

