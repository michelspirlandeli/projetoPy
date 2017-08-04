$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-phishing").modal("show");
            },
            success: function (data) {
                $("#modal-phishing .modal-content").html(data.html_form);
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
                    $("#phishing_table tbody").html(data.html_phishing_list);
                    $("#modal-phishing").modal("hide");
                }
                else {
                    $("#modal-phishing .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create phishing
    $(".js-create-phishing").click(loadForm);
    $("#modal-phishing").on("submit", ".js-phishing-create-form", saveForm);

    // Update phishing
    $("#phishing_table").on("click", ".js-update-phishing", loadForm);
    $("#modal-phishing").on("submit", ".js-phishings-update-form", saveForm);

    // Delete phishing
    $("#phishing_table").on("click", ".js-delete-phishing", loadForm);
    $("#modal-phishing").on("submit", ".js-phishing-delete-form", saveForm);

});
