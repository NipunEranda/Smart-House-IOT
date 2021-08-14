$(document).ready(function () {

    $('#btnToggle').text('Auto');
    $('#readingsLDR').show();
    $('#manualControls').hide();

    setInterval(function () {
        if ($(btnToggle).text() == 'Auto') {
            $('#manualControls').hide();
            $('#readingsLDR').show();
            loadData();
        } else {
            $('#manualControls').show();
            $('#readingsLDR').hide();
        }
    }, 500);

    function loadData() {
        $.ajax({
            url: 'http://localhost:5000/data/current',
            method: 'GET',
            success: function (result) {
                $('#ldrValue').text(result.split(",")[0]);
                $('#ldrDecision').text(result.split(",")[1]);
                console.log(result);
            }
        });
    }

    $('#turnOnBtn').on('click', function (e) {
        $.ajax({
            url: 'http://localhost:5000/led/on',
            method: 'GET',
            success: function (result) {
                console.log(result);
            }
        });
        e.preventDefault();
    });

    $('#turnOffBtn').on('click', function (e) {
        $.ajax({
            url: 'http://localhost:5000/led/off',
            method: 'GET',
            success: function (result) {
                console.log(result);
            }
        });
        e.preventDefault();
    });

    $('#btnToggle').on('click', function (e) {
        let status;
        if ($(this).text() == 'Auto') {
            $(this).text('Manual')
            $(this).removeClass().addClass('btn btn-block btn-light');
            status = 'manual';
        } else {
            $(this).text('Auto');
            $(this).removeClass().addClass('btn btn-block btn-dark');
            status = 'auto';
        }

        $.ajax({
            url: 'http://localhost:5000/mod/' + status,
            method: 'GET',
            success: function (result) {
                console.log(result);
            }
        });
        e.preventDefault();
    });
});
