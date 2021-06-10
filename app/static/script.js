(function (win, doc) {
    'use strict';

    // index.html
    // Confirmação de exclusão do dado
    if(doc.querySelector('.btnDel')) {
        let btnDel = doc.querySelectorAll('.btnDel')
        for (let i = 0; i < btnDel.length; i++) {
            btnDel[i].addEventListener('click', function(event) {
                if (confirm('Deseje realmente excluir este dado?')) {
                    return true
                } else {
                    event.preventDefault()
                }
            })
        }
    }


    // form.html
    //AJAX
    if (doc.querySelector('#form')) {
        let form = doc.querySelector('#form')
        function sendForm(event) {
            event.preventDefault()
            let data = new FormData(form) // recebe todos os dados do form através da API FormData
            let ajax = new XMLHttpRequest()
            let token = doc.querySelectorAll('input')[0].value // pega o token de segurança do form, senão o Django bloqueia a requisição
            ajax.open('POST', form.action)
            ajax.setRequestHeader('X-CSRF-TOKEN', token) // declara o token no header do request
            ajax.onreadystatechange = function() {
                if (ajax.status === 200 && ajax.readyState === 4) {
                    let result = doc.querySelector('#result')
                    result.innerHTML = 'Salvo com sucesso!'
                    result.classList.add('alert') // adiciona dinamicamente as classes do Bootstrap
                    result.classList.add('alert-success')
                }
            }
            ajax.send(data)
            form.reset()
        }
        form.addEventListener('submit', sendForm, false)
    }

})(window, document);