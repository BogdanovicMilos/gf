<?php
use App\Template;


$gf_posts = new WP_Query([
    'post_type'=> 'post',
    'posts_per_page' => 5,
    'ignore_sticky_posts' => 1,
    'orderby' => 'date',
    'order' => 'DESC',
]);
?>

<div class="article_page__aside">
    <div class="article_page__aside-news">

        <?php if ($gf_posts->have_posts()) : ?>

            <!-- The Loop -->
            <?php while ($gf_posts->have_posts()) : $gf_posts->the_post(); ?>
                <?php include(Template::locate('_template-parts/archive/_entry.php')); ?>
            <?php endwhile; ?>

        <?php endif; ?>

    </div>
</div>
