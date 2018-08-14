#!/usr/bin/env php
<?php
	print_r($_GET);
	echo 'hello ' . htmlspecialchars($_GET["name"]) . '!';
?>
