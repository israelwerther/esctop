//Função para primeiro cep da página
function limpa_formulário_cep_1() {
    //Limpa valores do formulário de cep.
    document.getElementById('rua_1').value=("");
    document.getElementById('bairro_1').value=("");
    document.getElementById('cidade_1').value=("");
    document.getElementById('uf_1').value=("");
}

function meu_callback_1(conteudo) {
if (!("erro" in conteudo)) {
    //Atualiza os campos com os valores.
    document.getElementById('rua_1').value=(conteudo.logradouro);
    document.getElementById('bairro_1').value=(conteudo.bairro);
    document.getElementById('cidade_1').value=(conteudo.localidade);
    document.getElementById('uf_1').value=(conteudo.uf);
} //end if.
else {
    //CEP não Encontrado.
    limpa_formulário_cep_1();
    alert("CEP não encontrado.");
}
}

function pesquisacep_1(valor) {
console.log("entrou")

//Nova variável "cep" somente com dígitos.
var cep_1 = valor.replace(/\D/g, '');

//Verifica se campo cep possui valor informado.
if (cep_1 != "") {

    //Expressão regular para validar o CEP.
    var validacep = /^[0-9]{8}$/;

    //Valida o formato do CEP.
    if(validacep.test(cep_1)) {

        //Preenche os campos com "..." enquanto consulta webservice.
        document.getElementById('rua_1').value="...";
        document.getElementById('bairro_1').value="...";
        document.getElementById('cidade_1').value="...";
        document.getElementById('uf_1').value="...";        

        //Cria um elemento javascript.
        var script = document.createElement('script');

        //Sincroniza com o callback.
        script.src = 'https://viacep.com.br/ws/'+ cep_1 + '/json/?callback=meu_callback_1';

        //Insere script no documento e carrega o conteúdo.
        document.body.appendChild(script);

    } //end if.
    else {
        //cep é inválido.
        limpa_formulário_cep_1();
        alert("Formato de CEP inválido.");
    }
} //end if.
else {
    //cep sem valor, limpa formulário.
    limpa_formulário_cep_1();
}
};


//Função para segundo cep da página
function limpa_formulário_cep_2() {
    //Limpa valores do formulário de cep.
    document.getElementById('rua_2').value=("");
    document.getElementById('bairro_2').value=("");
    document.getElementById('cidade_2').value=("");
    document.getElementById('uf_2').value=("");
}

function meu_callback_2(conteudo) {
if (!("erro" in conteudo)) {
    //Atualiza os campos com os valores.
    document.getElementById('rua_2').value=(conteudo.logradouro);
    document.getElementById('bairro_2').value=(conteudo.bairro);
    document.getElementById('cidade_2').value=(conteudo.localidade);
    document.getElementById('uf_2').value=(conteudo.uf);
} //end if.
else {
    //CEP não Encontrado.
    limpa_formulário_cep_2();
    alert("CEP não encontrado.");
}
}

function pesquisacep_2(valor) {
console.log("entrou2")

//Nova variável "cep" somente com dígitos.
var cep_2 = valor.replace(/\D/g, '');

//Verifica se campo cep_2 possui valor informado.
if (cep_2 != "") {

    //Expressão regular para validar o cep_2.
    var validacep = /^[0-9]{8}$/;

    //Valida o formato do CEP.
    if(validacep.test(cep_2)) {

        //Preenche os campos com "..." enquanto consulta webservice.
        document.getElementById('rua_2').value="...";
        document.getElementById('bairro_2').value="...";
        document.getElementById('cidade_2').value="...";
        document.getElementById('uf_2').value="...";        

        //Cria um elemento javascript.
        var script = document.createElement('script');

        //Sincroniza com o callback.
        script.src = 'https://viacep.com.br/ws/'+ cep_2 + '/json/?callback=meu_callback_2';

        //Insere script no documento e carrega o conteúdo.
        document.body.appendChild(script);

    } //end if.
    else {
        //cep é inválido.
        limpa_formulário_cep_2();
        alert("Formato de CEP inválido.");
    }
} //end if.
else {
    //cep sem valor, limpa formulário.
    limpa_formulário_cep_2();
}
};