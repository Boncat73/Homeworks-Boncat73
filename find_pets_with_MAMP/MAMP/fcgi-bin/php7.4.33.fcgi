#!/bin/sh
export PHP_FCGI_CHILDREN=4
export PHP_FCGI_MAX_REQUESTS=10000
exec /Applications/MAMP/bin/php/php7.4.33/bin/php-cgi -c "/Library/Application Support/appsolute/MAMP PRO/conf/php7.4.33.ini"
