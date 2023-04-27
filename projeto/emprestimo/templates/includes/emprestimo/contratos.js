
inFullMoney(number) {
    return extenso(number, { 
        mode: 'currency',
        number: { decimal: 'informal' }, 
    })
},
inFullNumber(number) {
    return extenso(number, {
        number: { decimal: 'informal' }, 
    })
},
currencyFormat(number) {
    return number.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })
},
getParcelas() {
    let dataDoEmprestimo = Object.assign(moment(this.emprestimo.dataEmprestimo), {}) // Faz um cópia do dia do emprestimo
    let diaVencimentoEmprestimo = dataDoEmprestimo.format("DD") // Pega o dia do vencimento do emprestimo
    let vencimento = dataDoEmprestimo // Variável que salva o vencimento da parcela
    
    // Lógica anterior (Não foi alterada)
    if(this.renegociar) {
        vencimento = dataDoEmprestimo.subtract(1, 'month')
    }

    for (let i = 1 ; i <= this.emprestimo.qtd_parcelas; i++) {
        vencimento = dataDoEmprestimo.add(1, 'month') // Vencimento da parcela com 1 mês a mais
        let isFeb = vencimento.month() == 1 // Verifica se é fevereiro
        let isApr = vencimento.month() == 3 // Verifica se é abril
        let lastDayOfMonth = vencimento.endOf('month').format("DD") // Pega o ultimo dia do mês da parcela
        let previousParcela = this.emprestimo.parcelas.at(-1) ? moment(this.emprestimo.parcelas.at(-1).vencimento) : null // Pega a parcela anterior
        let autoCalculateDates = diaVencimentoEmprestimo > (vencimento.isLeapYear() ? 29 : 28) ? false:true // Variável de controle para calculo automático das datas
        
        // Verifica se é fev ou abril
        if((isFeb || isApr) && !autoCalculateDates) {
            // Verifica se é ano bissexto e se o dia do emprestivo é maior do que 28 para não bissexto e 29 para bissexto 
            if(diaVencimentoEmprestimo > (vencimento.isLeapYear() ? 29 : 28)) {
                // se for Fevereiro aplica a regra de adicionar mais 1 mês e setar o dia 1
                if(isFeb) {
                    vencimento.add(1, 'month').date(1)
                }
                // Se for abril e o dia da parcela anterior for 01 então entra nessa condição
                if(isApr && (previousParcela && previousParcela.date() == 1)) {
                    // Remove um mês do vencimento e seta o ultimo dia do mês para dia do vencimento
                    vencimento.subtract(1, 'month')
                    vencimento.date(diaVencimentoEmprestimo)
                }
                //testando
            }
            // Certifica-se de que vai sempre pegar o ultimo dia do mês caso o dia do 
            // emprestivo seja maior que o dia do vencimento da parcela
            if(vencimento.month() == 3 && vencimento.endOf('month').format("DD") > diaVencimentoEmprestimo) {
                vencimento.date(diaVencimentoEmprestimo)
            }

        } else {
            // Segue o fluxo de adição do ultimo dia do mês ou o dia do vencimento da parcela
            if(lastDayOfMonth > diaVencimentoEmprestimo) {
                vencimento.date(diaVencimentoEmprestimo)
            } else {
                vencimento.date(lastDayOfMonth)
            }
        }
        // Adiciona mais um parcela ao array de parcelas
        this.emprestimo.parcelas.push({						
            vencimento: vencimento.format("YYYY-MM-DD"),
            valor_parcela: this.emprestimo.valor_prestacao
        })
    }
}
