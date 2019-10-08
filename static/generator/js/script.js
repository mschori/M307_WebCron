$(document).ready(function () {
    $("#authenticationToggle").prop("checked", false);
    $("#minutely").prop("checked", true);
    $("#alert_failed").prop("checked", false);
    $("#alert_success_after_failed").prop("checked", false);
    $("#alert_too_much_fails").prop("checked", false);

    handleInputExecution();
});

function toggleAuthentication() {
    if ($("#authenticationToggle").checked) {
        $("#authentication").toggle();
    } else {
        $("#authentication").toggle();
    }
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
}

function scrollToTop() {
    $("html, body").animate({scrollTop: 0}, "slow");
}

function submit_check() {
    let url = $("#url").val();
    let regexUrl = /^http[s]?:\/\/[\S]+[.][\S]+$/;
    let regexCronJob = /^[\S]+[\s][\S0-9]+[\s][\S0-9]+[\s][\S0-9]+[\s][\S0-9]+$/

    if (!$("#title").val()) {
        show_alert_danger('Bitte einen Titel eingeben!');
        $("#title").removeClass('is-valid').addClass('is-invalid');
        scrollToTop();
        return;
    } else {
        $("#title").removeClass('is-invalid').addClass('is-valid');
    }

    if (regexUrl.test(url) === false) {
        show_alert_danger('Die eingegebene URL ist nicht gültig!');
        $("#url").removeClass('is-valid').addClass('is-invalid');
        scrollToTop();
        return;
    } else {
        $("#url").removeClass('is-invalid').addClass('is-valid');
    }
    if ($('#custom').is(':checked')) {
        let customInput = $("#custom_input").val();
        if (regexCronJob.test(customInput) === false) {
            show_alert_danger('Die eingegebene CronTab-Norm ist nicht gültig!')
            $("#custom_input").removeClass('is-valid').addClass('is-invalid');
            scrollToTop();
            return;
        }
    }

    $("#form_cronJob").submit();
}