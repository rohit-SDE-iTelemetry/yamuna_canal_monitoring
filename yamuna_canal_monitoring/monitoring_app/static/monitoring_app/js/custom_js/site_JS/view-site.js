// weather check API : ajax call every 2hrs.
function weather_check() {
    let lon;
    let lat;
    let temperature = document.querySelector(".temp");
    let summary = document.querySelector(".summary");
    let loc = document.querySelector(".location");
    const kelvin = 273;
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
            console.log(position);
            lon = position.coords.longitude;
            lat = position.coords.latitude;
            const api = "6d055e39ee237af35ca066f35474e9df";
            const base = `http://api.openweathermap.org/data/2.5/weather?lat=${lat}&` +
                `lon=${lon}&appid=6d055e39ee237af35ca066f35474e9df`;
            fetch(base)
                .then((response) => {
                    return response.json();
                })
                .then((data) => {
                    console.log(data);
                    temperature.textContent =
                        Math.floor(data.main.temp - kelvin) + "°C";
                    $('.farenhite').html(Math.floor(data.main.temp - kelvin) * 9 / 5 + 32);
                    summary.textContent = data.weather[0].description;
                    loc.textContent = data.name + "," + data.sys.country;
                });
        });
    }
}


// site status check API : ajax call every 15minutes.
function site_check() {
    // ---------------  AJAX CALL  ----------------------------
    const url = $(location).attr('pathname').split('/');
    const uuid = url[url.length - 1];
    $.ajax({
        type: 'GET',
        url: "/site-check/" + uuid,
        success: function (response) {
            console.log('response >>>> ',response);
            site_status_append(response);
            reading_marquee(response);
            if('site_data' in localStorage){
                let localStg_response = convert4localstorage(response);
                params_cards(localStg_response);
            }else{
                localStorage.setItem("site_data", JSON.stringify({}));
                let localStg_response = convert4localstorage(response);
                params_cards(localStg_response);
            }
        }
    });
    // --------------------------------------------------------
}


// ============================================================================================
// API + Ajax calls
weather_check();
setTimeout(weather_check, 7200000); // restart at every 2 hours

site_check();
setTimeout(site_check, 900000); // restart at every 15 minutes
// ============================================================================================

// check for site status and update it on UI
function site_status_append(response) {
    if (response['response']['site_status'] == 'Live') {
        let site_status = '<a class="text-white badge badge-success"><b>' + response['response']['site_status'] + '</b></a>';
        $('#site-status-badge').html(site_status);
        return true;
    } else if (response['response']['site_status'] == 'Delay') {
        let site_status = '<a class="text-white badge badge-warning"><b>' + response['response']['site_status'] + '</b></a>';
        $('#site-status-badge').html(site_status);
        return true;
    } else if (response['response']['site_status'] == 'Offline') {
        let site_status = '<a class="text-white badge badge-danger"><b>' + response['response']['site_status'] + '</b></a>';
        $('#site-status-badge').html(site_status);
        return true;
    } else if (response['response']['site_status'] == 'Disabled') {
        let site_status = '<a class="text-white badge badge-info"><b>' + response['response']['site_status'] + '</b></a>';
        $('#site-status-badge').html(site_status);
        return true;
    } else {
        let site_status = '<a class="text-danger"><small><b>' + response['response']['site_status'] + '</b></small></a>';
        $('#site-status-badge').html(site_status);
        return true;
    }
}

// site latest reading marquee
function reading_marquee(response) {
    let reading_marquee_str = '';
    for (var key in response['response']['reading_dict']) {
        if (response['response']['reading_dict'].hasOwnProperty(key) && key != 'timestamp') {
            if (key == 'battery') {
                reading_marquee_str = reading_marquee_str + '<b><a class="badge badge-success">Battery : ' + response['response']['reading_dict'][key] + 'v</a></b>&nbsp;';
            } else if (key == 'waterLevel') {
                reading_marquee_str = reading_marquee_str + '<b><a class="badge badge-success">Water Level : ' + response['response']['reading_dict'][key] + 'm</a></b>&nbsp;';
            } else if (key == 'flowRate') {
                reading_marquee_str = reading_marquee_str + '<b><a class="badge badge-success">Flow Rate : ' + response['response']['reading_dict'][key] + 'm/s</a></b>&nbsp;';
            } else if (key == 'gateOpening') {
                reading_marquee_str = reading_marquee_str + '<b><a class="badge badge-success">Gate Opening : ' + response['response']['reading_dict'][key] + 'mm</a></b>&nbsp;';
            } else if (key == 'velocity') {
                reading_marquee_str = reading_marquee_str + '<b><a class="badge badge-success">Velocity : ' + response['response']['reading_dict'][key] + 'm/s</a></b>&nbsp;';
            } else {
                reading_marquee_str = reading_marquee_str + '<b><a class="badge badge-success">' + key + ' : ' + response['response']['reading_dict'][key] + '</a></b>&nbsp;';
            }
        }
    }
    $('#reading-marquee').html('<marquee class="news-content" scrollamount="4" onmouseover="this.stop();" onmouseout="this.start();">\
                                '+ reading_marquee_str + '\
                                <small style="color: #ffffff">( <strong>last updated at : '+ response['response']['reading_dict']['timestamp'] + '</strong>)</small>\
                                </marquee>');
}

