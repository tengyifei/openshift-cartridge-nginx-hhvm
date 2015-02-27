# OpenShift HHVM Cartridge

Nginx 1.7.7 with HHVM 3.4.1

Partly based on [pinodex/openshift-nginx-php-fpm](https://github.com/pinodex/openshift-nginx-php-fpm).

## Usage

### Command line
```bash
$ rhc app create <appname> http://cartreflect-claytondev.rhcloud.com/github/ranib/openshift-cartridge-nginx-hhvm
$ cd <appname>
$ echo '<?php echo "Hello HHVM " . HHVM_VERSION; ?>' > www/index.php
$ git add .
$ git commit -m 'Testing'
$ git push

To add mysql cartridge
$ rhc cartridge add mysql-5.5 -a <appname>

To add Wordpress
$ cd <appname>
$ git remote add upstream https://github.com/openshift/wordpress-example
$ git pull upstream master
## 1. fix conflicts in action_hooks/deploy
## 2. edit wp-config.php file (change FORCE_SSL_ADMIN to false)
## 3. add in wp-config.php file
## (before this line) /* That's all, stop editing! Happy blogging. */
## /** Woocommerce plugin recommends to increase WP Memory Limit to 64MB */
## define( 'WP_MEMORY_LIMIT', '64M' );
## (at the end)
## /** path to fastcgi cache directory for Nginx Helper plugin */
## define('RT_WP_NGINX_HELPER_CACHE_PATH','/tmp/nginx/nginx-cache');
## 4. then commit
$ git add -A
$ git commit -am 'install wordpress'
$ git push
```
### To check your logs on your gear (troubleshoot)
rhc tail -a <appname>
or
rhc ssh <appname>
cd $OPENSHIFT_LOG_DIR

### Updating Cartridge
OpenShift Online has made it next to impossible to update web cartridges unintrusively. Previous methods involved removing the cartridge (therefore the entire app!) and reinstalling it to let OpenShift grab the latest version in the repository.
This cartridge now comes with a script to update HHVM and Nginx binaries without reinstalls necessary. To update your cartridge, simply SSH into it and run `bin/control update` from shell:
```bash
rhc ssh hhvmtest
# In SSH
cd nginx-hhvm
bin/control update
```

## HHVM

The HHVM packaged with this cartridge is built directly from the newest released version of HHVM source. Different from the official version, it comes with the experimental Zend Compatibility Layer (enabling many Zend extensions e.g. gettext, oauth) and a GeoIP plug-in. However, the user must manually specify a GeoIP database location via the HHVM config file.

## User-defined configuration

Place your nginx .conf files inside config/nginx.d/. It will be include()ed from "http" scope.

You may edit the config.hdf inside config/hhvm.d/. This configuration file will be loaded by HHVM.
