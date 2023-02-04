this.getParcelas()
var bottom = 0;
$(document).ready(function() {
$(".pageBreak").slice(0, $(".pageBreak").length - 1).each(function() {
    bottom -= 100;
    botString = bottom.toString();
    var $counter = $('h3.first').text(' de ' + $(".pageBreak").length).clone().removeClass('first');
    $counter.css("bottom", botString + "%");
        ($counter).insertBefore('.insert');
    });
});