// Execute on pageload
$(document).ready(function () {
    resetForm();
});

// Reload page
function reloadPage() {
    location.reload();
}

// Reset whole form
function resetForm(withAlert = false) {
    $("#job_id").val('0');
    $("#title").val('');
    $("#title").removeClass('is-valid').removeClass('is-invalid');
    $("#url").removeClass('is-valid').removeClass('is-invalid');
    $("#url").val('');
    $("#username").val('');
    $("#password").val('');
    $("#custom_input").val('');
    if ($("#authenticationToggle").is(':checked')) {
        $("#authenticationToggle").prop("checked", false);
        $("#authentication").toggle();
    }
    $("#custom").prop("checked", true);
    handleInputExecution('custom');
    $("#alert_failed").prop("checked", false);
    $("#alert_success_after_failed").prop("checked", false);
    $("#alert_too_much_fails").prop("checked", false);
    $("#save_response").prop("checked", false);

    if (withAlert) {
        show_alert_success('Form erfolgreich zurückgesetzt!');
    }
}

// Toggle authentication block
function toggleAuthentication() {
    $("#authentication").toggle();

    if ($("#authenticationToggle").is(':checked')) {
        $("#username").prop('required', true);
        $("#password").prop('required', true);
    } else {
        $("#username").prop('required', false);
        $("#password").prop('required', false);
    }
}

// Check selected radio button .then disable or enable input fields
function handleInputExecution(input_class) {
    $('.radioInputButton').prop('disabled', true);
    $("." + input_class).prop('disabled', false);
}

// show alert message in red
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

// show alert message in green
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

// Fade out alerts
function fadeOutAlerts() {
    let alerts = $("#alerts").children();

    $(alerts).each(function () {
        $(this).delay(5000).fadeOut(1000);
    });
}

// Scroll automaticly to top of page
function scrollToTop() {
    $("html, body").animate({scrollTop: 0}, "slow");
}

// Check all inputs and submit or throw error
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
        show_alert_danger('Prüfe deine Eingaben!');
        return;
    }

    $.ajax({
        url: "process",
        type: "POST",
        data: form_serializer.serialize(),
        success: function (response) {
            if (response !== 'Fail') {
                show_alert_success('CronJob erfolgreich eingetragen/aktualisiert!')
                resetForm();
            } else {
                show_alert_danger('Error: CronJob konnte nicht eingetragen/aktualisiert werden!')
            }
        },
        error: function (response) {
            show_alert_danger('Error: CronJob konnte nicht eingetragen/aktualisiert werden!')
        }
    });
}

// Load selected job
function loadJob() {
    let form_serializer = $("#form_loadjob");

    $.ajax({
        url: "load",
        type: "POST",
        data: form_serializer.serialize(),
        success: function (response) {
            if (response !== 'Fail') {
                let job = response[0]['fields'];
                $("#job_id").val(response[0]['pk']);
                $("#title").val(job['title']);
                $("#url").val(job['url']);
                if (job['auth_enabled']) {
                    $("#authenticationToggle").prop('checked', true);
                    toggleAuthentication();
                    $("#username").val(job['auth_user']);
                    $("#password").val(job['auth_pw']);
                } else {
                    $("#authenticationToggle").prop('checked', false);
                }
                $("#custom").prop('checked', true);
                handleInputExecution('custom');
                let cron_norm = job['execute_interval'];
                $("#custom_input").val(cron_norm);
                if (job['allert_failed']) {
                    $("#alert_failed").prop('checked', true);
                } else {
                    $("#alert_failed").prop('checked', false);
                }
                if (job['allert_success_after_failed']) {
                    $("#alert_success_after_failed").prop('checked', true);
                } else {
                    $("#alert_success_after_failed").prop('checked', false);
                }
                if (job['allert_too_much_fails']) {
                    $("#alert_too_much_fails").prop('checked', true);
                } else {
                    $("#alert_too_much_fails").prop('checked', false);
                }
                if (job['save_response']) {
                    $("#save_response").prop('checked', true);
                } else {
                    $("#save_response").prop('checked', false);
                }
                show_alert_success('Job erfolgreich geladen!')
            } else {
                show_alert_danger('Error: Job konnte nicht geladen werden!')
            }
        },
        error: function (response) {
            show_alert_danger('Error: Job konnte nicht geladen werden!')
        }
    });
}

// execute cronjobs
function executeCronJobs() {
    let form_serializer = $("#execute_cronjobs");

    $.ajax({
        url: "testing",
        type: "POST",
        data: form_serializer.serialize(),
        success: function (response) {
            if (response !== 'Fail') {
                show_alert_success('Alle CronJobs wurden ausgeführt!')
            } else {
                show_alert_danger('Error: CronJobs konnten nicht ausgeführt werden!')
            }
        },
        error: function (response) {
            show_alert_danger('Error: CronJobs konnten nicht ausgeführt werden!')
        }
    });
}