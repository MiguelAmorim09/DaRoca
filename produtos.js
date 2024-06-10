function busca_dados(funcao){
    fetch ('http://localhost:3000/produtos')
        .then(response => { 
            return response.json();
        })
        .then((dados) => {
            if(funcao === 0){
                todos(dados)
            }
            else if(funcao === 1){
                mostrar_frutas(dados)
            }
            else if(funcao === 2){
                mostrar_vegetais(dados)
            }
            else if(funcao === 3){
                mostrar_legumes(dados)
            }
        })
}

function todos(dados){
    let pagina = ''
    for(let i in dados){
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

function mostrar_frutas(dados){
    let pagina = ''
    for(let i in dados){
        if(dados[i].categoria === 1){
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
    }

    document.querySelector('#produtos').innerHTML = pagina
}

function mostrar_vegetais(dados){
    let pagina = ''
    for(let i in dados){
        if(dados[i].categoria === 2){
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
    }

    document.querySelector('#produtos').innerHTML = pagina
}

function mostrar_legumes(dados){
    let pagina = ''
    for(let i in dados){
        if(dados[i].categoria === 3){
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
    }

    document.querySelector('#produtos').innerHTML = pagina
}