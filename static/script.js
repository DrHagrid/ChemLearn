$(document).ready(function () {
    var form = $('#check-answer');

    function next(reaction_id){
        document.location.href='/reaction/' + reaction_id;
    };

    function check(reaction_id, answer){
        var data = {};
        data.reaction_id = reaction_id;
        data.answer = answer;
        var csrf_token = $('#check-answer [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");
        console.log(data);
        $.ajax({
            url:url,
            type:'POST',
            data:data,
            cache:true,
            success: function(data){
                $('.alert-box').html("");
                if (data.response){
                    $('.alert-box').append('<div class="alert alert-success" role="alert">Верно! Откуда ты это знаешь, жук?</div>');
                    $('.answer-box').html("");
                    $('.answer-box').append(data.products_trans);
                    $('.button-box').html("");
                    $('.button-box').append('<button class="btn btn-success ans-btn" id="submit_btn" data-action="next" data-reaction_id="' + data.next_reaction_id +'">Продолжить</button>');
                }
                else {
                    $('.alert-box').append('<div class="alert alert-danger" role="alert">Ну ты и простофиля! Попробуй ещё...</div>');
                }
            },
            error: function(){
                console.log("ERROR");
            }
        });
    };

    form.on('submit', function (e) {
        e.preventDefault();
        var answer = $('#answer').val();
        var submit_btn = $('#submit_btn');
        var reaction_id = submit_btn.data("reaction_id");
        var action = submit_btn.data("action");
        if (action == 'submit') {
            check(reaction_id, answer);
        }
        if (action == 'next') {
            next(reaction_id);
        }
    })
});
