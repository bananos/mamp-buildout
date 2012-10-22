MAMP-buildout
==============
Install Apache/MySQL/PHP stack on your Mac for development purposes.

**PHP 5.2/5.3 support!**

Works on OSX 10.7.3 / Xcode 4.3 / llvm-gcc-4.2
Works on OSX 10.7.4 / Xcode 4.4.1 / llvm-gcc-4.2
Works on OSX 10.7.5 / Xcode 4.5.1 / llvm-gcc-4.2

Installation
-------------

### Prerequisites

1. Make sure you have Xcode installed, otherwise all compilation stuff will fail.
2. At least Python 2.6 is installed (python2.7 is recommended)
3. Make sure a set of following links is still valid

```bash

http://curl.haxx.se/download/curl-7.25.0.tar.gz
http://www.ijg.org/files/jpegsrc.v8d.tar.gz
http://prdownloads.sourceforge.net/libpng/libpng-1.5.10.tar.gz
http://prdownloads.sourceforge.net/freetype/freetype-2.1.9.tar.bz2
ftp://ftp.gnu.org/gnu/gettext/gettext-0.18.1.1.tar.gz
http://www.apache.org/dist//httpd/httpd-2.2.22.tar.gz
http://www.mysql.com/get/Downloads/MySQL-5.1/mysql-5.1.66.tar.gz/from/http://cdn.mysql.com/

http://us.php.net/get/php-5.3.8.tar.gz/from/us.php.net/mirror
http://us.php.net/get/php-5.2.17.tar.gz/from/us.php.net/mirror

```

If some of them fail, just fix corresponding URL in ``buildout-base.cfg``


### Run bootstrap.py


```bash

[bananos@amber]$ git clone git@github.com:bananos/mamp-buildout.git
[bananos@amber]$ cd mamp-buildout

[bananos@amber]$ /usr/bin/python2.7 bootstrap.py
Creating directory '/Users/bananos/Projects/github/mamp-buildout/bin'.
Creating directory '/Users/bananos/Projects/github/mamp-buildout/parts'.
Creating directory '/Users/bananos/Projects/github/mamp-buildout/eggs'.
Creating directory '/Users/bananos/Projects/github/mamp-buildout/develop-eggs'.
Generated script '/Users/bananos/Projects/github/mamp-buildout/bin/buildout'.
```

### Specify your user/group

Open ``buildout.cfg``,  navigate to ``[buildout]`` section and modify user/group lines:

```ini

[buildout]
# We extend the buildout-development.cfg configuration
extends = buildout-base.cfg

# you should specify your user here
user  = bananos
group = staff
```
Save and proceed to next step.

### Run buildout

```bash

[bananos@amber]$ bin/buildout
```

Grab a cup of coffee & wait for a while for parts to compile. On core i5 mac it takes about 20min.


### Run supervisor

