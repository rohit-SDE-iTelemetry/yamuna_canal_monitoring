// empty name validator
function name_validator(thisTxtID, errorID) {
  if ($(thisTxtID).val().trim().length == 0) {
    $(thisTxtID).css("border", "2px solid red");
    $(errorID).css("display", "");
    return false;
  } else {
    $(thisTxtID).css("border", "");
    $(errorID).css("display", "none");
  }
}


// email validator
function email_validator(thisTxtID, errorID) {
  if ($(thisTxtID).val().trim().length == 0) {
    $(thisTxtID).css("border", "2px solid red");
    $(errorID).css("display", "");
    return false;
  } else {
    inputText = $(thisTxtID).val().trim();
    var mailformat = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/; 
    if (inputText.match(mailformat)) {
        $(thisTxtID).css("border", "");
        $(errorID).css("display", "none");
        return true;
    } else {
        $(thisTxtID).css("border", "2px solid red");
        $(errorID).css("display", "");
    }
  }
}


// contact validator
const invalid_contact = ['0000000000','1111111111','2222222222','3333333333','4444444444','5555555555','6666666666','7777777777','8888888888','9999999999']
function contact_validator(thisTxtID, errorID) {
    if ($(thisTxtID).val().trim().length < 10) {
        $(thisTxtID).css("border", "2px solid red");
        $(errorID).css("display", "");
        return false;
      } else {
        if(invalid_contact.includes($(thisTxtID).val().trim())){
            $(thisTxtID).css("border", "2px solid red");
            $(errorID).css("display", "");
            return false;
        }else{
            $(thisTxtID).css("border", "");
            $(errorID).css("display", "none");
        }
      }
  }
