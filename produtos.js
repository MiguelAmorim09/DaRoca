function busca_dados(){
    fetch ('http://localhost:3000/produtos')
        .then(response => { 
            return response.json();
        })
        .then((dados) => {
            todos(dados)
        })
}

function todos(dados){
    let pagina = ''
    for(let i in dados){
        console.log(dados[i].nome)

        pagina += '<div id="'+dados[i].nome+'"class="categ'+dados[i].categoria+'">'
        pagina += '<img src="imgs\\'+dados[i].imagem+'.png">'
        pagina += '<h1>'+dados[i].nome+'</h1>'
        pagina += '<div class="dados_produtos">'
        pagina += '<div><h1>R$ '+dados[i].valor+'</h1></div>'
        pagina += '<button>+</button>'
        pagina += '<label for="unidade">'
        pagina += '<select id="unidade">'
        pagina += '<option value="quilo">Quilo</option>'
        pagina += '<option value="duzia">Duzia</option>'
        pagina += '<option value="unidade">Unidade</option>'
        pagina += '</select>'
        pagina += '</label>'
        pagina += '</div>'
        pagina += '</div>'
    }

    document.querySelector('#produtos').innerHTML = pagina
}
