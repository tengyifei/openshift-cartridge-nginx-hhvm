# OpenShift HHVM Cartridge

[![Join the chat at https://gitter.im/tengyifei/openshift-cartridge-nginx-hhvm](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/tengyifei/openshift-cartridge-nginx-hhvm?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Nginx 1.7.8 with HHVM 3.6.0

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

### On the Web

[![NGINX+HHVM ON OpenShift](http://launch-shifter.rhcloud.com/launch/NGINX+HHVM ON.svg)](https://openshift.redhat.com/app/console/application_type/custom?&cartridges[]=http://cartreflect-claytondev.rhcloud.com/github/tengyifei/openshift-cartridge-nginx-hhvm&name=hhvm)

OpenShift also offers a [web-based application launcher workflow](https://blog.openshift.com/customizing-openshifts-web-based-app-creation-workflow/).  PHP project maintainers can [build their own launch buttons using this cart, with `launch-service`](http://launch-shifter.rhcloud.com/?cartridges[]=http://cartreflect-claytondev.rhcloud.com/github/tengyifei/openshift-cartridge-nginx-hhvm&initial_git_url=http://github.com/ryanj/silex-base&name=hhvm)

### Updating Cartridge

*Note: from HHVM version 3.5.0 onwards this cartridge uses INI settings instead of the deprecated HDF. You'll still have to do a manual upgrade to pick up this change.*

OpenShift Online has made it next to impossible to update web cartridges unintrusively. Previous methods involved removing the cartridge (therefore the entire app!) and reinstalling it to let OpenShift grab the latest version in the repository.
This cartridge now comes with a script to update HHVM and Nginx binaries without reinstalls necessary. To update your cartridge binaries, simply SSH into it and run `bin/control update` from shell:
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
