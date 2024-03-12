$(document).ready(function(){
    // register user
    toastr.options = {
        "progressBar": true,
        "positionClass": "toast-top-right"
      };

    // register user
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

    // login user
    $('#loginUser').validate({
        rules:{
            email:{
                required:true,
                email:true,
            },
            password:{
                required:true,
            }
        },
        messages:{
            email:{
                required:"This field is required",
                email:"Please enter a valid email address"
            },
            password:{
                required:"This field is required",
            }
        },
        submitHandler: function(form) {
            $.ajax({
                url: form.action,
                type: form.method,
                data: $(form).serialize(),
                beforeSend:function(){
                    $('#login-loader').html('Please wait...');
                    $('#login-user').hide();
                },
                success: function(response) {
                    $('#login-loader').html('Please wait...');
                    $('#login-user').hide();
                    if(response.status==200){
                        toastr.success(response.message);
                    } else if(response.status==400){
                        toastr.error(response.message);
                    } else {
                        toastr.warning(response.message);
                    }
                },
                complete:function(){
                    $('#login-loader').html('');
                    $('#login-user').show();
                }            
            });
        }
    });
});