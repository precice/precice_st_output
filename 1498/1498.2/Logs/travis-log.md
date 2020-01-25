```
travis_fold:start:worker_info[0K[33;1mWorker information[0m
hostname: 0ce2f471-c6da-4abd-bdf3-0d147d058073@1.worker-org-57dfd4cd5-ff8q7.gce-production-3
version: v6.2.6 https://github.com/travis-ci/worker/tree/ba21bd30589fd152126e13df30e0cc78ccdf2837
instance: travis-job-eec7b2bc-62f5-4b91-8dde-ffe701390452 travis-ci-garnet-trusty-1512502259-986baf0 (via amqp)
startup: 6.340208319s
travis_fold:end:worker_info[0Ktravis_time:start:1446b1b2[0Ktravis_time:end:1446b1b2:start=1579947894996296777,finish=1579947895153698780,duration=157402003,event=no_world_writable_dirs[0Ktravis_time:start:00a73706[0Ktravis_time:end:00a73706:start=1579947895156275288,finish=1579947895161752061,duration=5476773,event=setup_filter[0Ktravis_time:start:0f4ce112[0Ktravis_time:end:0f4ce112:start=1579947895165235689,finish=1579947895173136413,duration=7900724,event=agent[0Ktravis_time:start:07d7804c[0Ktravis_time:end:07d7804c:start=1579947895176076977,finish=1579947895178035318,duration=1958341,event=check_unsupported[0Ktravis_time:start:05684c46[0Ktravis_fold:start:system_info[0K[33;1mBuild system information[0m
Build language: python
Build group: stable
Build dist: trusty
Build id: 641687652
Job id: 641687654
Runtime kernel version: 4.4.0-101-generic
travis-build version: 74fa7e3af
[34m[1mBuild image provisioning date and time[0m
Tue Dec  5 19:58:13 UTC 2017
[34m[1mOperating System Details[0m
Distributor ID:	Ubuntu
Description:	Ubuntu 14.04.5 LTS
Release:	14.04
Codename:	trusty
[34m[1mCookbooks Version[0m
7c2c6a6 https://github.com/travis-ci/travis-cookbooks/tree/7c2c6a6
[34m[1mgit version[0m
git version 2.15.1
[34m[1mbash version[0m
GNU bash, version 4.3.11(1)-release (x86_64-pc-linux-gnu)
[34m[1mgcc version[0m
gcc (Ubuntu 4.8.4-2ubuntu1~14.04.3) 4.8.4
Copyright (C) 2013 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

[34m[1mdocker version[0m
Client:
 Version:      17.09.0-ce
 API version:  1.32
 Go version:   go1.8.3
 Git commit:   afdb6d4
 Built:        Tue Sep 26 22:42:38 2017
 OS/Arch:      linux/amd64

Server:
 Version:      17.09.0-ce
 API version:  1.32 (minimum version 1.12)
 Go version:   go1.8.3
 Git commit:   afdb6d4
 Built:        Tue Sep 26 22:41:20 2017
 OS/Arch:      linux/amd64
 Experimental: false
[34m[1mclang version[0m
clang version 5.0.0 (tags/RELEASE_500/final)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /usr/local/clang-5.0.0/bin
[34m[1mjq version[0m
jq-1.5
[34m[1mbats version[0m
Bats 0.4.0
[34m[1mshellcheck version[0m
0.4.6
[34m[1mshfmt version[0m
v2.0.0
[34m[1mccache version[0m
ccache version 3.1.9

Copyright (C) 2002-2007 Andrew Tridgell
Copyright (C) 2009-2011 Joel Rosdahl

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 3 of the License, or (at your option) any later
version.
[34m[1mcmake version[0m
cmake version 3.9.2

CMake suite maintained and supported by Kitware (kitware.com/cmake).
[34m[1mheroku version[0m
heroku-cli/6.14.39-addc925 (linux-x64) node-v9.2.0
[34m[1mimagemagick version[0m
Version: ImageMagick 6.7.7-10 2017-07-31 Q16 http://www.imagemagick.org
[34m[1mmd5deep version[0m
4.2
[34m[1mmercurial version[0m
Mercurial Distributed SCM (version 4.2.2)
(see https://mercurial-scm.org for more information)

Copyright (C) 2005-2017 Matt Mackall and others
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
[34m[1mmysql version[0m
mysql  Ver 14.14 Distrib 5.6.33, for debian-linux-gnu (x86_64) using  EditLine wrapper
[34m[1mopenssl version[0m
OpenSSL 1.0.1f 6 Jan 2014
[34m[1mpacker version[0m
Packer v1.0.2

Your version of Packer is out of date! The latest version
is 1.1.2. You can update by downloading from www.packer.io
[34m[1mpostgresql client version[0m
psql (PostgreSQL) 9.6.6
[34m[1mragel version[0m
Ragel State Machine Compiler version 6.8 Feb 2013
Copyright (c) 2001-2009 by Adrian Thurston
[34m[1msubversion version[0m
svn, version 1.8.8 (r1568071)
   compiled Aug 10 2017, 17:20:39 on x86_64-pc-linux-gnu

Copyright (C) 2013 The Apache Software Foundation.
This software consists of contributions made by many people;
see the NOTICE file for more information.
Subversion is open source software, see http://subversion.apache.org/

The following repository access (RA) modules are available:

* ra_svn : Module for accessing a repository using the svn network protocol.
  - with Cyrus SASL authentication
  - handles 'svn' scheme
* ra_local : Module for accessing a repository on local disk.
  - handles 'file' scheme
* ra_serf : Module for accessing a repository via WebDAV protocol using serf.
  - using serf 1.3.3
  - handles 'http' scheme
  - handles 'https' scheme

[34m[1msudo version[0m
Sudo version 1.8.9p5
Configure options: --prefix=/usr -v --with-all-insults --with-pam --with-fqdn --with-logging=syslog --with-logfac=authpriv --with-env-editor --with-editor=/usr/bin/editor --with-timeout=15 --with-password-timeout=0 --with-passprompt=[sudo] password for %p:  --without-lecture --with-tty-tickets --disable-root-mailer --enable-admin-flag --with-sendmail=/usr/sbin/sendmail --with-timedir=/var/lib/sudo --mandir=/usr/share/man --libexecdir=/usr/lib/sudo --with-sssd --with-sssd-lib=/usr/lib/x86_64-linux-gnu --with-selinux
Sudoers policy plugin version 1.8.9p5
Sudoers file grammar version 43

Sudoers path: /etc/sudoers
Authentication methods: 'pam'
Syslog facility if syslog is being used for logging: authpriv
Syslog priority to use when user authenticates successfully: notice
Syslog priority to use when user authenticates unsuccessfully: alert
Send mail if the user is not in sudoers
Use a separate timestamp for each user/tty combo
Lecture user the first time they run sudo
Root may run sudo
Allow some information gathering to give useful error messages
Require fully-qualified hostnames in the sudoers file
Visudo will honor the EDITOR environment variable
Set the LOGNAME and USER environment variables
Length at which to wrap log file lines (0 for no wrap): 80
Authentication timestamp timeout: 15.0 minutes
Password prompt timeout: 0.0 minutes
Number of tries to enter a password: 3
Umask to use or 0777 to use user's: 022
Path to mail program: /usr/sbin/sendmail
Flags for mail program: -t
Address to send mail to: root
Subject line for mail messages: *** SECURITY information for %h ***
Incorrect password message: Sorry, try again.
Path to authentication timestamp dir: /var/lib/sudo
Default password prompt: [sudo] password for %p: 
Default user to run commands as: root
Value to override user's $PATH with: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
Path to the editor for use by visudo: /usr/bin/editor
When to require a password for 'list' pseudocommand: any
When to require a password for 'verify' pseudocommand: all
File descriptors >= 3 will be closed before executing a command
Environment variables to check for sanity:
	TZ
	TERM
	LINGUAS
	LC_*
	LANGUAGE
	LANG
	COLORTERM
Environment variables to remove:
	RUBYOPT
	RUBYLIB
	PYTHONUSERBASE
	PYTHONINSPECT
	PYTHONPATH
	PYTHONHOME
	TMPPREFIX
	ZDOTDIR
	READNULLCMD
	NULLCMD
	FPATH
	PERL5DB
	PERL5OPT
	PERL5LIB
	PERLLIB
	PERLIO_DEBUG 
	JAVA_TOOL_OPTIONS
	SHELLOPTS
	GLOBIGNORE
	PS4
	BASH_ENV
	ENV
	TERMCAP
	TERMPATH
	TERMINFO_DIRS
	TERMINFO
	_RLD*
	LD_*
	PATH_LOCALE
	NLSPATH
	HOSTALIASES
	RES_OPTIONS
	LOCALDOMAIN
	CDPATH
	IFS
Environment variables to preserve:
	JAVA_HOME
	TRAVIS
	CI
	DEBIAN_FRONTEND
	XAUTHORIZATION
	XAUTHORITY
	PS2
	PS1
	PATH
	LS_COLORS
	KRB5CCNAME
	HOSTNAME
	HOME
	DISPLAY
	COLORS
Locale to use while parsing sudoers: C
Directory in which to store input/output logs: /var/log/sudo-io
File in which to store the input/output log: %{seq}
Add an entry to the utmp/utmpx file when allocating a pty
PAM service name to use
PAM service name to use for login shells
Create a new PAM session for the command to run in
Maximum I/O log sequence number: 0

Local IP address and netmask pairs:
	10.240.0.28/255.255.255.255
	172.17.0.1/255.255.0.0

Sudoers I/O plugin version 1.8.9p5
[34m[1mgzip version[0m
gzip 1.6
Copyright (C) 2007, 2010, 2011 Free Software Foundation, Inc.
Copyright (C) 1993 Jean-loup Gailly.
This is free software.  You may redistribute copies of it under the terms of
the GNU General Public License <http://www.gnu.org/licenses/gpl.html>.
There is NO WARRANTY, to the extent permitted by law.

Written by Jean-loup Gailly.
[34m[1mzip version[0m
Copyright (c) 1990-2008 Info-ZIP - Type 'zip "-L"' for software license.
This is Zip 3.0 (July 5th 2008), by Info-ZIP.
Currently maintained by E. Gordon.  Please send bug reports to
the authors using the web page at www.info-zip.org; see README for details.

Latest sources and executables are at ftp://ftp.info-zip.org/pub/infozip,
as of above date; see http://www.info-zip.org/ for other sites.

Compiled with gcc 4.8.2 for Unix (Linux ELF) on Oct 21 2013.

Zip special compilation options:
	USE_EF_UT_TIME       (store Universal Time)
	BZIP2_SUPPORT        (bzip2 library version 1.0.6, 6-Sept-2010)
	    bzip2 code and library copyright (c) Julian R Seward
	    (See the bzip2 license for terms of use)
	SYMLINK_SUPPORT      (symbolic links supported)
	LARGE_FILE_SUPPORT   (can read and write large files on file system)
	ZIP64_SUPPORT        (use Zip64 to store large files in archives)
	UNICODE_SUPPORT      (store and read UTF-8 Unicode paths)
	STORE_UNIX_UIDs_GIDs (store UID/GID sizes/values using new extra field)
	UIDGID_NOT_16BIT     (old Unix 16-bit UID/GID extra field not used)
	[encryption, version 2.91 of 05 Jan 2007] (modified for Zip 3)

Encryption notice:
	The encryption code of this program is not copyrighted and is
	put in the public domain.  It was originally written in Europe
	and, to the best of our knowledge, can be freely distributed
	in both source and object forms from any country, including
	the USA under License Exception TSU of the U.S. Export
	Administration Regulations (section 740.13(e)) of 6 June 2002.

Zip environment options:
             ZIP:  [none]
          ZIPOPT:  [none]
[34m[1mvim version[0m
VIM - Vi IMproved 7.4 (2013 Aug 10, compiled Nov 24 2016 16:43:18)
Included patches: 1-52
Extra patches: 8.0.0056
Modified by pkg-vim-maintainers@lists.alioth.debian.org
Compiled by buildd@
Huge version without GUI.  Features included (+) or not (-):
+acl             +farsi           +mouse_netterm   +syntax
+arabic          +file_in_path    +mouse_sgr       +tag_binary
+autocmd         +find_in_path    -mouse_sysmouse  +tag_old_static
-balloon_eval    +float           +mouse_urxvt     -tag_any_white
-browse          +folding         +mouse_xterm     -tcl
++builtin_terms  -footer          +multi_byte      +terminfo
+byte_offset     +fork()          +multi_lang      +termresponse
+cindent         +gettext         -mzscheme        +textobjects
-clientserver    -hangul_input    +netbeans_intg   +title
-clipboard       +iconv           +path_extra      -toolbar
+cmdline_compl   +insert_expand   -perl            +user_commands
+cmdline_hist    +jumplist        +persistent_undo +vertsplit
+cmdline_info    +keymap          +postscript      +virtualedit
+comments        +langmap         +printer         +visual
+conceal         +libcall         +profile         +visualextra
+cryptv          +linebreak       +python          +viminfo
+cscope          +lispindent      -python3         +vreplace
+cursorbind      +listcmds        +quickfix        +wildignore
+cursorshape     +localmap        +reltime         +wildmenu
+dialog_con      -lua             +rightleft       +windows
+diff            +menu            -ruby            +writebackup
+digraphs        +mksession       +scrollbind      -X11
-dnd             +modify_fname    +signs           -xfontset
-ebcdic          +mouse           +smartindent     -xim
+emacs_tags      -mouseshape      -sniff           -xsmp
+eval            +mouse_dec       +startuptime     -xterm_clipboard
+ex_extra        +mouse_gpm       +statusline      -xterm_save
+extra_search    -mouse_jsbterm   -sun_workshop    -xpm
   system vimrc file: "$VIM/vimrc"
     user vimrc file: "$HOME/.vimrc"
 2nd user vimrc file: "~/.vim/vimrc"
      user exrc file: "$HOME/.exrc"
  fall-back for $VIM: "/usr/share/vim"
Compilation: gcc -c -I. -Iproto -DHAVE_CONFIG_H     -g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1      
Linking: gcc   -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,--as-needed -o vim        -lm -ltinfo -lnsl  -lselinux  -lacl -lattr -lgpm -ldl    -L/usr/lib/python2.7/config-x86_64-linux-gnu -lpython2.7 -lpthread -ldl -lutil -lm -Xlinker -export-dynamic -Wl,-O1 -Wl,-Bsymbolic-functions      
[34m[1miptables version[0m
iptables v1.4.21
[34m[1mcurl version[0m
curl 7.35.0 (x86_64-pc-linux-gnu) libcurl/7.35.0 OpenSSL/1.0.1f zlib/1.2.8 libidn/1.28 librtmp/2.3
[34m[1mwget version[0m
GNU Wget 1.15 built on linux-gnu.
[34m[1mrsync version[0m
rsync  version 3.1.0  protocol version 31
[34m[1mgimme version[0m
v1.2.0
[34m[1mnvm version[0m
0.33.6
[34m[1mperlbrew version[0m
/home/travis/perl5/perlbrew/bin/perlbrew  - App::perlbrew/0.80
[34m[1mphpenv version[0m
rbenv 1.1.1-25-g6aa70b6
[34m[1mrvm version[0m
rvm 1.29.3 (latest) by Michal Papis, Piotr Kuczynski, Wayne E. Seguin [https://rvm.io]
[34m[1mdefault ruby version[0m
ruby 2.4.1p111 (2017-03-22 revision 58053) [x86_64-linux]
[34m[1mCouchDB version[0m
couchdb 1.6.1
[34m[1mElasticSearch version[0m
5.5.0
[34m[1mInstalled Firefox version[0m
firefox 56.0.2
[34m[1mMongoDB version[0m
MongoDB 3.4.10
[34m[1mPhantomJS version[0m
2.1.1
[34m[1mPre-installed PostgreSQL versions[0m
9.2.24
9.3.20
9.4.15
9.5.10
9.6.6
[34m[1mRabbitMQ Version[0m
3.6.14
[34m[1mRedis version[0m
redis-server 4.0.6
[34m[1mriak version[0m
2.2.3
[34m[1mPre-installed Go versions[0m
1.7.4
[34m[1mant version[0m
Apache Ant(TM) version 1.9.3 compiled on April 8 2014
[34m[1mmvn version[0m
Apache Maven 3.5.2 (138edd61fd100ec658bfa2d307c43b76940a5d7d; 2017-10-18T07:58:13Z)
Maven home: /usr/local/maven-3.5.2
Java version: 1.8.0_151, vendor: Oracle Corporation
Java home: /usr/lib/jvm/java-8-oracle/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "4.4.0-98-generic", arch: "amd64", family: "unix"
[34m[1mgradle version[0m

------------------------------------------------------------
Gradle 4.0.1
------------------------------------------------------------

Build time:   2017-07-07 14:02:41 UTC
Revision:     38e5dc0f772daecca1d2681885d3d85414eb6826

Groovy:       2.4.11
Ant:          Apache Ant(TM) version 1.9.6 compiled on June 29 2015
JVM:          1.8.0_151 (Oracle Corporation 25.151-b12)
OS:           Linux 4.4.0-98-generic amd64

[34m[1mlein version[0m
Leiningen 2.8.1 on Java 1.8.0_151 Java HotSpot(TM) 64-Bit Server VM
[34m[1mPre-installed Node.js versions[0m
v4.8.6
v6.12.0
v6.12.1
v8.9
v8.9.1
[34m[1mphpenv versions[0m
  system
  5.6
* 5.6.32 (set by /home/travis/.phpenv/version)
  7.0
  7.0.25
  7.1
  7.1.11
  hhvm
  hhvm-stable
[34m[1mcomposer --version[0m
Composer version 1.5.2 2017-09-11 16:59:25
[34m[1mPre-installed Ruby versions[0m
ruby-2.2.7
ruby-2.3.4
ruby-2.4.1
travis_fold:end:system_info[0K
travis_time:end:05684c46:start=1579947895180619844,finish=1579947895187559672,duration=6939828,event=show_system_info[0Ktravis_time:start:1010a634[0Ktravis_time:end:1010a634:start=1579947895190234111,finish=1579947895211257179,duration=21023068,event=rm_riak_source[0Ktravis_time:start:0b16d00e[0Ktravis_time:end:0b16d00e:start=1579947895214184196,finish=1579947895219202449,duration=5018253,event=fix_rwky_redis[0Ktravis_time:start:26b3c1da[0Ktravis_time:end:26b3c1da:start=1579947895222302470,finish=1579947895561376990,duration=339074520,event=wait_for_network[0Ktravis_time:start:08bd0b8c[0Ktravis_time:end:08bd0b8c:start=1579947895576960623,finish=1579947896251509624,duration=674549001,event=update_apt_keys[0Ktravis_time:start:048980f4[0Ktravis_time:end:048980f4:start=1579947896256401338,finish=1579947897139826892,duration=883425554,event=fix_hhvm_source[0Ktravis_time:start:13c3b540[0Ktravis_time:end:13c3b540:start=1579947897145188113,finish=1579947897154311713,duration=9123600,event=update_mongo_arch[0Ktravis_time:start:17edcd60[0Ktravis_time:end:17edcd60:start=1579947897158431595,finish=1579947897193149496,duration=34717901,event=fix_sudo_enabled_trusty[0Ktravis_time:start:0d51870b[0Ktravis_time:end:0d51870b:start=1579947897196985266,finish=1579947897199341307,duration=2356041,event=update_glibc[0Ktravis_time:start:154607fc[0Ktravis_time:end:154607fc:start=1579947897203007975,finish=1579947897210857229,duration=7849254,event=clean_up_path[0Ktravis_time:start:0330dcdb[0Ktravis_time:end:0330dcdb:start=1579947897214795617,finish=1579947897221879130,duration=7083513,event=fix_resolv_conf[0Ktravis_time:start:0ccebc1a[0Ktravis_time:end:0ccebc1a:start=1579947897227376310,finish=1579947897235975382,duration=8599072,event=fix_etc_hosts[0Ktravis_time:start:0016d550[0Ktravis_time:end:0016d550:start=1579947897239577690,finish=1579947897247129462,duration=7551772,event=fix_mvn_settings_xml[0Ktravis_time:start:03017daf[0Ktravis_time:end:03017daf:start=1579947897251691249,finish=1579947897261715075,duration=10023826,event=no_ipv6_localhost[0Ktravis_time:start:0cd68381[0Ktravis_time:end:0cd68381:start=1579947897265731909,finish=1579947897268093167,duration=2361258,event=fix_etc_mavenrc[0Ktravis_time:start:114a9460[0Ktravis_time:end:114a9460:start=1579947897274594629,finish=1579947897277897475,duration=3302846,event=fix_wwdr_certificate[0Ktravis_time:start:0319becf[0Ktravis_time:end:0319becf:start=1579947897281167458,finish=1579947897306724493,duration=25557035,event=put_localhost_first[0Ktravis_time:start:1faf744d[0Ktravis_time:end:1faf744d:start=1579947897311060944,finish=1579947897314381087,duration=3320143,event=home_paths[0Ktravis_time:start:02c5b72c[0Ktravis_time:end:02c5b72c:start=1579947897319565168,finish=1579947897331224707,duration=11659539,event=disable_initramfs[0Ktravis_time:start:2396ed28[0Ktravis_time:end:2396ed28:start=1579947897335812801,finish=1579947897594038482,duration=258225681,event=disable_ssh_roaming[0Ktravis_time:start:19be8e4c[0Ktravis_time:end:19be8e4c:start=1579947897598768405,finish=1579947897601620335,duration=2851930,event=debug_tools[0Ktravis_time:start:045339b9[0Ktravis_time:end:045339b9:start=1579947897606094037,finish=1579947897610044335,duration=3950298,event=uninstall_oclint[0Ktravis_time:start:0a7ddf9c[0Ktravis_time:end:0a7ddf9c:start=1579947897615528065,finish=1579947897619507173,duration=3979108,event=rvm_use[0Ktravis_time:start:2dd1cbae[0Ktravis_time:end:2dd1cbae:start=1579947897624032161,finish=1579947897632861437,duration=8829276,event=rm_etc_boto_cfg[0Ktravis_time:start:2238a920[0Ktravis_time:end:2238a920:start=1579947897636288657,finish=1579947897638723292,duration=2434635,event=rm_oraclejdk8_symlink[0Ktravis_time:start:05913930[0Ktravis_time:end:05913930:start=1579947897642324172,finish=1579947897696099242,duration=53775070,event=enable_i386[0Ktravis_time:start:16c67b23[0Ktravis_time:end:16c67b23:start=1579947897700004836,finish=1579947897703479859,duration=3475023,event=update_rubygems[0Ktravis_time:start:02f4ac83[0Ktravis_time:end:02f4ac83:start=1579947897707820795,finish=1579947898540119385,duration=832298590,event=ensure_path_components[0Ktravis_time:start:023d165a[0Ktravis_time:end:023d165a:start=1579947898544372696,finish=1579947898546646886,duration=2274190,event=redefine_curl[0Ktravis_time:start:0273fb06[0Ktravis_time:end:0273fb06:start=1579947898550260268,finish=1579947898595392280,duration=45132012,event=nonblock_pipe[0Ktravis_time:start:174f9900[0Ktravis_time:end:174f9900:start=1579947898600208707,finish=1579947904631070003,duration=6030861296,event=apt_get_update[0Ktravis_time:start:262ff713[0Ktravis_time:end:262ff713:start=1579947904635164801,finish=1579947904637443877,duration=2279076,event=deprecate_xcode_64[0Ktravis_time:start:02f528c4[0Ktravis_time:end:02f528c4:start=1579947904641431841,finish=1579947908278453486,duration=3637021645,event=update_heroku[0Ktravis_time:start:011db400[0Ktravis_time:end:011db400:start=1579947908282173817,finish=1579947908284723579,duration=2549762,event=shell_session_update[0Ktravis_time:start:0b18dc3b[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3887
travis_fold:end:docker_mtu[0Ktravis_time:end:0b18dc3b:start=1579947908288119215,finish=1579947909470600789,duration=1182481574,event=set_docker_mtu[0Ktravis_time:start:1b51be5f[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:1b51be5f:start=1579947909473391996,finish=1579947909527115124,duration=53723128,event=resolvconf[0Ktravis_time:start:059a0cd6[0Ktravis_time:end:059a0cd6:start=1579947909531725727,finish=1579947909609568126,duration=77842399,event=maven_central_mirror[0Ktravis_time:start:0f896895[0Ktravis_time:end:0f896895:start=1579947909613511465,finish=1579947909672949688,duration=59438223,event=maven_https[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:12d1a268[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:12d1a268:start=1579947909746051323,finish=1579947910236808059,duration=490756736,event=configure[0Ktravis_time:start:094a04da[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:094a04da:start=1579947910241901594,finish=1579947918127645974,duration=7885744380,event=configure[0Ktravis_time:start:1b02f95a[0Ktravis_fold:start:services[0Ktravis_time:start:0b5c7d7a[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0b5c7d7a:start=1579947918149443832,finish=1579947918161049962,duration=11606130,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0b5c7d7a:start=1579947918149443832,finish=1579947921167272563,duration=3017828731,event=services[0Ktravis_time:start:10cbdb80[0Ktravis_time:end:10cbdb80:start=1579947921171624722,finish=1579947921174273108,duration=2648386,event=fix_ps4[0Ktravis_time:start:0613c579[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0295e3d9[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0295e3d9:start=1579947921182592285,finish=1579947926361025427,duration=5178433142,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:1b306920[0K$ git fetch origin +refs/pull/147/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/147/merge -> FETCH_HEAD
travis_time:end:1b306920:start=1579947926365724060,finish=1579947926728858391,duration=363134331,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:1b306920:start=1579947926365724060,finish=1579947927027654221,duration=661930161,event=checkout[0Ktravis_time:start:347058e0[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:347058e0:start=1579947927032364677,finish=1579947927043832001,duration=11467324,event=env[0Ktravis_time:start:0b191ce0[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:0b191ce0:start=1579947927048140525,finish=1579947927056659706,duration=8519181,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:000f3dd0[0K$ python system_testing.py -s of-of
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runFluid && cp -r Fluid/ /home/[secure]/Data/Output/"

      '
    container_name: openfoam-adapter-fluid
    image: [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
  openfoam-adapter-solid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam
      && sed -i ''s|<m2n:sockets from=\"Fluid\" to=\"Solid\"/>|<m2n:sockets from=\"Fluid\"
      to=\"Solid\" exchange-directory=\"/home/[secure]/Data/Exchange/\" network=\"eth0\"/>|g''
      [secure]-config.xml && ./runSolid && cp -r Solid/ /home/[secure]/Data/Output/"

      '
    container_name: openfoam-adapter-solid
    image: [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
  tutorial-data:
    container_name: tutorial-data
    image: alpine
    volumes:
    - output:/Output:rw
version: '3.0'
volumes:
  exchange: {}
  output: {}

Creating network "testcomposeofof_default" with the default driver
Creating network "testcomposeofof_[secure]comm" with the default driver
Creating volume "testcomposeofof_output" with default driver
Creating volume "testcomposeofof_exchange" with default driver
Pulling tutorial-data (alpine:latest)...
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:def31d1013d65c817c17d7798573862b7a630e67d5d5ba870507c83d187b879c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating openfoam-adapter-solid ... 
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid
Creating tutorial-data
Creating openfoam-adapter-fluid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!

```
