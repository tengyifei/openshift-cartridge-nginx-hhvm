# OpenShift HHVM Cartridge

Nginx 1.7.8 with HHVM 3.4.2

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
