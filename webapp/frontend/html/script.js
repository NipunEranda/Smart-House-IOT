$(document).ready(function() {
    $('#turnOnBtn').on('click', function(e){
        $.ajax({
            url: 'http://192.168.1.161:5000/led/on',
            method: 'GET',
            success: function(result) {
                console.log(result);
         }
        });
        e.preventDefault();
    });
    
    $('#turnOffBtn').on('click', function(e){
        $.ajax({
            url: 'http://192.168.1.161:5000/led/off',
            method: 'GET',
            success: function(result) {
                console.log(result);
         }
        });
        e.preventDefault();
    });
    
    $('#btnToggle').on('click', function(e){
        let status;
        if($(this).text() == 'Turn On') {
            $(this).text('Turn Off')
            $(this).removeClass().addClass('btn btn-block btn-light');
            status = 'on';
        } else {
            $(this).text('Turn On');
            $(this).removeClass().addClass('btn btn-block btn-dark');
            status = 'off';
        }
        
        $.ajax({
            url: 'http://192.168.1.161:5000/led/' + status,
            method: 'GET',
            success: function(result) {
                console.log(result);
         }
        });
        e.preventDefault();
    });
});
