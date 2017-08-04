$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-midia").modal("show");
            },
            success: function (data) {
                $("#modal-midia .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#midia_table tbody").html(data.html_midia_list);
                    $("#modal-midia").modal("hide");
                }
                else {
                    $("#modal-midia .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create midia
    $(".js-create-midia").click(loadForm);
    $("#modal-midia").on("submit", ".js-midia-create-form", saveForm);

    // Update midia
    $("#midia_table").on("click", ".js-update-midia", loadForm);
    $("#modal-midia").on("submit", ".js-midia-update-form", saveForm);

    // Delete midia
    $("#midia_table").on("click", ".js-delete-midia", loadForm);
    $("#modal-midia").on("submit", ".js-midia-delete-form", saveForm);

});
