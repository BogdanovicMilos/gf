<?php

namespace App;

class Template
{
    /**
     * Locate template
     * @param $path
     * @return string
     */
    public static function locate($path)
    {
        return locate_template($path, false, false);
    }

    /**
     * Get the post ID
     * @return int
     */
    public static function getPostID()
    {
        global $post;
        return $post->ID;
    }
}
