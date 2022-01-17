function boughtIngredient() {
    todoItem = $(this).parent().parent().parent();
    token = $('input[name="csrfmiddlewaretoken"]').val()
    jQuery.ajax({
        type: "PUT",
        url: todoItem.data('action'),
        headers: {
            "X-CSRFToken": token
        },
        data: {
            'id': todoItem.data('element-id'),
        },
        success: function () {
            todoItem.toggleClass('complete')
        }
    })
}

function removeIngredient() {
    todoItem = $(this).parent().parent();
    token = $('input[name="csrfmiddlewaretoken"]').val()
    jQuery.ajax({
        type: "DELETE",
        url: todoItem.data('action'),
        headers: {
            "X-CSRFToken": token
        },
        success: function () {
            todoItem.remove();
        }
    })
}

function addIngredient(ingredientInput) {
    token = $('input[name="csrfmiddlewaretoken"]').val()
    jQuery.ajax({
        type: "POST",
        url: ingredientInput.data('action'),
        headers: {
            "X-CSRFToken": token
        },
        data: {
            'input': ingredientInput.val(),
        },
        success: function (data) {
            window.location.reload();

        }
    })
}

function init(ingredient) {
    $(ingredient).find('input').click(boughtIngredient);
    $(ingredient).find('.remove-todo-item').click(removeIngredient);
}

$( document ).ready(function() {

    "use strict";

    $('.todo-item').each(function (index) {init(this)});

    $(".add-ingredient").keypress(function (e) {
        if ((e.which == 13)&&(!$(this).val().length == 0)) {
            addIngredient($(this));
            $(this).val('');
        }
    });
});
