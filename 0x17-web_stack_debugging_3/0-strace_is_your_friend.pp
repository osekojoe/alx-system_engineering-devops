# Fixing 500 error for an Apache is returning a 500 error

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
