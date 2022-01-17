function incrementIntInStr(str, sep) {
    var splitedString = str.split(sep)
    return splitedString[0] + sep + (parseInt(splitedString[1])+1) + sep + splitedString[2]
}

function cloneMore(selector, type) {
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();

    newElement.find('span.step-counter').each(function () {
        var newStepNumber = parseInt(total)+1;
        $(this).text('Step ' + newStepNumber + ':')
    })
    newElement.find('textarea').each(function () {
        $(this).val('')
        oldName = $(this).attr('name')
        $(this).attr('name', incrementIntInStr(oldName, '-'));

        oldId = $(this).attr('id')
        $(this).attr('id', incrementIntInStr(oldId, '-'));
    })
    newElement.find('input').each(function () {
        $(this).val('')
        oldName = $(this).attr('name')
        $(this).attr('name', incrementIntInStr(oldName, '-'));

        oldId = $(this).attr('id')
        $(this).attr('id', incrementIntInStr(oldId, '-'));
    })
    newElement.find('select').each(function () {
        $(this).val('')
        oldName = $(this).attr('name')
        $(this).attr('name', incrementIntInStr(oldName, '-'));

        oldId = $(this).attr('id')
        $(this).attr('id', incrementIntInStr(oldId, '-'));
    })
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
}
