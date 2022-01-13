function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();

    newElement.find('span.step-counter').each(function () {
        var newStepNumber = parseInt(total)+1;
        var newText = $(this).text('Step ' + newStepNumber + ':')
    })
    newElement.find('div.ingredient-adding').each(function () {
        var newText = $(this)
    })
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}
