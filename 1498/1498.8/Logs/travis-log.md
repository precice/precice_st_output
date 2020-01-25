```
travis_fold:start:worker_info[0K[33;1mWorker information[0m
hostname: 676a41c5-6a1e-4397-96bd-5bb938f43761@1.worker-org-847f45b8fd-7cdc5.gce-production-2
version: v6.2.6 https://github.com/travis-ci/worker/tree/ba21bd30589fd152126e13df30e0cc78ccdf2837
instance: travis-job-84921f0f-ef61-4040-ab36-ccb96672d57e travis-ci-garnet-trusty-1512502259-986baf0 (via amqp)
startup: 6.280946394s
travis_fold:end:worker_info[0Ktravis_time:start:0bd0b83e[0Ktravis_time:end:0bd0b83e:start=1579948097317199484,finish=1579948097464577341,duration=147377857,event=no_world_writable_dirs[0Ktravis_time:start:132877e6[0Ktravis_time:end:132877e6:start=1579948097467424643,finish=1579948097473418464,duration=5993821,event=setup_filter[0Ktravis_time:start:04ebf7cc[0Ktravis_time:end:04ebf7cc:start=1579948097476807109,finish=1579948097483710534,duration=6903425,event=agent[0Ktravis_time:start:118b7cf8[0Ktravis_time:end:118b7cf8:start=1579948097486249186,finish=1579948097488002243,duration=1753057,event=check_unsupported[0Ktravis_time:start:033185f0[0Ktravis_fold:start:system_info[0K[33;1mBuild system information[0m
Build language: python
Build group: stable
Build dist: trusty
Build id: 641687652
Job id: 641687660
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
travis_time:end:033185f0:start=1579948097491058406,finish=1579948097496041235,duration=4982829,event=show_system_info[0Ktravis_time:start:03c8f830[0Ktravis_time:end:03c8f830:start=1579948097498423484,finish=1579948097519073209,duration=20649725,event=rm_riak_source[0Ktravis_time:start:03677b1f[0Ktravis_time:end:03677b1f:start=1579948097521803108,finish=1579948097526366459,duration=4563351,event=fix_rwky_redis[0Ktravis_time:start:2aa58ca0[0Ktravis_time:end:2aa58ca0:start=1579948097529381664,finish=1579948097870198640,duration=340816976,event=wait_for_network[0Ktravis_time:start:1a06d9b4[0Ktravis_time:end:1a06d9b4:start=1579948097874482598,finish=1579948098898048839,duration=1023566241,event=update_apt_keys[0Ktravis_time:start:29253560[0Ktravis_time:end:29253560:start=1579948098902181570,finish=1579948099762214653,duration=860033083,event=fix_hhvm_source[0Ktravis_time:start:059bb4dd[0Ktravis_time:end:059bb4dd:start=1579948099766113539,finish=1579948099776430227,duration=10316688,event=update_mongo_arch[0Ktravis_time:start:025337fb[0Ktravis_time:end:025337fb:start=1579948099781747682,finish=1579948099818091394,duration=36343712,event=fix_sudo_enabled_trusty[0Ktravis_time:start:053c4b6c[0Ktravis_time:end:053c4b6c:start=1579948099822615344,finish=1579948099826676725,duration=4061381,event=update_glibc[0Ktravis_time:start:12246c0a[0Ktravis_time:end:12246c0a:start=1579948099830660878,finish=1579948099839933321,duration=9272443,event=clean_up_path[0Ktravis_time:start:22b95a21[0Ktravis_time:end:22b95a21:start=1579948099843405804,finish=1579948099852801851,duration=9396047,event=fix_resolv_conf[0Ktravis_time:start:15a79b4a[0Ktravis_time:end:15a79b4a:start=1579948099857079029,finish=1579948099867358632,duration=10279603,event=fix_etc_hosts[0Ktravis_time:start:028e6600[0Ktravis_time:end:028e6600:start=1579948099870950849,finish=1579948099878990549,duration=8039700,event=fix_mvn_settings_xml[0Ktravis_time:start:01fd8bb8[0Ktravis_time:end:01fd8bb8:start=1579948099882626684,finish=1579948099894287300,duration=11660616,event=no_ipv6_localhost[0Ktravis_time:start:0bf13b25[0Ktravis_time:end:0bf13b25:start=1579948099898313697,finish=1579948099900687633,duration=2373936,event=fix_etc_mavenrc[0Ktravis_time:start:06819ec9[0Ktravis_time:end:06819ec9:start=1579948099906766620,finish=1579948099909883383,duration=3116763,event=fix_wwdr_certificate[0Ktravis_time:start:188f56f6[0Ktravis_time:end:188f56f6:start=1579948099913842022,finish=1579948099934297213,duration=20455191,event=put_localhost_first[0Ktravis_time:start:1f1702b8[0Ktravis_time:end:1f1702b8:start=1579948099937717396,finish=1579948099941354503,duration=3637107,event=home_paths[0Ktravis_time:start:03c55d94[0Ktravis_time:end:03c55d94:start=1579948099945331856,finish=1579948099955954609,duration=10622753,event=disable_initramfs[0Ktravis_time:start:08686e88[0Ktravis_time:end:08686e88:start=1579948099959550281,finish=1579948100197407537,duration=237857256,event=disable_ssh_roaming[0Ktravis_time:start:2cb349df[0Ktravis_time:end:2cb349df:start=1579948100201338169,finish=1579948100204044453,duration=2706284,event=debug_tools[0Ktravis_time:start:000ea13a[0Ktravis_time:end:000ea13a:start=1579948100207616161,finish=1579948100211343060,duration=3726899,event=uninstall_oclint[0Ktravis_time:start:285a75fb[0Ktravis_time:end:285a75fb:start=1579948100215007650,finish=1579948100218635878,duration=3628228,event=rvm_use[0Ktravis_time:start:1037c9c4[0Ktravis_time:end:1037c9c4:start=1579948100221669479,finish=1579948100231073271,duration=9403792,event=rm_etc_boto_cfg[0Ktravis_time:start:1c3e30c2[0Ktravis_time:end:1c3e30c2:start=1579948100234528871,finish=1579948100237060847,duration=2531976,event=rm_oraclejdk8_symlink[0Ktravis_time:start:09381b34[0Ktravis_time:end:09381b34:start=1579948100240535554,finish=1579948100290229290,duration=49693736,event=enable_i386[0Ktravis_time:start:00be6b4e[0Ktravis_time:end:00be6b4e:start=1579948100294134374,finish=1579948100298190418,duration=4056044,event=update_rubygems[0Ktravis_time:start:018a6eaa[0Ktravis_time:end:018a6eaa:start=1579948100302171322,finish=1579948101142914523,duration=840743201,event=ensure_path_components[0Ktravis_time:start:1f81af5d[0Ktravis_time:end:1f81af5d:start=1579948101147471012,finish=1579948101150478727,duration=3007715,event=redefine_curl[0Ktravis_time:start:00ff8d12[0Ktravis_time:end:00ff8d12:start=1579948101154416719,finish=1579948101204251468,duration=49834749,event=nonblock_pipe[0Ktravis_time:start:00218f84[0Ktravis_time:end:00218f84:start=1579948101208633445,finish=1579948107238116098,duration=6029482653,event=apt_get_update[0Ktravis_time:start:32d6dfde[0Ktravis_time:end:32d6dfde:start=1579948107242729204,finish=1579948107245599608,duration=2870404,event=deprecate_xcode_64[0Ktravis_time:start:10fc1725[0Ktravis_time:end:10fc1725:start=1579948107249674124,finish=1579948110895116858,duration=3645442734,event=update_heroku[0Ktravis_time:start:02f4fbfa[0Ktravis_time:end:02f4fbfa:start=1579948110899075451,finish=1579948110901324932,duration=2249481,event=shell_session_update[0Ktravis_time:start:1de517f7[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3906
travis_fold:end:docker_mtu[0Ktravis_time:end:1de517f7:start=1579948110905135277,finish=1579948112099149941,duration=1194014664,event=set_docker_mtu[0Ktravis_time:start:20342493[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:20342493:start=1579948112102868947,finish=1579948112165355789,duration=62486842,event=resolvconf[0Ktravis_time:start:16734770[0Ktravis_time:end:16734770:start=1579948112168712871,finish=1579948112252825347,duration=84112476,event=maven_central_mirror[0Ktravis_time:start:12616b48[0Ktravis_time:end:12616b48:start=1579948112256829050,finish=1579948112316690775,duration=59861725,event=maven_https[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:198d10ee[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:198d10ee:start=1579948112383189755,finish=1579948112720438962,duration=337249207,event=configure[0Ktravis_time:start:01b8549d[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:01b8549d:start=1579948112725249484,finish=1579948120929041482,duration=8203791998,event=configure[0Ktravis_time:start:1d8e590a[0Ktravis_fold:start:services[0Ktravis_time:start:0c124a10[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:0c124a10:start=1579948120952858375,finish=1579948120965291652,duration=12433277,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:0c124a10:start=1579948120952858375,finish=1579948123971400252,duration=3018541877,event=services[0Ktravis_time:start:09504723[0Ktravis_time:end:09504723:start=1579948123975916063,finish=1579948123978713912,duration=2797849,event=fix_ps4[0Ktravis_time:start:0317d02e[0K
travis_fold:start:git.checkout[0Ktravis_time:start:0cbd6ba2[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:0cbd6ba2:start=1579948123987108575,finish=1579948129241219386,duration=5254110811,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:10f46c2a[0K$ git fetch origin +refs/pull/147/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/147/merge -> FETCH_HEAD
travis_time:end:10f46c2a:start=1579948129246618173,finish=1579948129636010588,duration=389392415,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:10f46c2a:start=1579948129246618173,finish=1579948129833679037,duration=587060864,event=checkout[0Ktravis_time:start:14fe2630[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:14fe2630:start=1579948129837942548,finish=1579948129845070173,duration=7127625,event=env[0Ktravis_time:start:242a0555[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:242a0555:start=1579948129848697152,finish=1579948129855370103,duration=6672951,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:03587994[0K$ python system_testing.py -s of-of_np
networks:
  [secure]comm: {}
services:
  openfoam-adapter-fluid:
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
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
    command: '/bin/bash -c "source /opt/openfoam4/etc/bashrc &&  cd /home/[secure]/openfoam-adapter/tutorials/CHT/flow-over-plate/buoyantPimpleFoam-laplacianFoam_nearest-projection
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

Creating network "testcomposeofofnp_default" with the default driver
Creating network "testcomposeofofnp_[secure]comm" with the default driver
Creating volume "testcomposeofofnp_output" with default driver
Creating volume "testcomposeofofnp_exchange" with default driver
Pulling tutorial-data (alpine:latest)...
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
Pulling openfoam-adapter-fluid ([secure]/openfoam-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/openfoam-adapter-ubuntu1604.home-develop
Digest: sha256:def31d1013d65c817c17d7798573862b7a630e67d5d5ba870507c83d187b879c
Status: Downloaded newer image for [secure]/openfoam-adapter-ubuntu1604.home-develop:latest
Creating openfoam-adapter-fluid ... 
Creating openfoam-adapter-solid ... 
Creating tutorial-data ... 
Creating openfoam-adapter-fluid
Creating tutorial-data
Creating openfoam-adapter-solid
[1A[2KCreating openfoam-adapter-solid ... [32mdone[0m[1B[1A[2KCreating tutorial-data ... [32mdone[0m[1B[1A[2KCreating openfoam-adapter-fluid ... [32mdone[0m[1BRunning the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: mkdir Logs && docker-compose logs > Logs/container-logs.md
EXECUTING: bash ../../compare_results.sh /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/referenceOutput /home/travis/build/[secure]/systemtests/tests/TestCompose_of-of_np/Output
TEST SUCCEEDED - Differences to referenceOutput within tolerance.
travis_time:end:03587994:start=1579948130127714270,finish=1579948259527251232,duration=129399536962,event=script[0K[32;1mThe command "python system_testing.py -s of-of_np" exited with 0.[0m
travis_time:start:0928bb55[0K$ python push.py -t of-of_np
Cloning into '[secure]_st_output'...

```