Once compilation is done, run [supervisor](http://supervisord.org), a client/server system that allows its users
to monitor and control a number of processes on UNIX-like operating systems.

```bash

[bananos@amber]$ bin/supervisord
```

Once supervisor daemon starts, you've already started mysql & apache processes. You can check them out:

```bash

[bananos@amber]$ bin/supervisorctl status
httpd                            RUNNING    pid 46002, uptime 0:00:08
mysqld                           RUNNING    pid 46003, uptime 0:00:08
```


### Test it in your browser

Go to ``var/www``  and create a simple ``index.php``:

```php

<?php

phpinfo();

?>
```

Open your browser at ``http://localhost:8080``, you should see PHP info page.


Project structure
------------------

After successful buildout you'll end up with something like this:

```bash

[bananos@amber]$ ls -l
 README.md
 bin
 bootstrap.py
 buildout-base.cfg
 buildout.cfg
 develop-eggs
 eggs
 etc             # <---- configuration for mysql/php/apache/supervisor
 parts           # <---- binary distributions live there
 templates       # <---- configuration templates
 thirdparty      # <---- source code & recipe downloads
 var             # <---- mysql data, PIDs, logs, www-root, etc.
```

**Note:**  To tune configuration for mysql/php or apache you should modify files in ``templates/``,
not in ``etc/`` which is recreated each time buildout is run.


Working with MySQL
-------------------

``mysql`` and ``mysqladmin`` are symlinked into ``bin/`` for convenience.


```bash

[bananos@amber]$ bin/mysql --protocol=TCP -u root --port=3305 --host=localhost

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1
Server version: 5.1.60-innodb-plugin-log Source distribution

Copyright (c) 2000, 2011, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> status
--------------
bin/mysql  Ver 14.14 Distrib 5.1.60, for apple-darwin11.3.0 (i386) using  EditLine wrapper

Connection id:		  1
Current database:
Current user:		  root@localhost
SSL:			      Not in use
Current pager:		  stdout
Using outfile:		  ''
Using delimiter:	  ;
Server version:		  5.1.60-innodb-plugin-log Source distribution
Protocol version:	  10
Connection:		      localhost via TCP/IP
Server characterset:  utf8
Db     characterset:  utf8
Client characterset:  utf8
Conn.  characterset:  utf8
TCP port:		      3305
Uptime:			      2 min 22 sec

Threads: 1  Questions: 4  Slow queries: 0  Opens: 15  Flush tables: 1  Open tables: 8  Queries per second avg: 0.28
--------------

mysql>
```

**Note:**  MySQL is compiled to listen on non-default ``3305`` port


Logs
-----
All logging happens to be in ``var/log/`` directory:

```bash

[bananos@amber]$ ls -l var/log/
total 32
-rw-r--r--  1 bananos  staff  1531 Feb  9 16:30 httpd.stdout.log
-rw-r--r--  1 bananos  staff     0 Feb  9 16:30 httpd_access.log
-rw-rw----  1 bananos  staff   303 Feb  9 16:30 mysqld-5.1.60.slow.log
-rw-r--r--  1 bananos  staff   925 Feb  9 16:30 mysqld-5.1.60.stdout.log
-rw-r--r--  1 bananos  staff   736 Feb  9 16:31 supervisord.log
```

MySQL/Apache stdout/stderr logs are intercepted by supervisor:

```bash

[bananos@amber]$ bin/supervisorctl tail httpd

httpd: Could not reliably determine the server's fully qualified domain name, using 192.168.99.249 for ServerName
[Thu Feb 09 16:30:40 2012] [info] Init: Seeding PRNG with 144 bytes of entropy
[Thu Feb 09 16:30:40 2012] [info] Init: Generating temporary RSA private keys (512/1024 bits)
[Thu Feb 09 16:30:40 2012] [info] Init: Generating temporary DH parameters (512/1024 bits)
[Thu Feb 09 16:30:40 2012] [warn] Init: Session Cache is not configured [hint: SSLSessionCache]
[Thu Feb 09 16:30:40 2012] [info] Init: Initializing (virtual) servers for SSL
[Thu Feb 09 16:30:40 2012] [info] mod_ssl/2.2.22 compiled against Server: Apache/2.2.22, Library: OpenSSL/0.9.8r
httpd: Could not reliably determine the server's fully qualified domain name, using 192.168.99.249 for ServerName
[Thu Feb 09 16:30:40 2012] [info] Init: Seeding PRNG with 144 bytes of entropy
[Thu Feb 09 16:30:40 2012] [info] Init: Generating temporary RSA private keys (512/1024 bits)
[Thu Feb 09 16:30:40 2012] [info] Init: Generating temporary DH parameters (512/1024 bits)
[Thu Feb 09 16:30:40 2012] [info] Init: Initializing (virtual) servers for SSL
[Thu Feb 09 16:30:40 2012] [info] mod_ssl/2.2.22 compiled against Server: Apache/2.2.22, Library: OpenSSL/0.9.8r
[Thu Feb 09 16:30:40 2012] [notice] Apache/2.2.22 (Unix) PHP/5.3.8 mod_ssl/2.2.22 OpenSSL/0.9.8r configured -- resuming normal operations
[Thu Feb 09 16:30:40 2012] [info] Server built: Feb  9 2012 16:02:28
[Thu Feb 09 16:30:40 2012] [debug] prefork.c(1023): AcceptMutex: flock (default: flock)
```


PHP/MySQL versions known to work
--------------------------------

This buildout currently tested on following configurations:

1. php-5.3.8 / MySQL-5.1.60
2. php-5.2.17 / MySQL-5.1.60
2. @TODO add php-5.2 / php-5.1  and MySQL 5.5 versions



TODO
-----
1. Add support for php-5.1
2. Add PostgreSQL



FAQ
----

### What is buildout?

[Buildout](http://www.buildout.org/) is a Python-based build system for creating, assembling
and deploying applications from multiple parts, some of which may be non-Python-based. 
It lets you create a buildout configuration and reproduce the same software later.


### Why didn't you use homebrew?

Though, [brew](http://mxcl.github.com/homebrew/) is really cool it does not support installation of custom php/mysql versions in an easy manner.


### Why not [MAMP](http://www.mamp.info/)?

Because I'm a command-liner, dude :)

