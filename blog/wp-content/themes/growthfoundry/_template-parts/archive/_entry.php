<article class="blog__article" data-aos="fade-up" data-aos-delay="100">
    <a href="<?php echo get_permalink(); ?>" class="blog__article-thumb">
        <?php if (has_post_thumbnail()) : ?>
            <?php the_post_thumbnail('archive_thumbnail'); ?>
        <?php else : ?>
            <img src="<?= get_stylesheet_directory_uri() ?>/_assets/img/content/blog-1.jpg" alt="">
        <?php endif; ?>
    </a>
    <a href="<?php echo get_permalink(); ?>" class="blog__article-title">
        <?php the_title(); ?>
    </a>
    <div class="blog__article-descr">
        <?php the_excerpt(); ?>
    </div>
    <div class="blog__article-mata">
        Posted on <?php the_date(); ?> by
        <?php echo get_the_author_meta( 'first_name' ); ?>
        <?php echo get_the_author_meta( 'last_name' ); ?>
    </div>
</article>
