function submit_site_data(){
    
    // Station Basic Information
    name_validator('#name','#valid-name');
    email_validator('#email','#valid-email');
    contact_validator('#contact','#valid-contact');
    name_validator('#prefix','#valid-prefix');
    if($('#sec-email').val().trim().length > 0){
        email_validator('#sec-email','#valid-secondary-email');
    }
    if($('#sec-contact').val().trim().length > 0){
        contact_validator('#sec-contact','#valid-secondary-contact');
    }
    let station_name = $('#name').val();
    let email = $('#email').val();
    let contact = $('#contact').val();
    let prefix = $('#prefix').val();
    let sec_email = $('#sec-email').val();
    let sec_contact = $('#sec-contact').val();
    let siteType = $('#site-type').val();
    if (siteType.trim().length == 0) {
        $('#site-type').css("border", "2px solid red");
        $('#valid-site-type').css("display", "");
        return false;
    } else{
        $('#site-type').css("border", "");
        $('#valid-site-type').css("display", "none");
    }
    let demosite = $("input[name='demo-site']").val();

    // Station Address Information
    let pincode = $('#pincode').val();
    if (pincode.trim().length == 0) {
        $('#valid-pincode').css("display", "");
        return false;
    } else {
        $('#valid-pincode').css("display", "none");
    }
    let city = $('#city').val();
    let state = $('#state').val();
    let country = $('#country').val();
    let address = $('#address').val();
    if (address.trim().length == 0) {
        $('#valid-address').css("display", "");
        return false;
    } else {
        $('#valid-address').css("display", "none");
    }
    
    let lattitude = $('#lattitude').val();
    if (lattitude.trim().length == 0) {
        $('#valid-lattitude').css("display", "");
        return false;
    } else {
        $('#valid-lattitude').css("display", "none");
    }
    let longitude = $('#longitude').val();
    if (longitude.trim().length == 0) {
        $('#valid-longitude').css("display", "");
        return false;
    } else {
        $('#valid-longitude').css("display", "none");
    }

    // Station Data Transmission & Alerts Services
    let data2nic = false;
    let nic_alert_email = '';
    if($("#data2nic").prop('checked') == true){
        data2nic = true;
        if($('#nic-email').val().trim().length > 0){
            email_validator('#nic-email','#valid-nic-email');
            nic_alert_email = $('#nic-email').val().trim();
        }
    }
    let data2sdc = false;
    let sdc_alert_email = '';
    if($("#data2sdc").prop('checked') == true){
        data2nic = true;
        if($('#sdc-email').val().trim().length > 0){
            email_validator('#sdc-email','#valid-sdc-email');
            sdc_alert_email = $('#sdc-email').val().trim();
        }
    }
    let data2ce = false;
    let ce_alert_email = '';
    if($("#data2ce").prop('checked') == true){
        data2nic = true;
        if($('#ce-email').val().trim().length > 0){
            email_validator('#ce-email','#valid-ce-email');
            ce_alert_email = $('#ce-email').val().trim();
        }
    }
    let data2wims = false;
    if($("#data2wims").prop('checked') == true){
        data2wims = true;
    }

    // Station Data Encryption Information
    let enc_key = $('#enc-key').val().trim();
    let prv_key = $('#prv-key').val().trim();
    let pub_key = $('#pub-key').val().trim();

    // Station Other Information
    let sinage = false;
    if($("#sinage").prop('checked') == true){
        sinage = true;
    }
    let sms_alert = false;
    if($("#sms-alert").prop('checked') == true){
        sms_alert = true;
    }
    let email_alert = false;
    if($("#email-alert").prop('checked') == true){
        email_alert = true;
    }
    let watsapp_alert = false;
    if($("#watsapp-alert").prop('checked') == true){
        watsapp_alert = true;
    }

    let delay_hr = $('#delay-time').val().trim();
    let offline_hr = $('#offline-time').val().trim();

    // form data
    var formdata = new FormData();
    formdata.append("station_name", station_name);
    formdata.append("email", email);
    formdata.append("site_id", $('#site-id').val().trim());
    formdata.append("version", $('#version').val().trim());
    formdata.append("contact", contact);
    formdata.append("prefix", prefix);
    formdata.append("sec_email", sec_email);
    formdata.append("sec_contact", sec_contact);
    formdata.append("siteType", siteType);
    formdata.append("demosite", demosite);
    
    formdata.append("pincode", pincode);
    formdata.append("city", city);
    formdata.append("state", state);
    formdata.append("country", country);
    formdata.append("address", address);
    formdata.append("lattitude", lattitude);
    formdata.append("longitude", longitude);

    formdata.append("data2nic", data2nic);
    formdata.append("nic_alert_email", nic_alert_email);
    formdata.append("data2sdc", data2sdc);
    formdata.append("sdc_alert_email", sdc_alert_email);
    formdata.append("data2ce", data2ce);
    formdata.append("ce_alert_email", ce_alert_email);
    formdata.append("data2wims", address);

    formdata.append("enc_key", enc_key);
    formdata.append("prv_key", prv_key);
    formdata.append("pub_key", pub_key);

    formdata.append("sinage", sinage);
    formdata.append("sms_alert", sms_alert);
    formdata.append("email_alert", email_alert);
    formdata.append("watsapp_alert", watsapp_alert);
    formdata.append("delay_hr", delay_hr);
    formdata.append("offline_hr", offline_hr);

    // ===================================================================================
    // ===================================================================================
    Swal.fire({
        position: 'center',
        title: "<b style='font-size:20px;font-weight:900;color:#1eb6e9;'><i class='fa-solid fa-user-plus'></i> Adding New Station</b>\
                    <br><br><div class='d-flex justify-content-center'>\
                    <div class='spinner-border text-primary' role='status'>\
                    <span class='sr-only'></span>\
                    </div>\
                </div>",
        showConfirmButton: false,
        onOpen: () => {
            Swal.showLoading();
        }
    })
    // ---------------  AJAX CALL  ----------------------------
    const csrftoken = getCookie('csrftoken');
    $.ajax({
        type: 'POST',
        url: "/add-site",
        headers: { 'X-CSRFToken': csrftoken },
        data: formdata,
        cache : false,
        processData : false,
        contentType : false,
        encType : 'multipart/form-data',
        success: function (response) {
            console.log(response['message']);
            Swal.close();
            // $('#enquiryButton').css('display','');
            // $('#spinnerbtn').css('display','none');
            if(response['message'] == 'success'){
                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: '<small>New station added successfully</small>',
                    showConfirmButton: false,
                    timer: 1500
                }).then(function(){
                    // window.location.href = '/sites';
                })

            }
            else if(response['message'] == 'Site Id already registered with different station'){
                $('#site-id').css('border','2px solid red');
                Swal.fire({
                    position: 'center',
                    icon: 'error',
                    title: '<small>Site Id already registered with different station</small>',
                    showConfirmButton: false,
                    timer: 2000
                })
                return false;
            }
            // else if(response['response'] == 'User With this Email Already Exist!'){
            //     $('#email').css('border','2px solid red');
            //     // alert('User With this Email Already Exist!');
            //     Swal.fire({
            //         position: 'center',
            //         icon: 'error',
            //         title: '<small>User With this Email Already Exist!</small>',
            //         showConfirmButton: false,
            //         timer: 2000
            //     })
            //     return false;
            // }else if(response['response'] == 'User With this Contact Already Exist!'){
            //     $('#contact').css('border','2px solid red');
            //     // alert('User With this Contact Already Exist!');
            //     Swal.fire({
            //         position: 'center',
            //         icon: 'error',
            //         title: '<small>User With this Contact Already Exist!</small>',
            //         showConfirmButton: false,
            //         timer: 1500
            //     })
            //     return false;
            // }
            else{
                // alert('An Error occured while storing Station Info. Please try again!');
                alert(response['message']);
                return false;
            }
        }
    });
    // --------------------------------------------------------

}
