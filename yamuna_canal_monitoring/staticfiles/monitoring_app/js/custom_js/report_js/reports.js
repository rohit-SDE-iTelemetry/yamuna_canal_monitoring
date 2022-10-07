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