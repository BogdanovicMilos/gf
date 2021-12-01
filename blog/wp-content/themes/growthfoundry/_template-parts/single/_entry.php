<?php
use App\Template;
?>

<article class="article_page__content">
    <h1 class="article_page__title"><?php the_title(); ?></h1>
    <div class="article_page__meta">
        Posted on <?php the_date(); ?> by
        <strong>
            <?php echo get_the_author_meta( 'first_name' ); ?>
            <?php echo get_the_author_meta( 'last_name' ); ?>
        </strong>
    </div>
    <div class="article_page__text">
        <?php if (has_post_thumbnail()) : ?>
            <div class="blog__article-thumb">
                <?php the_post_thumbnail('single_thumbnail'); ?>
            </div>
        <?php endif; ?>
        <div class="richtext">
            <h2>Create Partnership</h2>
            <div>
                <?php the_content(); ?>
            </div>
        </div>
    </div>

    <?php include(Template::locate('_template-parts/single/_share_block.php')); ?>

</article>
