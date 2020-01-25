```
travis_fold:start:worker_info[0K[33;1mWorker information[0m
hostname: 750d5ac4-dc11-47f4-929e-22152b134722@1.worker-org-847f45b8fd-58q2f.gce-production-2
version: v6.2.6 https://github.com/travis-ci/worker/tree/ba21bd30589fd152126e13df30e0cc78ccdf2837
instance: travis-job-3259bd36-5298-4dd5-9b0c-b6da5ace11f5 travis-ci-garnet-trusty-1512502259-986baf0 (via amqp)
startup: 6.503209831s
travis_fold:end:worker_info[0Ktravis_time:start:0db36656[0Ktravis_time:end:0db36656:start=1579947893322418389,finish=1579947893469782618,duration=147364229,event=no_world_writable_dirs[0Ktravis_time:start:01b1e43a[0Ktravis_time:end:01b1e43a:start=1579947893472259733,finish=1579947893474648502,duration=2388769,event=setup_filter[0Ktravis_time:start:0e68b8b2[0Ktravis_time:end:0e68b8b2:start=1579947893479040973,finish=1579947893485325365,duration=6284392,event=agent[0Ktravis_time:start:1fb75c81[0Ktravis_time:end:1fb75c81:start=1579947893487788298,finish=1579947893489544998,duration=1756700,event=check_unsupported[0Ktravis_time:start:0ab8a7e0[0Ktravis_fold:start:system_info[0K[33;1mBuild system information[0m
Build language: python
Build group: stable
Build dist: trusty
Build id: 641687652
Job id: 641687655
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
travis_time:end:0ab8a7e0:start=1579947893491945964,finish=1579947893496744725,duration=4798761,event=show_system_info[0Ktravis_time:start:03189ad4[0Ktravis_time:end:03189ad4:start=1579947893499261952,finish=1579947893518449946,duration=19187994,event=rm_riak_source[0Ktravis_time:start:02d2d253[0Ktravis_time:end:02d2d253:start=1579947893521660497,finish=1579947893529328083,duration=7667586,event=fix_rwky_redis[0Ktravis_time:start:020a9648[0Ktravis_time:end:020a9648:start=1579947893532128630,finish=1579947893845810626,duration=313681996,event=wait_for_network[0Ktravis_time:start:212d95eb[0Ktravis_time:end:212d95eb:start=1579947893850290244,finish=1579947894846986181,duration=996695937,event=update_apt_keys[0Ktravis_time:start:2f33907e[0Ktravis_time:end:2f33907e:start=1579947894850109207,finish=1579947895796335590,duration=946226383,event=fix_hhvm_source[0Ktravis_time:start:040b8730[0Ktravis_time:end:040b8730:start=1579947895800585745,finish=1579947895808852058,duration=8266313,event=update_mongo_arch[0Ktravis_time:start:0408a4e0[0Ktravis_time:end:0408a4e0:start=1579947895812228565,finish=1579947895847602319,duration=35373754,event=fix_sudo_enabled_trusty[0Ktravis_time:start:003c0802[0Ktravis_time:end:003c0802:start=1579947895852327361,finish=1579947895855364292,duration=3036931,event=update_glibc[0Ktravis_time:start:2241a6e6[0Ktravis_time:end:2241a6e6:start=1579947895858911684,finish=1579947895870905260,duration=11993576,event=clean_up_path[0Ktravis_time:start:001c0d4c[0Ktravis_time:end:001c0d4c:start=1579947895874322444,finish=1579947895881309795,duration=6987351,event=fix_resolv_conf[0Ktravis_time:start:042755ac[0Ktravis_time:end:042755ac:start=1579947895884855053,finish=1579947895893110813,duration=8255760,event=fix_etc_hosts[0Ktravis_time:start:08cc02be[0Ktravis_time:end:08cc02be:start=1579947895897732912,finish=1579947895904824980,duration=7092068,event=fix_mvn_settings_xml[0Ktravis_time:start:3a77812a[0Ktravis_time:end:3a77812a:start=1579947895909836854,finish=1579947895919253470,duration=9416616,event=no_ipv6_localhost[0Ktravis_time:start:00c4e6d6[0Ktravis_time:end:00c4e6d6:start=1579947895923453067,finish=1579947895925516265,duration=2063198,event=fix_etc_mavenrc[0Ktravis_time:start:28248f74[0Ktravis_time:end:28248f74:start=1579947895929312892,finish=1579947895932148528,duration=2835636,event=fix_wwdr_certificate[0Ktravis_time:start:00920ddc[0Ktravis_time:end:00920ddc:start=1579947895938301562,finish=1579947895959134596,duration=20833034,event=put_localhost_first[0Ktravis_time:start:01038594[0Ktravis_time:end:01038594:start=1579947895963057928,finish=1579947895966296937,duration=3239009,event=home_paths[0Ktravis_time:start:093cba0f[0Ktravis_time:end:093cba0f:start=1579947895970145130,finish=1579947895980780180,duration=10635050,event=disable_initramfs[0Ktravis_time:start:1ff52d70[0Ktravis_time:end:1ff52d70:start=1579947895984854525,finish=1579947896153711820,duration=168857295,event=disable_ssh_roaming[0Ktravis_time:start:0a4597a5[0Ktravis_time:end:0a4597a5:start=1579947896157917261,finish=1579947896160667613,duration=2750352,event=debug_tools[0Ktravis_time:start:014a1c02[0Ktravis_time:end:014a1c02:start=1579947896166625923,finish=1579947896169473462,duration=2847539,event=uninstall_oclint[0Ktravis_time:start:0aa2e11a[0Ktravis_time:end:0aa2e11a:start=1579947896173277019,finish=1579947896175924129,duration=2647110,event=rvm_use[0Ktravis_time:start:04f5d600[0Ktravis_time:end:04f5d600:start=1579947896179389165,finish=1579947896188228676,duration=8839511,event=rm_etc_boto_cfg[0Ktravis_time:start:056de430[0Ktravis_time:end:056de430:start=1579947896192219662,finish=1579947896194531360,duration=2311698,event=rm_oraclejdk8_symlink[0Ktravis_time:start:02417468[0Ktravis_time:end:02417468:start=1579947896198790129,finish=1579947896241814927,duration=43024798,event=enable_i386[0Ktravis_time:start:017e8c0f[0Ktravis_time:end:017e8c0f:start=1579947896245720522,finish=1579947896249102463,duration=3381941,event=update_rubygems[0Ktravis_time:start:043c6020[0Ktravis_time:end:043c6020:start=1579947896253908037,finish=1579947897068068038,duration=814160001,event=ensure_path_components[0Ktravis_time:start:09a5e190[0Ktravis_time:end:09a5e190:start=1579947897072222122,finish=1579947897074742338,duration=2520216,event=redefine_curl[0Ktravis_time:start:08ff5368[0Ktravis_time:end:08ff5368:start=1579947897080320233,finish=1579947897124042889,duration=43722656,event=nonblock_pipe[0Ktravis_time:start:10be16c3[0Ktravis_time:end:10be16c3:start=1579947897128241153,finish=1579947903157405583,duration=6029164430,event=apt_get_update[0Ktravis_time:start:088fee3c[0Ktravis_time:end:088fee3c:start=1579947903161145804,finish=1579947903163427583,duration=2281779,event=deprecate_xcode_64[0Ktravis_time:start:21e32eb8[0Ktravis_time:end:21e32eb8:start=1579947903166423106,finish=1579947906531333820,duration=3364910714,event=update_heroku[0Ktravis_time:start:08ff46de[0Ktravis_time:end:08ff46de:start=1579947906535945095,finish=1579947906538518136,duration=2573041,event=shell_session_update[0Ktravis_time:start:269e8fdb[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3905
travis_fold:end:docker_mtu[0Ktravis_time:end:269e8fdb:start=1579947906542695418,finish=1579947907723387062,duration=1180691644,event=set_docker_mtu[0Ktravis_time:start:24599564[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:24599564:start=1579947907726282279,finish=1579947907776641353,duration=50359074,event=resolvconf[0Ktravis_time:start:14a37b03[0Ktravis_time:end:14a37b03:start=1579947907779605555,finish=1579947907850523267,duration=70917712,event=maven_central_mirror[0Ktravis_time:start:03c4a082[0Ktravis_time:end:03c4a082:start=1579947907854334218,finish=1579947907919352122,duration=65017904,event=maven_https[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:02cd6296[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:02cd6296:start=1579947907988076898,finish=1579947908310668916,duration=322592018,event=configure[0Ktravis_time:start:02f684e0[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:02f684e0:start=1579947908315599420,finish=1579947916093915667,duration=7778316247,event=configure[0Ktravis_time:start:03c08e6a[0Ktravis_fold:start:services[0Ktravis_time:start:020aec50[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:020aec50:start=1579947916115313611,finish=1579947916127439941,duration=12126330,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:020aec50:start=1579947916115313611,finish=1579947919132943758,duration=3017630147,event=services[0Ktravis_time:start:1050b884[0Ktravis_time:end:1050b884:start=1579947919137120527,finish=1579947919139455234,duration=2334707,event=fix_ps4[0Ktravis_time:start:173446dc[0K
travis_fold:start:git.checkout[0Ktravis_time:start:18849c58[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:18849c58:start=1579947919147337843,finish=1579947924303615926,duration=5156278083,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:0c181700[0K$ git fetch origin +refs/pull/147/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/147/merge -> FETCH_HEAD
travis_time:end:0c181700:start=1579947924309185088,finish=1579947924679334343,duration=370149255,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:0c181700:start=1579947924309185088,finish=1579947924928243015,duration=619057927,event=checkout[0Ktravis_time:start:178c0214[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:178c0214:start=1579947924932519547,finish=1579947924943856139,duration=11336592,event=env[0Ktravis_time:start:236359aa[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:236359aa:start=1579947924948729637,finish=1579947924953888626,duration=5158989,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:095705e0[0K$ python system_testing.py -s of-ccx
networks:
  [secure]comm: {}
services:
  calculix-adapter-solid:
    command: '/bin/bash -c "ln -s /home/[secure]/Data/Input/ Solid && ln -sf configs/*
      .  && ccx_preCICE -i Solid/solid -[secure]-participant Solid"

      '
    container_name: calculix-adapter-solid
    depends_on:
    - tutorial-data
    image: [secure]/calculix-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
    - solid_input:/home/[secure]/Data/Input:rw
    - configs:/home/[secure]/calculix-adapter/configs:rw
  openfoam-adapter-inner:
    command: "/bin/bash -c \"source /opt/openfoam4/etc/bashrc  && ln -sf configs/*\
      \ .  && buoyantSimpleFoam -case /home/[secure]/Data/Input && cp -r /home/[secure]/Data/Input/.\
      \ /home/[secure]/Data/Output/Inner-Fluid\" \n"
    container_name: openfoam-adapter-inner
    depends_on:
    - tutorial-data
    image: [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
    - inner_fluid_input:/home/[secure]/Data/Input:rw
    - configs:/home/[secure]/openfoam-adapter/configs:rw
  openfoam-adapter-outer:
    command: "/bin/bash -c \"source /opt/openfoam4/etc/bashrc && ln -sf configs/*\
      \ .  && buoyantSimpleFoam -case /home/[secure]/Data/Input && cp -r /home/[secure]/Data/Input/.\
      \ /home/[secure]/Data/Output/Outer-Fluid\" \n"
    container_name: openfoam-adapter-outer
    depends_on:
    - tutorial-data
    image: [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
    - outer_fluid_input:/home/[secure]/Data/Input:rw
    - configs:/home/[secure]/openfoam-adapter/configs:rw
  tutorial-data:
    build:
      context: /home/travis/build/[secure]/systemtests/tests/TestCompose_of-ccx
      dockerfile: Dockerfile.tutorial_data
    container_name: tutorial-data
    volumes:
    - solid_input:/tutorials/CHT/heat_exchanger/buoyantSimpleFoam-CalculiX/Solid:rw
    - outer_fluid_input:/tutorials/CHT/heat_exchanger/buoyantSimpleFoam-CalculiX/Outer-Fluid:rw
    - inner_fluid_input:/tutorials/CHT/heat_exchanger/buoyantSimpleFoam-CalculiX/Inner-Fluid:rw
    - configs:/configs:rw
    - output:/Output:rw
version: '3.0'
volumes:
  configs: {}
  exchange: {}
  inner_fluid_input: {}
  outer_fluid_input: {}
  output: {}
  solid_input: {}

Creating network "testcomposeofccx_default" with the default driver
Creating network "testcomposeofccx_[secure]comm" with the default driver
Creating volume "testcomposeofccx_exchange" with default driver
Creating volume "testcomposeofccx_solid_input" with default driver
Creating volume "testcomposeofccx_inner_fluid_input" with default driver
Creating volume "testcomposeofccx_output" with default driver
Creating volume "testcomposeofccx_configs" with default driver
Creating volume "testcomposeofccx_outer_fluid_input" with default driver
Building tutorial-data
Step 1/14 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/14 : ENV tutorial_path /tutorials/CHT/heat_exchanger/buoyantSimpleFoam-CalculiX
 ---> Running in 4419e7ce4bd5
 ---> d9c35f10ae2f
Removing intermediate container 4419e7ce4bd5
Step 3/14 : RUN apk add git bash
 ---> Running in fd2530e56140
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
(1/11) Installing ncurses-terminfo-base (6.1_p20191130-r0)
(2/11) Installing ncurses-terminfo (6.1_p20191130-r0)
(3/11) Installing ncurses-libs (6.1_p20191130-r0)
(4/11) Installing readline (8.0.1-r0)
(5/11) Installing bash (5.0.11-r1)
Executing bash-5.0.11-r1.post-install
(6/11) Installing ca-certificates (20191127-r0)
(7/11) Installing nghttp2-libs (1.40.0-r0)
(8/11) Installing libcurl (7.67.0-r0)
(9/11) Installing expat (2.2.9-r1)
(10/11) Installing pcre2 (10.34-r1)
(11/11) Installing git (2.24.1-r0)
Executing busybox-1.31.1-r9.trigger
Executing ca-certificates-20191127-r0.trigger
OK: 31 MiB in 25 packages
 ---> 335c6c7c0f50
Removing intermediate container fd2530e56140
Step 4/14 : ARG branch=develop
 ---> Running in f53fc6f77781
 ---> 126219cdc04e
Removing intermediate container f53fc6f77781
Step 5/14 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in 7557173750f0
[91mCloning into 'tutorials'...
[0m ---> 98a53aacad4d
Removing intermediate container 7557173750f0
Step 6/14 : COPY controlDict $tutorial_path/Inner-Fluid/system/controlDict
 ---> 8008bf4f0825
Step 7/14 : COPY controlDict $tutorial_path/Outer-Fluid/system/controlDict
 ---> 2c0a49c7e4d7
Step 8/14 : COPY [secure]-config.xml configs/[secure]-config.xml
 ---> 4c1954ba4fc9
Step 9/14 : WORKDIR $tutorial_path
 ---> db9bf0090179
Removing intermediate container b8a66cf14b48
Step 10/14 : RUN bash ./Download_meshes &&     cp -r Inner-Fluid/constant/polyMesh.org Inner-Fluid/constant/polyMesh &&     cp -r Outer-Fluid/constant/polyMesh.org Outer-Fluid/constant/polyMesh
 ---> Running in 1079d4127668
This tutorial is based on a case prepared with SimScale.
Since the mesh files are several MB large, we don't store them in the Git repository.
This script downloads and extracts the missing files.

Downloading the Solid case...
[91mConnecting to syncandshare.lrz.de (129.187.255.213:443)
[0m[91mwriting to stdout
[0m[91m-                      1% |                                | 16384  0:01:38 ETA
[0mSolid/solid.inp
[91m-                     33% |**********                      |  531k  0:00:03 ETA
[0m[91m-                     69% |**********************          | 1098k  0:00:01 ETA
[0m[91m-                    100% |********************************| 1592k  0:00:00 ETA
written to stdout
[0mSolid/outer-interface.sur
Solid/adiabatic.dfl
Solid/inner-interface.sur
Solid/outer-interface.nam
Solid/inner-interface.nam
Solid/
Solid/outer-interface.flm
Solid/inner-interface.flm
Solid/all.msh
Downloading and extracting the Inner-Fluid mesh...
[91mConnecting to syncandshare.lrz.de (129.187.255.213:443)
[0m[91mwriting to stdout
[0mpolyMesh.org/boundary
[91m-                      1% |                                |  215k  0:01:07 ETA
[0m[91m-                      4% |*                               |  659k  0:00:42 ETA
[0m[91m-                      8% |**                              | 1217k  0:00:33 ETA
[0m[91m-                     12% |****                            | 1856k  0:00:27 ETA
[0m[91m-                     16% |*****                           | 2415k  0:00:25 ETA
[0m[91m-                     20% |******                          | 3048k  0:00:22 ETA
[0m[91m-                     24% |*******                         | 3621k  0:00:21 ETA
[0m[91m-                     28% |*********                       | 4177k  0:00:20 ETA
[0m[91m-                     32% |**********                      | 4818k  0:00:18 ETA
[0m[91m-                     33% |**********                      | 4911k  0:00:19 ETA
[0m[91m-                     35% |***********                     | 5284k  0:00:19 ETA
[0m[91m-                     39% |************                    | 5856k  0:00:18 ETA
[0m[91m-                     43% |*************                   | 6428k  0:00:16 ETA
[0m[91m-                     47% |***************                 | 7050k  0:00:15 ETA
[0m[91m-                     51% |****************                | 7625k  0:00:13 ETA
[0m[91m-                     55% |*****************               | 8193k  0:00:12 ETA
[0m[91m-                     59% |*******************             | 8818k  0:00:11 ETA
[0m[91m-                     63% |********************            | 9388k  0:00:10 ETA
[0m[91m-                     68% |*********************           |  9.7M  0:00:08 ETA
[0m[91m-                     68% |**********************          |  9.8M  0:00:09 ETA
[0m[91m-                     71% |**********************          | 10.2M  0:00:08 ETA
[0m[91m-                     74% |***********************         | 10.7M  0:00:07 ETA
[0m[91m-                     78% |*************************       | 11.2M  0:00:06 ETA
[0m[91m-                     82% |**************************      | 11.8M  0:00:05 ETA
[0m[91m-                     86% |***************************     | 12.4M  0:00:03 ETA
[0m[91m-                     90% |****************************    | 13.0M  0:00:02 ETA
[0m[91m-                     94% |******************************  | 13.6M  0:00:01 ETA
[0m[91m-                     98% |******************************* | 14.1M  0:00:00 ETA
[0m[91m-                    100% |********************************| 14.3M[0m[91m  0:00:00 ETA
written to stdout
[0mpolyMesh.org/neighbour.gz
polyMesh.org/points.gz
polyMesh.org/cellZones.gz
polyMesh.org/owner.gz
polyMesh.org/pointZones.gz
polyMesh.org/faceZones.gz
polyMesh.org/faces.gz
polyMesh.org/blockMeshDict
polyMesh.org/
Downloading and extracting the Outer-Fluid mesh...
[91mConnecting to syncandshare.lrz.de (129.187.255.213:443)
[0m[91mwriting to stdout
[0mpolyMesh.org/boundary
[91m-                      0% |                                |  246k  0:01:42 ETA
[0m[91m-                      3% |*                               |  832k  0:00:59 ETA
[0m[91m-                      5% |*                               | 1440k  0:00:50 ETA
[0m[91m-                      7% |**                              | 2027k  0:00:46 ETA
[0m[91m-                     10% |***                             | 2598k  0:00:44 ETA
[0m[91m-                     12% |***                             | 3200k  0:00:42 ETA
[0m[91m-                     14% |****                            | 3801k  0:00:40 ETA
[0m[91m-                     17% |*****                           | 4401k  0:00:38 ETA
[0m[91m-                     19% |******                          | 4995k  0:00:37 ETA
[0m[91m-                     21% |******                          | 5567k  0:00:36 ETA
[0m[91m-                     24% |*******                         | 6165k  0:00:34 ETA
[0m[91m-                     26% |********                        | 6766k  0:00:33 ETA
[0m[91m-                     28% |*********                       | 7331k  0:00:32 ETA
[0m[91m-                     30% |*********                       | 7939k  0:00:31 ETA
[0m[91m-                     33% |**********                      | 8525k  0:00:30 ETA
[0m[91m-                     35% |***********                     | 9133k  0:00:28 ETA
[0m[91m-                     37% |************                    | 9722k  0:00:27 ETA
[0m[91m-                     40% |************                    | 10.0M  0:00:26 ETA
[0m[91m-                     42% |*************                   | 10.6M  0:00:25 ETA
[0m[91m-                     44% |**************                  | 11.2M  0:00:24 ETA
[0m[91m-                     47% |***************                 | 11.7M  0:00:23 ETA
[0m[91m-                     49% |***************                 | 12.3M  0:00:22 ETA
[0m[91m-                     51% |****************                | 12.9M  0:00:21 ETA
[0m[91m-                     54% |*****************               | 13.5M  0:00:20 ETA
[0m[91m-                     56% |******************              | 14.1M  0:00:19 ETA
[0m[91m-                     58% |******************              | 14.6M  0:00:18 ETA
[0m[91m-                     60% |*******************             | 15.2M  0:00:17 ETA
[0m[91m-                     63% |********************            | 15.8M  0:00:16 ETA
[0m[91m-                     65% |********************            | 16.3M  0:00:15 ETA
[0m[91m-                     67% |*********************           | 16.9M  0:00:14 ETA
[0m[91m-                     70% |**********************          | 17.5M  0:00:13 ETA
[0m[91m-                     72% |***********************         | 18.1M  0:00:12 ETA
[0m[91m-                     74% |***********************         | 18.7M  0:00:11 ETA
[0m[91m-                     77% |************************        | 19.2M  0:00:10 ETA
[0m[91m-                     79% |*************************       | 19.8M  0:00:09 ETA
[0m[91m-                     81% |**************************      | 20.4M  0:00:08 ETA
[0m[91m-                     83% |**************************      | 21.0M  0:00:07 ETA
[0m[91m-                     86% |***************************     | 21.6M  0:00:06 ETA
[0m[91m-                     87% |***************************     | 21.7M  0:00:05 ETA
[0m[91m-                     88% |****************************    | 22.1M[0m[91m  0:00:05 ETA[0m[91m
[0m[91m-                     90% |****************************    | 22.5M  0:00:04 ETA
[0m[91m-                     92% |*****************************   | 23.1M  0:00:03 ETA
[0m[91m-                     94% |******************************  | 23.7M  0:00:02 ETA
[0m[91m-                     97% |******************************* | 24.3M  0:00:01 ETA
[0m[91m-                     99% |******************************* | 24.8M  0:00:00 ETA
[0m[91m-                    100% |********************************| 25.0M  0:00:00 ETA
written to stdout
[0mpolyMesh.org/neighbour.gz
polyMesh.org/points.gz
polyMesh.org/cellZones.gz
polyMesh.org/owner.gz
polyMesh.org/pointZones.gz
polyMesh.org/faceZones.gz
polyMesh.org/faces.gz
polyMesh.org/blockMeshDict
polyMesh.org/
Completed.
 ---> a4f20e748448
Removing intermediate container 1079d4127668
Step 11/14 : WORKDIR /
 ---> 4428a6257be1
Removing intermediate container 7f5c9f3c9a89
Step 12/14 : RUN sed -i 's|exchange-directory\="."|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'     configs/[secure]-config.xml && cp $tutorial_path/config.yml  configs/config.yml
 ---> Running in c8667415f311
 ---> 9487d7eb1faf
Removing intermediate container c8667415f311
Step 13/14 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 26026fca1505
 ---> 83ff63719eaf
Removing intermediate container 26026fca1505
Step 14/14 : USER [secure]
 ---> Running in 35847b54352a
 ---> 41860b654cde
Removing intermediate container 35847b54352a
Successfully built 41860b654cde
Successfully tagged testcomposeofccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling openfoam-adapter-outer ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:def31d1013d65c817c17d7798573862b7a630e67d5d5ba870507c83d187b879c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Pulling calculix-adapter-solid ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:eed3979fbded39e8a23ede0f432ef6f195727d13ee124bb42462ecca63a1b1fe
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating openfoam-adapter-outer ... 
Creating calculix-adapter-solid ... 
Creating openfoam-adapter-inner ... 
Creating openfoam-adapter-outer
Creating openfoam-adapter-inner
Creating calculix-adapter-solid
[1A[2KCreating openfoam-adapter-inner ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-outer ... [32mdone[0m[1B[1A[2KCreating calculix-adapter-solid ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient

```
