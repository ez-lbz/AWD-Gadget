<?php
$ip = $_SERVER["REMOTE_ADDR"];

    $filename = $_SERVER['PHP_SELF'];
    $parameter = $_SERVER["QUERY_STRING"];
    $method = $_SERVER['REQUEST_METHOD'];
    $uri = $_SERVER['REQUEST_URI'];
    $time = date('Y-m-d H:i:s',time());
    $post = file_get_contents("php://input",'r');
    $logadd = 'Visit Time：'.$time.' '.'Visit IP：'.$ip."\r\n".'RequestURI：'.$uri.' '.$parameter.'RequestMethod：'.$method."\r\n";
    $fh = fopen("/tmp/log.txt", "a+");
    fwrite($fh, $logadd);
    fwrite($fh, print_r($_COOKIE, true)."\r\n");
    fwrite($fh, $post."\r\n");
    fwrite($fh, $others."\r\n");
    fclose($fh);
?>