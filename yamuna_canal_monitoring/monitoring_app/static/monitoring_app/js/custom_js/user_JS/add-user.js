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
    formdata.append("permissions[]", JSON.stringify(permissions));
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
            console.log(response['response']);
            Swal.close();
            // $('#enquiryButton').css('display','');
            // $('#spinnerbtn').css('display','none');
            if(response['response'] == 'success'){

                // alert('New Employee Added successfully');
                // location.reload();
                // $('#exampleModalCenter').modal('hide');
                Swal.fire({
                    position: 'center',
                    icon: 'success',
                    title: '<small>New employee added successfully</small>',
                    showConfirmButton: false,
                    timer: 1500
                }).then(function(){
                    window.location.reload();
                })

            }else if(response['response'] == 'User With this Employee ID Already Exist!'){
                $('#emp-id').css('border','2px solid red');
                // alert('User With this Employee ID Already Exist!');
                Swal.fire({
                    position: 'center',
                    icon: 'error',
                    title: '<small>User With this Employee ID Already Exist!</small>',
                    showConfirmButton: false,
                    timer: 2000
                })
                return false;
            }else if(response['response'] == 'User With this Email Already Exist!'){
                $('#email').css('border','2px solid red');
                // alert('User With this Email Already Exist!');
                Swal.fire({
                    position: 'center',
                    icon: 'error',
                    title: '<small>User With this Email Already Exist!</small>',
                    showConfirmButton: false,
                    timer: 2000
                })
                return false;
            }else if(response['response'] == 'User With this Contact Already Exist!'){
                $('#contact').css('border','2px solid red');
                // alert('User With this Contact Already Exist!');
                Swal.fire({
                    position: 'center',
                    icon: 'error',
                    title: '<small>User With this Contact Already Exist!</small>',
                    showConfirmButton: false,
                    timer: 1500
                })
                return false;
            }else{
                alert('An Error occured while storing Employee Info. Please try again!');
                return false;
            }
        }
    });
    // --------------------------------------------------------

}

    // console.log('fullname >>> ',fullname);
    // console.log('email >>> ',email);
    // console.log('contact >>> ',contact);
    // console.log('contact >>> ',contact);
    // console.log('userType >>> ',userType);
    // console.log('demoUser >>> ',demoUser);
    // console.log('permissions >>> ',permissions);
    // console.log('pincode >>> ',pincode);
    // console.log('city >>> ',city);
    // console.log('state >>> ',state);
    // console.log('country >>> ',country);
    // console.log('address >>> ',address);

    // if(empID.trim().length == 0){
    //     alert('Enter Employee ID');
    //     return false;
    // }

   
    // if(contact.trim().length < 10){
    //     alert('Enter valid 10 digit contact number');
    //     return false;
    // }
    // // if(alternateContact.trim().length > 0 && alternateContact.trim().length < 10){
    // //     alert('Enter valid 10 digit alternate contact number');
    // //     return false;
    // // }
    // if(DOB.trim().length == 0){
    //     alert('Enter valid DOB');
    //     return false;
    // }
    // // if(fathersName.trim().length == 0){
    // //     alert('Enter valid Fathers Name');
    // //     return false;
    // // }
    // // if(pincode.trim().length < 6){
    // //     alert('Enter valid pincode');
    // //     return false;
    // // }
    // // if(city.trim().length == 0){
    // //     alert('Enter valid city');
    // //     return false;
    // // }
    // // if(state.trim().length == 0){
    // //     alert('Select valid state');
    // //     return false;
    // // }
    // // if(address.trim().length == 0){
    // //     alert('Enter valid address');
    // //     return false;
    // // }
    

    // var qualificationType=[];
    // var qualificationFrom=[];
    // var qualificationYear=[];

    // $('.qualification').each(function() { qualificationType.push($(this).val()); });
    // console.log(qualificationType);
    // $('.qualificationFrom').each(function() { qualificationFrom.push($(this).val()); });
    // console.log(qualificationFrom);
    // $('.qualificationYear').each(function() { qualificationYear.push($(this).val()); });
    // console.log(qualificationYear);

    
    // var QualificationDetails = '';
    // var lstIndex = qualificationType.length -1;
    // for(var i=0;i<qualificationType.length;i++){
    //     // if(qualificationType[i] == '' && qualificationFrom[i] == '' && qualificationYear[i] == ''){
    //     //     var stringData = qualificationType[i]+'$'+qualificationFrom[i]+"$"+qualificationYear[i];
    //     // }
    //     var stringData = qualificationType[i]+'$'+qualificationFrom[i]+"$"+qualificationYear[i];
    //     if(i != lstIndex){
    //         stringData = stringData + "|";
    //     }
    //     QualificationDetails = QualificationDetails + stringData;
    // }
    // console.log('QualificationDetails >>> ',QualificationDetails);
    // // return false;

    // var empType = $('#empType').val();
    // var experience = $('#experience').val();
    // var current_Designation = $('#current_Designation').val();
    // var dateOfJoin = $('#dateOfJoin').val();
    // var last_experience = $('#last_experience').val();
    // var Company = $('#Company').val();
    // var Duration = $('#Duration').val();

    // // if(empType.trim().length == 0){
    // //     alert('Select valid Employee Type');
    // //     return false;
    // // }
    // // if(experience.trim().length == 0){
    // //     alert('Enter valid experience year');
    // //     return false;
    // // }
    // // if(current_Designation.trim().length == 0){
    // //     alert('Select valid current designation');
    // //     return false;
    // // }
    // // if(dateOfJoin.trim().length == 0){
    // //     alert('Enter valid date Of Join');
    // //     return false;
    // // }
    // // if(last_experience.trim().length == 0){
    // //     alert('Select valid experience year');
    // //     return false;
    // // }
    // // if(Company.trim().length == 0){
    // //     alert('Enter valid Company');
    // //     return false;
    // // }
    // // if(Duration.trim().length == 0){
    // //     alert('Select valid Duration');
    // //     return false;
    // // }
    
    // console.log('fullname >>> ',fullname);
    // console.log('email >>> ',email);
    // console.log('contact >>> ',contact);
    // console.log('alternateContact >>> ',alternateContact);
    // console.log('DOB >>> ',DOB);
    // console.log('fathersName >>> ',fathersName);
    // console.log('address >>> ',address);
    // console.log('pincode >>> ',pincode);
    // console.log('state >>> ',state);
    // console.log('city >>> ',city);
    // console.log('empType >>> ',empType);
    // console.log('experience >>> ',experience);
    // console.log('current_Designation >>> ',current_Designation);
    // console.log('dateOfJoin >>> ',dateOfJoin);
    // console.log('last_experience >>> ',last_experience);
    // console.log('Company >>> ',Company);
    // console.log('Duration >>> ',Duration);
    // console.log('QualificationDetails >>> ',QualificationDetails);
    // // return false;

    // // ev.preventDefault();   
    // //bundle the files and data we want to send to the server
    // var formdata = new FormData();
    // formdata.append("empID", empID);
    // formdata.append("fullname", fullname);
    // formdata.append("email", email);

    // // condition ? exprIfTrue : exprIfFalse

    // formdata.append("contact", contact);
    // formdata.append("alternateContact", alternateContact);
    // formdata.append("dateOfBirth", DOB);
    // formdata.append("fathersName", fathersName);
    // formdata.append("guardianName", $('input[name="guardianName"]').val());
    // formdata.append("address", address);
    // formdata.append("pincode", pincode);
    // formdata.append("state", state);
    // formdata.append("city", city);
    // formdata.append("empType", empType);
    // formdata.append("experience", experience);
    // formdata.append("current_Designation", current_Designation);
    // formdata.append("dateOfJoin", dateOfJoin);
    // formdata.append("last_experience", last_experience);
    // formdata.append("Company", Company);
    // formdata.append("Duration", Duration);
    // formdata.append("QualificationDetails",QualificationDetails);
    // formdata.append("perm_country", $('select[name="perm_country"]').val());
    // formdata.append("perm_state", $('select[name="perm_state"]').val());
    // formdata.append("perm_district", $('input[name="perm_district"]').val());
    // formdata.append("perm_address", $('textarea[name="perm_address"]').val());
    // formdata.append("perm_pincode", $('input[name="perm_pincode"]').val());
    
    // let myFileimg = document.getElementById('emp_photo').files[0];
    // if (typeof myFileimg != 'undefined') {
    //     formdata.append('profile_image', myFileimg, myFileimg['name']);
    // }
    // // ===================================================================================
    // //                                EMPLOYEE DOCS
    // // ===================================================================================
    // var empDocTypeName = [];
    // var empDocName= [];
    
    //     $('.emp_docs_type').each(function() { empDocTypeName.push($(this).attr('id')); });
    //     console.log(empDocTypeName);
    //     $('.empDocs').each(function() { empDocName.push($(this).attr('id')); });
    //     console.log(empDocName);

    //     for(var j=0;j<empDocTypeName.length;j++){
    //         let upload_docs_type = document.getElementById(empDocTypeName[j]).value;
    //         if (typeof upload_docs_type != 'undefined') {
    //             formdata.append('upload_docs_type_'+j+'', upload_docs_type);
    //         }
    //         let upload_docs = document.getElementById(empDocName[j]).files[0];
    //         if (typeof upload_docs != 'undefined') {
    //             formdata.append('upload_docs_'+j+'', upload_docs, upload_docs['name']);
    //         }
    //     }
    // // ===================================================================================
    // // ===================================================================================
    // Swal.fire({
    //     position: 'center',
    //     title: "<b style='font-size:20px;font-weight:500;color:#1eb6e9;'>Adding New Employee Details</b><br><div class='d-flex justify-content-center'>\
    //     <div class='spinner-border text-primary' role='status'>\
    //       <span class='sr-only'></span>\
    //     </div>\
    //   </div>",
    //     showConfirmButton: false,
    //     onOpen: () => {
    //         Swal.showLoading();
    //     }
    // })
    // // ---------------  AJAX CALL  ----------------------------
    // const csrftoken = getCookie('csrftoken');
    // $.ajax({
    //     type: 'POST',
    //     url: "/employee-management/add-employee",
    //     headers: { 'X-CSRFToken': csrftoken },
    //     data: formdata,
    //     cache : false,
    //     processData : false,
    //     contentType : false,
    //     encType : 'multipart/form-data',
    //     success: function (response) {
    //         console.log(response['response']);
    //         Swal.close();
    //         // $('#enquiryButton').css('display','');
    //         // $('#spinnerbtn').css('display','none');
    //         if(response['response'] == 'success'){

    //             // alert('New Employee Added successfully');
    //             // location.reload();
    //             // $('#exampleModalCenter').modal('hide');
    //             Swal.fire({
    //                 position: 'center',
    //                 icon: 'success',
    //                 title: '<small>New employee added successfully</small>',
    //                 showConfirmButton: false,
    //                 timer: 1500
    //               }).then(function(){
    //                   window.location.reload();
    //               })

    //         }else if(response['response'] == 'User With this Employee ID Already Exist!'){
    //             $('#emp-id').css('border','2px solid red');
    //             // alert('User With this Employee ID Already Exist!');
    //             Swal.fire({
    //                 position: 'center',
    //                 icon: 'error',
    //                 title: '<small>User With this Employee ID Already Exist!</small>',
    //                 showConfirmButton: false,
    //                 timer: 2000
    //               })
    //             return false;
    //         }else if(response['response'] == 'User With this Email Already Exist!'){
    //             $('#email').css('border','2px solid red');
    //             // alert('User With this Email Already Exist!');
    //             Swal.fire({
    //                 position: 'center',
    //                 icon: 'error',
    //                 title: '<small>User With this Email Already Exist!</small>',
    //                 showConfirmButton: false,
    //                 timer: 2000
    //               })
    //             return false;
    //         }else if(response['response'] == 'User With this Contact Already Exist!'){
    //             $('#contact').css('border','2px solid red');
    //             // alert('User With this Contact Already Exist!');
    //             Swal.fire({
    //                 position: 'center',
    //                 icon: 'error',
    //                 title: '<small>User With this Contact Already Exist!</small>',
    //                 showConfirmButton: false,
    //                 timer: 1500
    //               })
    //             return false;
    //         }else{
    //             alert('An Error occured while storing Employee Info. Please try again!');
    //             return false;
    //         }
    //     }
    // });
    // // --------------------------------------------------------
// }