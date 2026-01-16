<?php
if (PHP_VERSION_ID < 70205) {
	header('Location: /phpMyAdmin/');
	exit; 
} else if (PHP_VERSION_ID < 80400) {
	header('Location: /phpMyAdmin5/');
	exit; 
} else if (PHP_VERSION_ID >= 80400) {
	echo "This version of <strong>phpMyAdmin 6</strong> is a pre-release version for PHP 8.4 and newer. <a href=\"./public/\"><strong>Continue</strong></a> at your own risk, or use <a href=\"../adminer/adminer.php\"><strong>Adminer</strong></a>.";
	exit;
}
?>

<!doctype html>
<html lang="en">
<head>
<title>phpMyAdmin</title>
<meta http-equiv="expires" content="0">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Cache-Control" content="no-cache">
<meta http-equiv="Refresh" content="0;url=./public/">
<script>
//<![CDATA[
setTimeout(function() { window.location = decodeURI('./public/'); }, 2000);
//]]>
</script>
</head>
<body>
<script>
//<![CDATA[
document.write('<p>Redirecting to the <a href="./public/">phpMyAdmin interface</a>. If you are not redirected automatically, click the link.</p>');
//]]>
</script>
</body>
</html>
