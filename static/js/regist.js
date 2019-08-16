$(function(){
	var error_name = false


	$('#user_name').blur(function () {
		check_user_name();
	});

	function check_user_name(){
		var len = $('#user_name').val()
		alert(len);
	};

});