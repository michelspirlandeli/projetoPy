$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-mobile").modal("show");
            },
            success: function (data) {
                $("#modal-mobile .modal-content").html(data.html_form);
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
                    $("#mobile_table tbody").html(data.html_mobile_list);
                    $("#modal-mobile").modal("hide");
                }
                else {
                    $("#modal-mobile .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create midia
    $(".js-create-mobile").click(loadForm);
    $("#modal-mobile").on("submit", ".js-mobile-create-form", saveForm);

    // Update midia
    $("#mobile_table").on("click", ".js-update-mobile", loadForm);
    $("#modal-mobile").on("submit", ".js-mobile-update-form", saveForm);

    // Delete midia
    $("#mobile_table").on("click", ".js-delete-mobile", loadForm);
    $("#modal-mobile").on("submit", ".js-mobile-delete-form", saveForm);

});