// update site params cards
function params_cards(localStg_response) {
    let param_card_str = '';
    console.log('param card >>>> ',localStg_response);
    for (let key in localStg_response) {
        if (localStg_response.hasOwnProperty(key) && key != 'timestamp') {
            if (key == 'battery') {
                param_card_str = param_card_str + generate_params_cards('Battery', localStg_response[key]['val'], 'v', '20', '<i class="fa-solid fa-battery-full"></i>',localStg_response[key]['tstamp']);
            } else if (key == 'waterLevel') {
                param_card_str = param_card_str + generate_params_cards('Water Level', localStg_response[key]['val'], 'm', '10', '<i class="fa-solid fa-water"></i>',localStg_response[key]['tstamp']);
            } else if (key == 'flowRate') {
                param_card_str = param_card_str + generate_params_cards('Flow Rate', localStg_response[key]['val'], 'm/s', '20', '<i class="fa-solid fa-bars-staggered"></i>',localStg_response[key]['tstamp']);
            } else if (key == 'gateOpening') {
                param_card_str = param_card_str + generate_params_cards('Gate Opening', localStg_response[key]['val'], 'mm', '9', '<i class="fa-solid fa-door-open"></i>',localStg_response[key]['tstamp']);
            } else if (key == 'velocity') {
                param_card_str = param_card_str + generate_params_cards('Velocity', localStg_response[key]['val'], 'm/s', '20', '<i class="fa-solid fa-gauge"></i>',localStg_response[key]['tstamp']);
            }
        }
    }
    $('#params-cards').html(param_card_str);
}


// generate html params cards
function generate_params_cards(param, param_val, param_unit, param_lmt, param_icon, timestamp) {
    return '<div class="col-lg-3 p-1">\
                <div class="col-lg-12" style="box-shadow: 0 0 1rem 0 rgba(0, 0, 0, .2);border-radius:10px;background-color: #36AE7C">\
                    <p><b class="text-white">'+ param + ' ' + param_icon + '</b>\
                        <span class="float-right"><small class="text-white"><b><i class="fa-solid fa-bell"></i> Alert Limit : '+ param_lmt + '' + param_unit + '</b></small></span>\
                    </p>\
                </div>\
                <div class="col-lg-12" style="box-shadow: 0 0 1rem 0 rgba(0, 0, 0, .2);border-radius:10px;background-color: #7FDBDA">\
                    <span style="font-size: 12px;"><b class="text-dark">Current Reading : <span class="badge badge-secondary"><strong>'+ param_val + '' + param_unit + '</strong></span></b></span>\
                    <br>\
                    <span style="font-size: 12px;"><b class="text-dark">Last received at : '+ timestamp + ' </b></span>\
                </div>\
            </div>'
}

// conver site readings to json dict for localstorage
function convert4localstorage(response) {
    let response_readings = response['response']['reading_dict'];
    let localStg_response_setdata = JSON.parse(localStorage.getItem("site_data"));
    for (const [key, value] of Object.entries(response_readings)) {
        if (key != 'timestamp') {
            localStg_response_setdata[key] = {
                'val': response_readings[key],
                'tstamp': response_readings['timestamp']
            }
        }
    }
    for (const [key, value] of Object.entries(localStg_response_setdata)) {
        console.log('key >>> ', key);
        if(key in response_readings){
            if (key != 'timestamp') {
                localStg_response_setdata[key] = {
                    'val': response_readings[key],
                    'tstamp': response_readings['timestamp']
                }
            }
        }
    }
    console.log('localStg_dict >>>> ', localStg_response_setdata);
    localStorage.setItem("site_data", JSON.stringify(localStg_response_setdata));
    return localStg_response_setdata;
}


