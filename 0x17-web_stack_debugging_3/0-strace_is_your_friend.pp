# strace did not provide revealing errors, even when run with -e flag
# defautled to asking

exec { 'change wp-locale extension':
    command  => 'sed  -i  s/phpp/php/g /var/www/html/wp-settings.php',
    provider => shell,
}
