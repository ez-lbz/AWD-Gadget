适当使用sm3.sh，谨慎使用sm4.sh，sm5.sh

### 小技巧

可以使用alias来修改键位：
```shell
alias cat='echo flag{1b2c3d4e5f6g7h8i9j0k}'
```

取消方式为：
```shell
unalias cat
```

### 源码备份

项目源码备份：
```shell
cd /var/www/html
tar -zcvf ~/html.tar.gz *
```

项目源码还原：
```shell
rm -rf /var/www/html
tar -zxvf ~/html.tar.gz -C /var/www/html
```

### 数据库与ssh

查找数据库密码：
```shell
cd /var/www/html
find .|xargs grep "password"
```

数据库备份：
```shell
$ cd /var/lib/mysql #(进入到MySQL库目录，根据自己的MySQL的安装情况调整目录)
$ mysqldump -u root -p Test > Test.sql # 输入密码即可。
$ mysqldump -u root -p --all-databases > ~/backup.sql  # 备份所有数据库
$ mysqldump -u root -p --all-databases -skip-lock-tables > ~/backup.sql  # 跳过锁定的数据库表
```

数据库还原：
```shell
$ mysql -u root -p
mysql> create database [database_name];  # 输入要还原的数据库名
mysql> use [database_name]
mysql> source backup.sql;    # source后跟备份的文件名Copy
```

数据库口令修改：
```shell
$ mysql -u root -p
show databases;
use mysql
set password for root@localhost = password('123');
或者
update user set password = PASSWORD('需要更换的密码') where user='root';
update user set password = PASSWORD('1') where user='root';
flush privileges;
show tables;   # 看看有没有flag
```

ssh修改（如果不是相同密码可以不修改）：
```shell
passwd [user]
```

### 监控

常见的MVC框架入口点（用于添加监控）：
```shell
PHPCMS V9 \phpcms\base.php
PHPWIND8.7 \data\sql_config.php
DEDECMS5.7 \data\common.inc.php
DiscuzX2   \config\config_global.php
Wordpress   \wp-config.php
Metinfo   \include\head.php
```

如果不是MVC结构的话使用如下命令在所有php文件开头添加：
```shell
find /var/www/html/ -type f -path "*.php" | xargs sed -i "s/<?php /<?php\nrequire_once('\/var\/www\/html\/waf2.php');\n/g"
```
