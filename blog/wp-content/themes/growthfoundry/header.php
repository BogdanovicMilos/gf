<?php
use App\Template;
?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

    <title>Growth Foundry</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <meta name="description" content="description">
    <link rel="preload" href="<?= get_stylesheet_directory_uri() ?>/_assets/fonts/RNSPhysis/RNSPhysis-Black.woff" as="font" type="font/woff" crossorigin>
    <link rel="preload" href="<?= get_stylesheet_directory_uri() ?>/_assets/fonts/RNSPhysis/RNSPhysis-Bold.woff" as="font" type="font/woff" crossorigin>
    <link rel="preload" href="<?= get_stylesheet_directory_uri() ?>/_assets/fonts/RNSPhysis/RNSPhysis-Light.woff" as="font" type="font/woff" crossorigin>
    <link rel="preload" href="<?= get_stylesheet_directory_uri() ?>/_assets/fonts/RNSPhysis/RNSPhysis-Medium.woff" as="font" type="font/woff" crossorigin>
    <link rel="preload" href="<?= get_stylesheet_directory_uri() ?>/_assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-Roman.woff" as="font" type="font/woff" crossorigin>
    <link rel="preload" href="<?= get_stylesheet_directory_uri() ?>/_assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-Light.woff" as="font" type="font/woff" crossorigin>

    <link rel="stylesheet" href="<?= get_stylesheet_directory_uri() ?>/_assets/css/styles.css">

    <?php wp_head(); ?>

</head>
<body>
    <div id="page-wrap">

    <?php include(Template::locate('_template-parts/header/_header.php')); ?>
