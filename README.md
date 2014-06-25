# OpenShift HHVM Cartridge

Nginx 1.6.0 with HHVM 3.1.0

Partly based on [pinodex/openshift-nginx-php-fpm](https://github.com/pinodex/openshift-nginx-php-fpm).

## Usage

### Command line
```bash
$ rhc app create appname http://cartreflect-claytondev.rhcloud.com/github/tengyifei/openshift-cartridge-nginx-hhvm
$ cd appname
$ echo '<?php echo "Hello HHVM " . HHVM_VERSION; ?>' > www/index.php
$ git add .
$ git commit -m 'Testing'
$ git push
```

## HHVM

The HHVM packaged with this cartridge is built directly from HHVM 3.1.0 source. Different from the official version, it comes with the experimental Zend Compatibility Layer (enabling many Zend extensions e.g. gettext, oauth) and a GeoIP plug-in. However, the user must manually specify a GeoIP database location via the HHVM config file.

## User-defined configuration

Place your nginx .conf files inside config/nginx.d/. It will be include()ed from "http" scope.
You may edit the config.hdf inside config/hhvm.d/. This configuration file will be loaded by HHVM.