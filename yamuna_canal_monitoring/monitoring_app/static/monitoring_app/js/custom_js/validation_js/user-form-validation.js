// global flags
let validPincode = true;

// get city and state
function getPostalAddress() {
    var pincode = $('#pincode').val().trim();
    if (pincode.length == 6) {
        $('#pincode-spinner').removeClass('d-none');
        $.ajax({
            type: 'GET',
            url: "https://api.postalpincode.in/pincode/"+pincode,
            success: function (response) {
                $('#pincode-spinner').addClass('d-none');
                if(response[0]['Status'] == 'Success'){
                    $('#valid-pincode').css('display','none');
                    $('#pincode').css('border','');
                    $('#pincode').css('color','black');

                    var district = response[0]['PostOffice'][0]['District'];
                    var state = response[0]['PostOffice'][0]['State'];
                    $('#city').val('');
                    $('#state').val('');
                    
                    $('#city').val(district);
                    $('#state').val(state);
                    validPincode = true;
                }else{
                    $('#pincode').css('border','2px solid red');
                    $('#pincode').css('color','red');
                    $('#valid-pincode').css('display','');
                    $('#city').val('');
                    $('#state').val('');
                    validPincode = false;
                }
                
            }
        });
    }else{
        $('#city').val('');
        $('#state').val('');
        validPincode = false;
    }
}



// function validateUserForm(){
//     // name check
//     if($('#name').val().trim().length == 0 || $('#name').val().trim().length <= 5){
//         alert('Invalid name');
//         return false;
//     }
// }



// function validateName(thisTxt){
//     if($('#name').val().trim().length == 0 || $('#name').val().trim().length <= 5){
//         alert('Invalid name');
//         return false;
//     }else{
//         return true;
//     }
// }