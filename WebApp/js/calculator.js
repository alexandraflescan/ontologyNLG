// Select all the from document using queryselectAll
var keys = document.querySelectorAll('#calculator span');
// Define operators
var operators = ['+', '-', 'x', '÷'];
// Set decimal flag for use later
var decimalAdded = false;

// loop through all keys
for (var i = 0; i < keys.length; i++) {
    //add onclick event to the keys
    keys[i].onclick = function (e) {
        // Get the input and button values
        var input = document.querySelector('.screen');
        var inputVal = input.innerHTML;
        var btnVal = this.innerHTML;

        // If clear key is pressed, erase everything
        if (btnVal == 'Del') {
            input.innerHTML = input.innerHTML.substring(0, input.innerHTML.length - 1);
            decimalAdded = false;
        }

        // Javascript checks

        // No two operators should be added consecutively.
        else if (operators.indexOf(btnVal) > -1) {
            // Get the last character from the equation
            var lastChar = inputVal[inputVal.length - 1];

            // Only add operator if input is not empty
            if (inputVal != '' && operators.indexOf(lastChar) == -1)
                input.innerHTML += btnVal;

            // Allow minus operator if the string is empty
            else if (inputVal == '' && btnVal == '-')
                input.innerHTML += btnVal;

            // Replace the last operator (if exists) with the newly pressed operator
            if (operators.indexOf(lastChar) > -1 && inputVal.length > 1) {
                input.innerHTML = inputVal.replace(/.$/, btnVal);
            }

            decimalAdded = false;
        }
        // allow decimal point input
        else if (btnVal == '.') {
            if (!decimalAdded) {
                input.innerHTML += btnVal;
                decimalAdded = true;
            }
        }

        else if (btnVal == 'Go!') {
            inputVal= inputVal.replace(/x/g, '*').replace(/÷/g, '/').replace(/\^/g, '\*\*');
            var queryParam = encodeURIComponent(inputVal);

            jQuery.ajax({
                url: ' http://127.0.0.1:5000/problem?op=' + queryParam,
                type: 'GET',
                error: function (error) {
                    console.log(error);
                },
                success: function (data) {
                    let panel_body = document.querySelector('#problem_output .panel-body');
                    panel_body.innerHTML += `<span class="problem">${data["problem"]}</span>`;

                }
            });
        }
        // if any other key is pressed, just append it after the decimal
        else {
            input.innerHTML += btnVal;
        }

        // prevent page jumps
        e.preventDefault();
    }
}

//adding keyboard input functionality
document.onkeydown = function (event) {

    var key_press = String.fromCharCode(event.keyCode);
    var key_code = event.keyCode;
    var input = document.querySelector('.screen');
    var inputVal = input.innerHTML;
    var btnVal = this.innerHTML;
    var lastChar = inputVal[inputVal.length - 1];

    // Target each keypress and update the input screen

    if (key_press == 1) {
        input.innerHTML += key_press;
    }
    if (key_press == 2) {
        input.innerHTML += key_press;
    }
    if (key_press == 3 || key_code == 32) {
        input.innerHTML += key_press;
    }
    if (key_press == 4) {
        input.innerHTML += key_press;
    }
    if (key_press == 5) {
        input.innerHTML += key_press;
    }
    if (key_press == 6 && event.shiftKey == false) {
        input.innerHTML += key_press;
    }
    if (key_press == 7) {
        input.innerHTML += key_press;
    }
    if (key_press == 8 && event.shiftKey == false) {
        input.innerHTML += key_press;
    }
    if (key_press == 9) {
        input.innerHTML += key_press;
    }
    if (key_press == 0) {
        input.innerHTML += key_press;
    }

    // Cature operators and prevent from addint two consecutuve operators

    if ((inputVal != '' && operators.indexOf(lastChar) == -1 && key_code == 187 && event.shiftKey) || (key_code == 107) || (key_code == 61 && event.shiftKey)) {
        document.querySelector('.screen').innerHTML += '+';
    }
    if ((inputVal != '' && operators.indexOf(lastChar) == -1 && key_code == 189 && event.shiftKey) || (inputVal != '' && operators.indexOf(lastChar) == -1 && key_code == 107)) {
        document.querySelector('.screen').innerHTML += '-';
    }
    if ((inputVal != '' && operators.indexOf(lastChar) == -1 && key_code == 56 && event.shiftKey) || (inputVal != '' && operators.indexOf(lastChar) == -1 && key_code == 106)) {
        document.querySelector('.screen').innerHTML += 'x';
    }
    if ((inputVal != '' && operators.indexOf(lastChar) == -1 && key_code == 191) || (inputVal != '' && operators.indexOf(lastChar) == -1 && key_code == 111)) {
        document.querySelector('.screen').innerHTML += '÷';
    }

    if (key_code == 8 || key_code == 46) {
        input.innerHTML = input.innerHTML.substring(0, input.innerHTML.length - 1);
        decimalAdded = false;
    }
}

