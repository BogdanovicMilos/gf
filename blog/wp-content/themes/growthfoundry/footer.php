<?php
use App\Template;
?>

        <?php include(Template::locate('_template-parts/footer/_footer.php')); ?>

        <?php include(Template::locate('_template-parts/footer/_footer_menu.php')); ?>

    </div>

    <?php include(Template::locate('_template-parts/footer/_footer_svg.php')); ?>

    <script src="<?= get_stylesheet_directory_uri() ?>/_assets/js/jquery-3.6.0.min.js"></script>
    <script src="<?= get_stylesheet_directory_uri() ?>/_assets/js/aos.js"></script>
    <script src="<?= get_stylesheet_directory_uri() ?>/_assets/js/dynamic-adaptiv.js"></script>
    <script src="<?= get_stylesheet_directory_uri() ?>/_assets/js/jquery.fancybox.min.js"></script>
    <script src="<?= get_stylesheet_directory_uri() ?>/_assets/js/jquery.inputmask.bundle.min.js"></script>
    <script src="<?= get_stylesheet_directory_uri() ?>/_assets/js/jquery.viewportchecker.min.js"></script>
    <script src="<?= get_stylesheet_directory_uri() ?>/_assets/js/sticky-kit.min.js"></script>
    <script src="<?= get_stylesheet_directory_uri() ?>/_assets/js/swiper-bundle.min.js"></script>

    <script src="<?= get_stylesheet_directory_uri() ?>/_assets/js/common.js"></script>

    <?php wp_footer(); ?>

</body>
</html>
