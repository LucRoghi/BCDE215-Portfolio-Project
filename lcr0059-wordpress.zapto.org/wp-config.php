<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );

/** Database username */
define( 'DB_USER', 'wordpressuser' );

/** Database password */
define( 'DB_PASSWORD', 'password' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         '>E;_d=V#Kl-6*.%w^-|R3qi)Hb d^Ze~5#n(K.#wA5u|2tMZad})qM^LLDUmAUY*');
define('SECURE_AUTH_KEY',  'Gi:+:-~`aHr,$t~C;.wV?+A1_u~LE-uzUQf`E[Rf0#MUn^et2D=AR)MFINuTz()V');
define('LOGGED_IN_KEY',    'Y6tFmfcEsGPZw Dl4@.>c-9[|yKzc^dq,uFGWNBFUca}JSrTR@?@7Mug!1z?p_)^');
define('NONCE_KEY',        'v[-Hl~lR9z-BUy1Q%qzr&|.WP7 (]w ~nn67O>i+]53t8];*&>fa|i0FC{S;m>..');
define('AUTH_SALT',        ';|>>N`g;vPZ0@kKR#ekzx-a&QYc&z`n61%^R7UHyu(K1}W&mk2x{%pq|`|;4m=mc');
define('SECURE_AUTH_SALT', 'Sbt,SS5QYNpn`0g1hp?ED3I{=$/|e!`}FuT%1Z&ysn{:3K;Z-`W/4BR-*X^G8[yZ');
define('LOGGED_IN_SALT',   'lU9&8?X~4?s/c)>hYIH%$XB(rB1x|x_YE@`FbC3p.nwfrzX9ZMhl(%|:M>y[+J%B');
define('NONCE_SALT',       '~~J(4CvBBP3goj*636-9+L+.A^jJk67KGi1<q3.+KFut; y|,0:[9}<!RO6 az?h');

/**#@-*/

/**
 * WordPress database table prefix.
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

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';

define('FS_METHOD', 'direct');
