function submit_user_data(){
    

    // validate form fields
    name_validator('#name','#valid-name');
    email_validator('#email','#valid-email');
    contact_validator('#contact','#valid-contact');

    let fullname = $('#name').val();
    let email = $('#email').val();
    let contact = $('#contact').val();
    let userType = $('#user-type').val();
    if (userType.trim().length == 0) {
        $('#user-type').css("border", "2px solid red");
        $('#valid-user-type').css("display", "");
        return false;
    } else{
        $('#user-type').css("border", "");
        $('#valid-user-type').css("display", "none");
    }

    let demoUser = $("input[name='demo-user']").val();
    let permissions = [];
    $('input.permissions:checkbox:checked').each(function () {
        permissions.push($(this).val());
    });
    if (permissions.length < 3) {
        $('#valid-permissions').css("display", "");
        return false;
    } else {
        $('#valid-permissions').css("display", "none");
    }
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

    var formdata = new FormData();
    formdata.append("fullname", fullname);
    formdata.append("email", email);
    formdata.append("contact", contact);
    formdata.append("userType", userType);
    formdata.append("demoUser", demoUser);
    formdata.append("permissions[]", permissions);
    formdata.append("pincode", pincode);
    formdata.append("city", city);
    formdata.append("state", state);
    formdata.append("country", country);
    formdata.append("address", address);


    // ===================================================================================
    // ===================================================================================
    Swal.fire({
        position: 'center',
        title: "<b style='font-size:20px;font-weight:900;color:#1eb6e9;'><i class='fa-solid fa-user-plus'></i> Adding New User</b>\
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
        url: "/user-management/add-user",
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
                    title: '<small>New user added successfully</small>',
                    showConfirmButton: false,
                    timer: 1500
                }).then(function(){
                    window.location.href = '/user-management/users';
                })

            }
            // else if(response['response'] == 'User With this Employee ID Already Exist!'){
            //     $('#emp-id').css('border','2px solid red');
            //     // alert('User With this Employee ID Already Exist!');
            //     Swal.fire({
            //         position: 'center',
            //         icon: 'error',
            //         title: '<small>User With this Employee ID Already Exist!</small>',
            //         showConfirmButton: false,
            //         timer: 2000
            //     })
            //     return false;
            // }else if(response['response'] == 'User With this Email Already Exist!'){
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
                alert('An Error occured while storing Employee Info. Please try again!');
                return false;
            }
        }
    });
    // --------------------------------------------------------

}
