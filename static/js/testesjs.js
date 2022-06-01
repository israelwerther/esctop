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

//CALCULA AS PARCELAS E TAXAS DO EMPRÉSTIMO
function somar(){
    var tvalor_emprestado  = document.getElementById('valor_emprestado')
    var tqtd_parcelas      = document.getElementById('qtd_parcelas')
    var tprestacao         = document.getElementById('prestacao')
    var mes                = document.getElementById("dataselecionada").value.split("-")[1];
    var valor_emprestado   = Number(tvalor_emprestado.value)
    var qtd_parcelas       = Number(tqtd_parcelas.value)
    var prestacao          = Number(tprestacao.value)
    var mes_num            = Number(mes)
    var iof_diario         = 0.00137
    var iof_adicional      = 0.0038
    var multa_por_atraso   = parseFloat(0.020)
    var valor_devido       = parseFloat(0)
    var juros_moratorio    = parseFloat(0.0066)
    var parcela = 0.0
    var juros = 0.083
    var encargos = 0.0
    var encargos_maior_que_um = 0.0
    var principal = 0.0
    var encargos = new Array(qtd_parcelas).fill(0);
    var principal = new Array(qtd_parcelas).fill(0);
    var iof_fora_contrato = new Array(qtd_parcelas).fill(0);
    var somatorio_encargos_anteriores = 0.0
    var qtd_dias           = 0
    //var primeiro = document.getElementById('dataselecionada')
    var boleto    = document.getElementById("boleto").checked

    //if(primeiro == 1){
    //    primeiro = true
    //}

    //-------------------CALCULA O IOF FORA DO CONTRATO--------------------- 

    //> parcela
    parcela = ((valor_emprestado*(1+juros)**(qtd_parcelas)).toFixed(2)/qtd_parcelas) .toFixed(2)
    

    //> encargos[i]
    encargos[0] = Math.round((valor_emprestado*juros)*100)/100    
    if (qtd_parcelas > 1) {
        for(let i=1; i<qtd_parcelas; i++){
            somatorio_encargos_anteriores += encargos[i-1]
            encargos[i] = Math.round(((valor_emprestado + somatorio_encargos_anteriores) * juros)*100)/100
        }    
    }else {
        encargos[0]
    }

    //> principal[i]
    if (qtd_parcelas > 1) {
    for(let i=0; i<qtd_parcelas; i++){
        principal[i] = Math.floor((parcela - encargos[i])*100)/100
    }
    }else {
        for(let i=0; i<qtd_parcelas; i++){
            principal[i] = Math.floor((parcela - encargos[0])*100)/100
        }
    }

    //> qtd_dias
    iof_fora_contrato_total = 0
    for (let i = 0 ; i < qtd_parcelas; i++){
        if(mes_num == 1 || mes_num == 3 || mes_num == 5 || mes_num == 7 || mes_num == 8 || mes_num == 10 || mes_num == 12){
            qtd_dias += 31
        }
        else if(mes_num == 2){
            qtd_dias += 28
        }
        else{
            qtd_dias +=30
        }
        mes_num+=1
        if(mes_num == 13){
            mes_num = 1
        }

    //> iof_fora_contrato
        iof_fora_contrato[i] = Math.floor(((principal[i]*qtd_dias*iof_diario)/100)*100)/100 + Math.floor((principal[i]*iof_adicional)*100)/100
        
        iof_fora_contrato_total += iof_fora_contrato[i]
    }

    //> IOF_INICIAL
    var iof_inicial = Math.round(iof_fora_contrato_total*100)/100

    //----------------CALCULA O IOF DENTRO DO VALOR DO CONTRATO ---------------->

    //> juros_acerto
    var juros_acerto = valor_emprestado*(juros/30)*((mes_num+1)-(mes_num+1))
    
    //> iof_final
    var iof_final = Math.round((valor_emprestado*iof_inicial)/(valor_emprestado-iof_inicial)*100)/100

    //> valor_contrato
    var valor_contrato = valor_emprestado+juros_acerto+iof_final

    //> valor_total_a_Prazo
    var valor_total_a_Prazo = Math.round((valor_contrato*(1+juros)**qtd_parcelas)*100)/100

    //> parcela_final
    if (boleto == true){        
        var parcela_final = Math.round((valor_total_a_Prazo/qtd_parcelas+10)*100)/100           
    }else {
        var parcela_final = Math.round((valor_total_a_Prazo/qtd_parcelas)*100)/100            
    }
    //console.log("parcela_final", parcela_final)
    document.getElementById('prestacao').value = parcela_final
    
    // CALCULA MULTA POR ATRASO 
    var valor_multa = parseFloat((parcela_final*multa_por_atraso)).toFixed(2)
    document.getElementById('multa').value = valor_multa

    // CALCULA JUROS AO DIA
    var juros_ao_dia = (parcela_final*juros_moratorio).toFixed(2)
    document.getElementById('juros_ao_dia').value = juros_ao_dia
    
    // LANÇA O VALOR MUTUADO
    var valor_mutuado = valor_total_a_Prazo
    document.getElementById('valor_mutuado').value = valor_mutuado

    // LANÇA VALOR DEVIDO 
    valor_devido = valor_total_a_Prazo
    document.getElementById('valor_devido').value = valor_devido        

    // LANÇA TAXA DE JUROS AO MÊS
    var taxa_juros_a_m = juros*100 .toFixed(2)
    document.getElementById('juros_ao_mes').value = taxa_juros_a_m        
    
    // LANÇA TAXA DE JUROS MORATÓRIO 
    var juros_moratorio2 = juros_moratorio*100
    document.getElementById('juros_moratorio').value = juros_moratorio2

    // LANÇA TAXA DE JUROS POR ATRASO
    var multa_por_atraso2 = multa_por_atraso*100
    document.getElementById('multa_por_atraso').value = multa_por_atraso2

    // LANÇA TAXA DE IOF TOTAL 
    document.getElementById('iof_real').value = iof_final
}
//CALCULA AS PARCELAS E TAXAS DO EMPRÉSTIMO

// função para marcar online quando presencial não está marcado
function checkUncheck(){
    if ($('#online').is(':checked') == true) {
        $('#presencial').prop('checked', false);
    }
    if($('#online').is(':checked') == false) {
        $('#presencial').prop('checked', true);
    }
}
// função para marcar online quando presencial não está marcado
