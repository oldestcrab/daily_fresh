$(function () {
	var error_name = false;
	var error_pwd = false;
	var error_check_pwd = false;
	var error_email = false;
	var error_check = false;


	$('#user_name').blur(function () {
		check_user_name();
	});

	$('#pwd').blur(function () {
		check_pwd();
	});

	$('#cpwd').blur(function () {
		check_cpwd();
	});

	$('#email').blur(function () {
		check_email();
	});

	$('#allow').click(function () {
		if ($(this).is(":checked")) {
			$(this).siblings('span').hide();
			error_check = false;
		} else {
			$(this).siblings('span').html("请勾选同意").show();
			error_check = true;
		}
	});

	function check_user_name() {
		// 判断长度是否符合
		var len = $('#user_name').val().length;
		if (len < 5 || len > 20) {
			$('#user_name').siblings('span').html('请输入5-20个字符的用户名');
			$('#user_name').siblings('span').show();
			error_name = true;
		} else {
			// 判断输入的用户名是否存在
			$.get("/user/register_exist/?user_name=" + $('#user_name').val(),
				function (data) {
					if (data.count >= 1) {
						$('#user_name').siblings('span').html('用户名已存在').show();
						error_name = true;
					} else {
						// 无问题隐藏提示信息
						$('#user_name').next().hide();
						error_name = false;
					}
				},
			);

		}
	};

	function check_pwd() {
		var pwd = $('#pwd').val().length;
		if (pwd < 8 || pwd > 20) {
			$('#pwd').siblings('span').html('密码最少8位，最长20位').show();
			error_pwd = true;
		} else {
			$('#pwd').next().hide();
			error_pwd = false;
		}
	}

	function check_cpwd() {
		var pwd = $('#pwd').val();
		var cpwd = $('#cpwd').val();
		if (pwd != cpwd) {
			$('#cpwd').siblings('span').html('两次输入的密码不一致').show();
			error_check_pwd = true;
		} else {
			$('#cpwd').next().hide();
			error_check_pwd = false;
		}
	}

	function check_email() {
		var re = /^[0-9a-z][\w\.\-]*@[0-9a-z\-]+(\.[a-z]{2,5}){1,2}$/i;
		// var re = /^[0-9a-z][\w\.\-]*@[0-9a-z\-]+(\.[a-z]{2,5}){1,2}$/;
		if (re.test($('#email').val())) {
			$('#email').next().hide();
			error_email = false;
		} else {
			$('#email').next().html('你输入的邮箱格式不正确').show();
			error_email = true;
		}
	}

	$('#reg_from').submit(function () {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		// var user_name = $('#user_name').val().length
		// if(user_name == 0){
		// 	$('#user_name').siblings('span').html('用户名不能为空');
		// 	$('#user_name').siblings('span').show();
		// 	error_name = true;
		// }


		if(error_name == false && error_pwd == false && error_check_pwd == false && error_email == false && error_check == false ){
			return true;
		}else{
			return false;
		}

	});
});