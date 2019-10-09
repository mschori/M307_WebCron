$(document).ready(function () {
    resetForm();
});

function resetForm() {
    $("#title").val('');
    $("#title").removeClass('is-valid').removeClass('is-invalid');
    $("#url").removeClass('is-valid').removeClass('is-invalid');
    $("#url").val('');
    $("#username").val('');
    $("#password").val('');
    $("#custom_input").val('');
    $("#authenticationToggle").prop("checked", false);
    $("#minutely").prop("checked", true);
    $("#alert_failed").prop("checked", false);
    $("#alert_success_after_failed").prop("checked", false);
    $("#alert_too_much_fails").prop("checked", false);
    $("#save_response").prop("checked", false);

    handleInputExecution();
}

function toggleAuthentication() {
    $("#authentication").toggle();
}

function handleInputExecution() {
    if ($('#minutely').is(':checked')) {
        $('#minutely_minutes').prop('disabled', false);
        $('#daily_hour').prop('disabled', true);
        $('#daily_minutes').prop('disabled', true);
        $('#monthly_day').prop('disabled', true);
        $('#monthly_hour').prop('disabled', true);
        $('#monthly_minutes').prop('disabled', true);
        $('#custom_input').prop('disabled', true);
    }
    if ($('#daily').is(':checked')) {
        $('#minutely_minutes').prop('disabled', true);
        $('#daily_hour').prop('disabled', false);
        $('#daily_minutes').prop('disabled', false);
        $('#monthly_day').prop('disabled', true);
        $('#monthly_hour').prop('disabled', true);
        $('#monthly_minutes').prop('disabled', true);
        $('#custom_input').prop('disabled', true);
    }
    if ($('#monthly').is(':checked')) {
        $('#minutely_minutes').prop('disabled', true);
        $('#daily_hour').prop('disabled', true);
        $('#daily_minutes').prop('disabled', true);
        $('#monthly_day').prop('disabled', false);
        $('#monthly_hour').prop('disabled', false);
        $('#monthly_minutes').prop('disabled', false);
        $('#custom_input').prop('disabled', true);
    }
    if ($('#custom').is(':checked')) {
        $('#minutely_minutes').prop('disabled', true);
        $('#daily_hour').prop('disabled', true);
        $('#daily_minutes').prop('disabled', true);
        $('#monthly_day').prop('disabled', true);
        $('#monthly_hour').prop('disabled', true);
        $('#monthly_minutes').prop('disabled', true);
        $('#custom_input').prop('disabled', false);
    }
}

function show_alert_danger(message) {
    $("#alerts").html(
        '<div class="alert alert-danger alert-dismissable">' +
        '<button type="button" class="close" ' +
        'data-dismiss="alert" aria-hidden="true">' +
        '&times;' +
        '</button>' +
        message +
        '</div>');

    scrollToTop();
    fadeOutAlerts();
}

function show_alert_success(message) {
    $("#alerts").html(
        '<div class="alert alert-success alert-dismissable">' +
        '<button type="button" class="close" ' +
        'data-dismiss="alert" aria-hidden="true">' +
        '&times;' +
        '</button>' +
        message +
        '</div>');

    scrollToTop();
    fadeOutAlerts();
}

function fadeOutAlerts() {
    let alerts = $("#alerts").children();

    $(alerts).each(function() {
        $(this).delay(5000).fadeOut(1000);
    });
}

function scrollToTop() {
    $("html, body").animate({scrollTop: 0}, "slow");
}

function submit_check() {
    let url = $("#url").val();
    let regexUrl = /^http[s]?:\/\/[\S]+[.][\S]+$/;
    let regexCronJob = /^[\S]+[\s][\S0-9]+[\s][\S0-9]+[\s][\S0-9]+[\s][\S0-9]+$/
    let form = document.getElementById('form_cronJob');
    let form_serializer = $("#form_cronJob");

    if (!$("#title").val()) {
        show_alert_danger('Bitte einen Titel eingeben!');
        $("#title").removeClass('is-valid').addClass('is-invalid');
        return;
    } else {
        $("#title").removeClass('is-invalid').addClass('is-valid');
    }

    if (regexUrl.test(url) === false) {
        show_alert_danger('Die eingegebene URL ist nicht gültig!');
        $("#url").removeClass('is-valid').addClass('is-invalid');
        return;
    } else {
        $("#url").removeClass('is-invalid').addClass('is-valid');
    }
    if ($('#custom').is(':checked')) {
        let customInput = $("#custom_input").val();
        if (regexCronJob.test(customInput) === false) {
            show_alert_danger('Die eingegebene CronTab-Norm ist nicht gültig!')
            $("#custom_input").removeClass('is-valid').addClass('is-invalid');
            return;
        }
    }

    if (!form.checkValidity()) {
        scrollToTop();
        return;
    }

    $.ajax({
        url: "process",
        type: "POST",
        data: form_serializer.serialize(),
        success: function (response) {
            show_alert_success('CronJob erfolgreich eingetragen/aktualisiert!')
            resetForm();
        },
        error: function (response) {
            show_alert_danger('Error: CronJob konnte nicht eingetragen/aktualisiert werden!')
        }
    });
}