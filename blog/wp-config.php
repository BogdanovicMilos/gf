<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

if (!function_exists('getenv_docker')) {
	// https://github.com/docker-library/wordpress/issues/588 (WP-CLI will load this file 2x)
	function getenv_docker($env, $default) {
		if ($fileEnv = getenv($env . '_FILE')) {
			return rtrim(file_get_contents($fileEnv), "\r\n");
		}
		else if (($val = getenv($env)) !== false) {
			return $val;
		}
		else {
			return $default;
		}
	}
}

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', getenv_docker('MYSQL_DATABASE', 'wordpress') );

/** MySQL database username */
define( 'DB_USER', getenv_docker('MYSQL_USER', 'user') );

/** MySQL database password */
define( 'DB_PASSWORD', getenv_docker('MYSQL_PASSWORD', 'password') );

/** MySQL hostname */
define( 'DB_HOST', 'blog-db' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '#L7[frz99}l(g0tzyeh?67L%2R)i(jQ$x8wp<9wR0GWlf{SA0:Vu$wtJP6QL5YS9' );
define( 'SECURE_AUTH_KEY',  '[#d~}0)FvT>*QZKjKe)_Y{Mdo~L4i#<FXUGlx3-JxdXZlFG@>3)0;+fIk +;jb,N' );
define( 'LOGGED_IN_KEY',    'niz`5jhL8Y$J$ <~IVpQ^Jo0N_qMCc::hiv`SVnAhOv;KSItt}sdRPuLK)ka=>Qe' );
define( 'NONCE_KEY',        'wZs5c9^a(k*F.!xrp&^_`WY6CdB]@-3R*W# :r&:Jpijleg2[PPK8sv-;)Rx<dtU' );
define( 'AUTH_SALT',        '5ef$)OT4Bz%.kL4*j^]nc0rb_I& ,z[X}OW#LEDTBRTsB,`zlRL|k/?SfrGTC!(D' );
define( 'SECURE_AUTH_SALT', '.IJZ8>#$g3b!^h)/;SU:s7;^Fgu`as^[EgWx PV$qt]P%bZn%6[i(h&6rm;4b1<|' );
define( 'LOGGED_IN_SALT',   '/Yi:aY#8C8kh~g9f4YB:1.=cle+^lc-h w*nhN(&YVzp(l}&@mPq0,H~1ToBmesM' );
define( 'NONCE_SALT',       'y^l)R<1&laIT||m6&AM-[`jZ,WyeWS)/OyLrdOQkgD{#u7<Kp[)7-A96z%[r!UI/' );

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/** Allow Direct Updating Without FTP */
define('FS_METHOD', 'direct');

/** Disable editing of themes and plugins using the built in editor */
define( 'DISALLOW_FILE_EDIT', true );


/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
