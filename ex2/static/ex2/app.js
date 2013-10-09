$(function() {
    $("#sort_button").click(function() {
        $(this).prop('disabled', true);
        $("#id_input").prop('disabled', true);

        $.ajax({
            type: "POST",
            url: "/ex2/sort/",
            data: {
                input: $("#id_input").val()
            },
            success: function(data) {
                $("#id_output").val(data.result.join(", "));
            },
            complete: function() {
                $("#sort_button").prop('disabled', false);
                $("#id_input").prop('disabled', false);
            }
        });

    });
});
