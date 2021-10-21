$(document).ready(function () {
    $('#btnToggle').text('Auto');
    $('#readingsLDR').show();
    $('#autoLightSet').show();
    $('#manualControls').hide();
    $('#manualLightControl').hide();

    $( document ).ready(function() {
    	$.ajax({
            url: 'http://192.168.1.161:5000/led/status',
            method: 'GET',
            success: function (result) {
                if(result != null){
		    Object.keys(result).forEach(function(key){
			if(result[key] == "on"){
			    $(('#manualTurnOnBtn' + key.charAt(key.length - 1))).removeClass('btn-info');
                    	    $(('#manualTurnOnBtn' + key.charAt(key.length - 1))).addClass('btn-danger');
			}else{
			    $(('#manualTurnOnBtn' + key.charAt(key.length - 1))).removeClass('btn-danger');
                    	    $(('#manualTurnOnBtn' + key.charAt(key.length - 1))).addClass('btn-info');
			}
		    });
		}
            }
        });

	$.ajax({
            url: 'http://192.168.1.161:5000/led/auto/list',
            method: 'GET',
            success: function (result) {
                if(result != null){
                    result.data.forEach(function (item, index) {
                        if(item != null){
                            $(('#autoTurnOnBtn' + item.charAt(item.length - 1))).removeClass('btn-info');
                            $(('#autoTurnOnBtn' + item.charAt(item.length - 1))).addClass('btn-danger');

                        }
                    });
                }
            }
        });

    });

    setInterval(function () {
        if ($(btnToggle).text() == 'Auto') {
            $('#readingsLDR').show();
            loadData();
        } else {
            $('#readingsLDR').hide();
        }
    }, 100);

    function loadData() {
        $.ajax({
            url: 'http://192.168.1.161:5000/data/current',
            method: 'GET',
            success: function (result) {
                $('#ldrValue').text(result.split(",")[0]);
                $('#ldrDecision').text(result.split(",")[1]);
		console.log(result.split(",")[0]);
            }
        });
    }

    function loadBtnStatus(){
	$.ajax({
            url: 'http://192.168.1.161:5000/led/status',
            method: 'GET',
            success: function (result) {
                ledStatus = result;
            }
        });
    }

    //Manual LED activate Buttons

    $('#manualTurnOnBtn1').on('click', function (e) {
        if (document.querySelector('#manualTurnOnBtn1').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/off?id=led1',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn1').removeClass('btn-info');
                    $('#manualTurnOnBtn1').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/on?id=led1',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn1').removeClass('btn-danger');
                    $('#manualTurnOnBtn1').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#manualTurnOnBtn2').on('click', function (e) {
        if (document.querySelector('#manualTurnOnBtn2').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/off?id=led2',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn2').removeClass('btn-info');
                    $('#manualTurnOnBtn2').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/on?id=led2',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn2').removeClass('btn-danger');
                    $('#manualTurnOnBtn2').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#manualTurnOnBtn3').on('click', function (e) {
        if (document.querySelector('#manualTurnOnBtn3').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/off?id=led3',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn3').removeClass('btn-info');
                    $('#manualTurnOnBtn3').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/on?id=led3',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn3').removeClass('btn-danger');
                    $('#manualTurnOnBtn3').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#manualTurnOnBtn4').on('click', function (e) {
        if (document.querySelector('#manualTurnOnBtn4').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/off?id=led4',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn4').removeClass('btn-info');
                    $('#manualTurnOnBtn4').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/on?id=led4',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn4').removeClass('btn-danger');
                    $('#manualTurnOnBtn4').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#manualTurnOnBtn5').on('click', function (e) {
        if (document.querySelector('#manualTurnOnBtn5').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/off?id=led5',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn5').removeClass('btn-info');
                    $('#manualTurnOnBtn5').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/on?id=led5',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn5').removeClass('btn-danger');
                    $('#manualTurnOnBtn5').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#manualTurnOnBtn6').on('click', function (e) {
        if (document.querySelector('#manualTurnOnBtn6').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/off?id=led6',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn6').removeClass('btn-info');
                    $('#manualTurnOnBtn6').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/on?id=led6',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn6').removeClass('btn-danger');
                    $('#manualTurnOnBtn6').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#manualTurnOnBtn7').on('click', function (e) {
        if (document.querySelector('#manualTurnOnBtn7').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/off?id=led7',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn7').removeClass('btn-info');
                    $('#manualTurnOnBtn7').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/on?id=led7',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn7').removeClass('btn-danger');
                    $('#manualTurnOnBtn7').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#manualTurnOnBtn8').on('click', function (e) {
        if (document.querySelector('#manualTurnOnBtn8').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/off?id=led8',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn8').removeClass('btn-info');
                    $('#manualTurnOnBtn8').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/on?id=led8',
                method: 'GET',
                success: function (result) {
                    $('#manualTurnOnBtn8').removeClass('btn-danger');
                    $('#manualTurnOnBtn8').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    //Auto LED activate Buttons

    $('#autoTurnOnBtn1').on('click', function (e) {
        if (document.querySelector('#autoTurnOnBtn1').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led1&status=on',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn1').removeClass('btn-info');
                    $('#autoTurnOnBtn1').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led1&status=off',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn1').removeClass('btn-danger');
                    $('#autoTurnOnBtn1').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#autoTurnOnBtn2').on('click', function (e) {
        if (document.querySelector('#autoTurnOnBtn2').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led2&status=on',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn2').removeClass('btn-info');
                    $('#autoTurnOnBtn2').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led2&status=off',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn2').removeClass('btn-danger');
                    $('#autoTurnOnBtn2').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#autoTurnOnBtn3').on('click', function (e) {
        if (document.querySelector('#autoTurnOnBtn3').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led3&status=on',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn3').removeClass('btn-info');
                    $('#autoTurnOnBtn3').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led3&status=off',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn3').removeClass('btn-danger');
                    $('#autoTurnOnBtn3').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#autoTurnOnBtn4').on('click', function (e) {
        if (document.querySelector('#autoTurnOnBtn4').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led4&status=on',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn4').removeClass('btn-info');
                    $('#autoTurnOnBtn4').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led4&status=off',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn4').removeClass('btn-danger');
                    $('#autoTurnOnBtn4').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#autoTurnOnBtn5').on('click', function (e) {
        if (document.querySelector('#autoTurnOnBtn5').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led5&status=on',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn5').removeClass('btn-info');
                    $('#autoTurnOnBtn5').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led5&status=off',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn5').removeClass('btn-danger');
                    $('#autoTurnOnBtn5').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#autoTurnOnBtn6').on('click', function (e) {
        if (document.querySelector('#autoTurnOnBtn6').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led6&status=on',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn6').removeClass('btn-info');
                    $('#autoTurnOnBtn6').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led6&status=off',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn6').removeClass('btn-danger');
                    $('#autoTurnOnBtn6').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#autoTurnOnBtn7').on('click', function (e) {
        if (document.querySelector('#autoTurnOnBtn7').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led7&status=on',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn7').removeClass('btn-info');
                    $('#autoTurnOnBtn7').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led7&status=off',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn7').removeClass('btn-danger');
                    $('#autoTurnOnBtn7').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#autoTurnOnBtn8').on('click', function (e) {
        if (document.querySelector('#autoTurnOnBtn8').classList.contains('btn-info')) {
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led8&status=on',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn8').removeClass('btn-info');
                    $('#autoTurnOnBtn8').addClass('btn-danger');
                    console.log(result);
                }
            });
        }else{
            $.ajax({
                url: 'http://192.168.1.161:5000/led/auto?id=led8&status=off',
                method: 'GET',
                success: function (result) {
                    $('#autoTurnOnBtn8').removeClass('btn-danger');
                    $('#autoTurnOnBtn8').addClass('btn-info');
                    console.log(result);
                }
            });
        }
        e.preventDefault();
    });

    $('#btnToggle').on('click', function (e) {
        let status;
        if ($(this).text() == 'Auto') {
            $(this).text('Manual')
            $('#autoLightSet').hide();
            $('#manualLightControl').show();
            $(this).removeClass().addClass('btn btn-block btn-light');
            status = 'manual';
        } else {
            $(this).text('Auto');
            $('#autoLightSet').show();
            $('#manualLightControl').hide();
            $(this).removeClass().addClass('btn btn-block btn-dark');
            status = 'auto';
        }

        $.ajax({
            url: 'http://192.168.1.161:5000/mod/' + status,
            method: 'GET',
            success: function (result) {
                console.log(result);
            }
        });
        e.preventDefault();
    });
});

