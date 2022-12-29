function get_report_type(thisTxt){
    $('#choice-div').addClass('d-none');
    $('.analysis-div').addClass('d-none');
    if($(thisTxt).val().trim() == 'avgerage'){
        $('#category-report').addClass('d-none');
        $('#frequency-report').addClass('d-none');
        $('#comparision-report').addClass('d-none');
        $('#avg-report').removeClass('d-none');
    }else if($(thisTxt).val().trim() == 'category'){
        $('#avg-report').addClass('d-none');
        $('#frequency-report').addClass('d-none');
        $('#comparision-report').addClass('d-none');
        $('#category-report').removeClass('d-none');
    }else if($(thisTxt).val().trim() == 'frequency'){
        $('#avg-report').addClass('d-none');
        $('#category-report').addClass('d-none');
        $('#comparision-report').addClass('d-none');
        $('#frequency-report').removeClass('d-none');
    }else if($(thisTxt).val().trim() == 'comparision'){
        $('#avg-report').addClass('d-none');
        $('#category-report').addClass('d-none');
        $('#frequency-report').addClass('d-none');
        $('#comparision-report').removeClass('d-none');
    }
}




function fetch_report(){
    $('.analysis-div').removeClass('d-none');
}


function update_report_table(thisTxt){
    var ele = $(thisTxt).attr('id');
    if ($(thisTxt).not(':checked').length) {
        $('.'+ele).hide();
    }else{
        $('.'+ele).show();
    }
}


function generate_report(){
    $('#generate-report-btn').addClass('d-none');
    $('#spn1').removeClass('d-none');

    let station_uuid = $('#station-uuid').val().trim();
    let from_dt = $('#from-dt').val().trim();
    let to_dt = $('#to-dt').val().trim();

    if(station_uuid == '' || station_uuid.length <= 0){
        alert('select station!');
        $('#generate-report-btn').removeClass('d-none');
        $('#spn1').addClass('d-none');
        return false;
    }
    if(from_dt == '' || from_dt.length <= 0){
        alert('select from date!');
        $('#generate-report-btn').removeClass('d-none');
        $('#spn1').addClass('d-none');
        return false;
    }
    if(to_dt == '' || to_dt.length <= 0){
        alert('select to date!');
        $('#generate-report-btn').removeClass('d-none');
        $('#spn1').addClass('d-none');
        return false;
    }

    // ajax call ------ this is for calling reports
    $.ajax({
        type: 'GET',
        url: "/report-filter",
        data: {
            'station_uuid' : station_uuid.trim(),
            'from_dt' : from_dt.trim(),
            'to_dt' : to_dt.trim()
        },
        success: function (response) {
            console.log(response['data_record']);
            let table_str = '';
            for (let reading = 0; reading < response['data_record'].length; reading++) {
                const element = response['data_record'][reading];
                table_str = table_str + '<tr>\
                                            <td><strong>'+element['timestamp']+'</strong></td>\
                                            <td class="bat-param">'+element['Battery']+'</td>\
                                            <td class="wl-param">'+element['Waterlevel']+'</td>\
                                            <td class="fr-param">'+element['Flowrate']+'4</td>\
                                            <td class="go-param">'+element['Gateopening']+'</td>\
                                            <td class="velocity-param">'+element['Velocity']+'</td>\
                                        </tr>';
            }
            $('#append2body').html(table_str);
            $('#generate-report-btn').removeClass('d-none');
            $('#spn1').addClass('d-none');

            $('#home').removeClass('d-none');
            $('#params-checker').removeClass('d-none');
            $('#report-data-div').removeClass('d-none');

            // $('table').DataTable({
            //     "destroy": true,
            // });

        }
    });


}