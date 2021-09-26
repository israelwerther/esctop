function calcularEmprestimo(){
    let valor_emprestado = parseFloat($('#id_valor_emprestado').val())
    console.log("🚀 ~ file: testesjs.js ~ line 3 ~ calcularEmprestimo ~ valor_emprestado", valor_emprestado)


}

function atualizaRelogio() {
    var momentoAtual = new Date();
    
    var vhora = momentoAtual.getHours();
    var vminuto = momentoAtual.getMinutes();
    var vsegundo = momentoAtual.getSeconds();
    
    var vdia = momentoAtual.getDate();
    var vmes = momentoAtual.getMonth() + 1;
    var vano = momentoAtual.getFullYear();
    
    if (vdia < 10) { vdia = "0" + vdia; }
    if (vmes < 10) { vmes = "0" + vmes; }
    if (vhora < 10) { vhora = "0" + vhora; }
    if (vminuto < 10) { vminuto = "0" + vminuto; }
    if (vsegundo < 10) { vsegundo = "0" + vsegundo; }
    
    dataFormat = vdia + " / " + vmes + " / " + vano;
    horaFormat = vhora + " : " + vminuto + " : " + vsegundo;
    
    document.getElementById("data").innerHTML = dataFormat;
    document.getElementById("hora").innerHTML = horaFormat;
    
    setTimeout("atualizaRelogio()", 1000);
}

function sequencial(){
    var dt = new Date()      
    // var ano = String(dt.getYear())
    var ano       = document.getElementById("dataselecionada").value.split("-")[0];
    ano = String(ano)
    // RETORNA APENAS OS DOIS ULTIMOS DIGITOS DO ANO
    ano = (ano.substr(2, 3))
    var mes       = document.getElementById("dataselecionada").value.split("-")[1];
    var dia       = document.getElementById("dataselecionada").value.split("-")[2];   
    var hora      = String(dt.getHours())
    var minutos   = String(dt.getMinutes())        
    var sequencia = ano
    var sequencia = sequencia+mes       
    var sequencia = sequencia+dia    

    if(hora<10){
        sequencia += '0'
    } 
    var sequencia = sequencia+hora  

    if(minutos<10 && minutos>0){
        sequencia += '0'
    }
    var sequencia = sequencia+minutos  

    document.getElementById('n_contrato').value = sequencia
   
}