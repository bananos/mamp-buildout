=================
MAMP-buildout
=================
Install Apache/MySQL/PHP stack on your Mac for development purposes.



Installation
==============

Prerequisites
--------------
1) Make sure you have Xcode installed, otherwise all compilation stuff will fail.
2) At least Python 2.6 is installed (2.7 is recommended)
3) Make sure a set of following links is still valid:

.. code-block:: bash

   http://dev.mysql.com/get/Downloads/MySQL-5.1/mysql-5.1.60.tar.gz/from/http://mysql.infocom.ua/
   http://us3.php.net/get/php-5.3.8.tar.gz/from/ua.php.net/mirror
   http://curl.download.nextag.com/download/curl-7.20.0.tar.gz
   http://ftp.gnu.org/pub/gnu/libiconv/libiconv-1.9.2.tar.gz
   http://www.ijg.org/files/jpegsrc.v8c.tar.gz
   http://prdownloads.sourceforge.net/libpng/libpng-1.4.0.tar.gz
   http://prdownloads.sourceforge.net/freetype/freetype-2.1.9.tar.bz2
   ftp://ftp.gnu.org/gnu/gettext/gettext-0.18.1.1.tar.gz
   http://www.apache.org/dist//httpd/httpd-2.0.64.tar.gz

If some them fail, just fix corresponding URL in ``buildout-base.cfg``   


Run bootstrap.py
-----------------

.. code-block:: bash

   git clone git@github.com:bananos/mamp-buildout.git
   cd mamp-buildout

   bananos@amber: ~/Projects/github/mamp-buildout (master) $ /usr/bin/python2.7 bootstrap.py 
   Creating directory '/Users/bananos/Projects/github/mamp-buildout/bin'.
   Creating directory '/Users/bananos/Projects/github/mamp-buildout/parts'.
   Creating directory '/Users/bananos/Projects/github/mamp-buildout/eggs'.
   Creating directory '/Users/bananos/Projects/github/mamp-buildout/develop-eggs'.
   Generated script '/Users/bananos/Projects/github/mamp-buildout/bin/buildout'.


Run buildout
------------

.. code-block:: bash

   bin/buildout



 





FAQ
======


What is buildout?
------------------
`Buildout <http://www.buildout.org/>` is a Python-based build system for creating, assembling 
and deploying applications from multiple parts, some of which may be non-Python-based. 
It lets you create a buildout configuration and reproduce the same software later.


Why didn't you use homebrew?
-----------------------------
Though, `brew <http://mxcl.github.com/homebrew/>`_ is really cool it does not support installation of custom php/mysql versions in an easy manner.
