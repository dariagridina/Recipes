$( document ).ready(function() {

    "use strict";

    var todo = function() {
        $('.todo-list .todo-item input').click(function() {
            if($(this).is(':checked')) {
                $(this).parent().parent().parent().toggleClass('complete');
            } else {
                $(this).parent().parent().parent().toggleClass('complete');
            }
        });

        $('.todo-nav .all-task').click(function() {
            $('.todo-nav li.active').removeClass('active');
            $(this).addClass('active');
        });

        $('#uniform-all-complete input').click(function() {
            if($(this).is(':checked')) {
                $('.todo-item .checker span:not(.checked) input').click();
            } else {
                $('.todo-item .checker span.checked input').click();
            }
        });

        $('.remove-todo-item').click(function() {
            $(this).parent().remove();
        });
    };

    todo();

    $(".add-task").keypress(function (e) {
        if ((e.which == 13)&&(!$(this).val().length == 0)) {
            $('<div class="todo-item"><div class="alignment"><a href="javascript:void(0);" class="float-right remove-todo-item"><i class="bi bi-x-lg"></i></a><span>' + $(this).val() + '</span></div><div class="checker"><span class=""><input type="checkbox"></span></div></div>').insertAfter('.todo-list .todo-item:last-child');
            $(this).val('');
        } else if(e.which == 13) {
            alert('Please enter new ingredient');
        }
        $(document).on('.todo-list .todo-item.added input').click(function() {
            if($(this).is(':checked')) {
                $(this).parent().parent().parent().toggleClass('complete');
            } else {
                $(this).parent().parent().parent().toggleClass('complete');
            }
        });
        $('.todo-list .todo-item.added .remove-todo-item').click(function() {
            $(this).parent().remove();
        });
    });
});
