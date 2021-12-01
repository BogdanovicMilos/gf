<?php
use App\Template;
?>

<?php get_header(); ?>



    <div class="container" data-aos="fade" data-aos-delay="700">
        <div class="breadcrumbs">
            <ul>
                <li><a href="#">Home</a></li>
                <li>News</li>
            </ul>
        </div>
    </div>

    <section class="blog">
        <div class="container">
            <h1 class="page_title" data-aos="fade-up" data-aos-delay="100">Blog Posts</h1>
            <div class="blog__list">

                <?php if (have_posts()) : ?>

                    <!-- The Loop -->
                    <?php while (have_posts()) : the_post(); ?>
                        <?php include(Template::locate('_template-parts/archive/_entry.php')); ?>
                    <?php endwhile; ?>

                <?php else : ?>
                    <p>Sorry, no posts matched your criteria.</p>
                <?php endif; ?>

            </div>

            <div class="blog__pager">
                <div class="pager">
                    <ul>
                        <li><a href="#">1</a></li>
                        <li><a href="#">2</a></li>
                        <li class="active"><a href="#">3</a></li>
                        <li>...</li>
                        <li><a href="#">4</a></li>
                        <li><a href="#">5</a></li>
                    </ul>
                </div>
                <a href="#" class="btn btn-main">Load More Posts</a>
            </div>
        </div>
    </section>

<?php get_footer(); ?>
