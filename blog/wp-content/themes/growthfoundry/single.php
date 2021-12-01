<?php
use App\Template;
?>

<?php get_header(); ?>

    <?php while (have_posts()) : the_post(); ?>

        <div class="container" data-aos="fade" data-aos-delay="700">
            <div class="breadcrumbs">
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">News</a></li>
                    <li><?php the_title(); ?></li>
                </ul>
            </div>
        </div>

        <section class="article_page">
            <div class="container">
                <div class="article_page__row">

                    <?php include(Template::locate('_template-parts/single/_entry.php')); ?>

                    <?php get_sidebar(); ?>

                </div>
            </div>
        </section>

    <?php endwhile; ?>

<?php get_footer(); ?>
