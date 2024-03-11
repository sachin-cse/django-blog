$(document).ready(function(){
    // register user
    toastr.options = {
        "progressBar": true,
        "positionClass": "toast-top-right"
      };

    $('#registerUser').validate({
        rules:{
            name:"required",
            email:{
                required:true,
                email:true,
            },
            password:{
                required:true,
                minlength: 8,
                maxlength: 8
            }
        },
        messages:{
            name:"This field is required",
            email:{
                required:"This field is required",
                email:"Please enter a valid email address"
            },
            password:{
                required:"This field is required",
                minlength:"Please enter at least {0} characters",
                maxlength:"Please enter maximum {0} characters"
            }
        },
        submitHandler: function(form) {
            $.ajax({
                url: form.action,
                type: form.method,
                data: $(form).serialize(),
                beforeSend:function(){
                    $('#loader').html('Please wait...');
                    $('#submitajaxform').hide();
                },
                success: function(response) {
                    $('#loader').html('Please wait...');
                    $('#submitajaxform').hide();
                    if(response.status==201){
                        toastr.success(response.message);
                    } else if(response.status==500){
                        toastr.error(response.message);
                    } else {
                        toastr.warning(response.message);
                    }
                },
                complete:function(){
                    $('#loader').html('');
                    $('#submitajaxform').show();
                }            
            });
        }
    });
});