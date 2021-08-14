$(document).ready(function () {

    setInterval(function () {
        loadData();
    }, 500);

    function loadData() {
        $.ajax({
            url: 'http://localhost:5000/data/current',
            method: 'GET',
            success: function (result) {
                $('#ldrValue').text(result);
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
        if ($(this).text() == 'Turn On') {
            $(this).text('Turn Off')
            $(this).removeClass().addClass('btn btn-block btn-light');
            status = 'manual';
        } else {
            $(this).text('Turn On');
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

        /*$.ajax({
            url: 'http://localhost:5000/led/' + status,
            method: 'GET',
            success: function (result) {
                console.log(result);
            }
        });*/
        e.preventDefault();
    });
});
