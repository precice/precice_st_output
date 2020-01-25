```
travis_fold:start:worker_info[0K[33;1mWorker information[0m
hostname: 8b5f0c21-a087-41e4-a083-acd34b3d7522@1.worker-org-78ccbd844c-vch4n.gce-production-1
version: v6.2.6 https://github.com/travis-ci/worker/tree/ba21bd30589fd152126e13df30e0cc78ccdf2837
instance: travis-job-397a36ff-482f-4b25-b093-2a27bb73f477 travis-ci-garnet-trusty-1512502259-986baf0 (via amqp)
startup: 6.294090658s
travis_fold:end:worker_info[0Ktravis_time:start:1955aed0[0Ktravis_time:end:1955aed0:start=1579947896941938742,finish=1579947897093163442,duration=151224700,event=no_world_writable_dirs[0Ktravis_time:start:01078272[0Ktravis_time:end:01078272:start=1579947897095924679,finish=1579947897100625664,duration=4700985,event=setup_filter[0Ktravis_time:start:125cf040[0Ktravis_time:end:125cf040:start=1579947897104081038,finish=1579947897111078256,duration=6997218,event=agent[0Ktravis_time:start:00926886[0Ktravis_time:end:00926886:start=1579947897113592698,finish=1579947897115386570,duration=1793872,event=check_unsupported[0Ktravis_time:start:070ce464[0Ktravis_fold:start:system_info[0K[33;1mBuild system information[0m
Build language: python
Build group: stable
Build dist: trusty
Build id: 641687652
Job id: 641687653
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
travis_time:end:070ce464:start=1579947897117912747,finish=1579947897123219560,duration=5306813,event=show_system_info[0Ktravis_time:start:2f754ac7[0Ktravis_time:end:2f754ac7:start=1579947897125869015,finish=1579947897149646961,duration=23777946,event=rm_riak_source[0Ktravis_time:start:12da773a[0Ktravis_time:end:12da773a:start=1579947897153152591,finish=1579947897159473145,duration=6320554,event=fix_rwky_redis[0Ktravis_time:start:07c705b7[0Ktravis_time:end:07c705b7:start=1579947897162245010,finish=1579947897592063642,duration=429818632,event=wait_for_network[0Ktravis_time:start:34ed1d48[0Ktravis_time:end:34ed1d48:start=1579947897596614123,finish=1579947898753514337,duration=1156900214,event=update_apt_keys[0Ktravis_time:start:0f726a1a[0Ktravis_time:end:0f726a1a:start=1579947898756691679,finish=1579947899742038214,duration=985346535,event=fix_hhvm_source[0Ktravis_time:start:00ebe810[0Ktravis_time:end:00ebe810:start=1579947899745815190,finish=1579947899754078044,duration=8262854,event=update_mongo_arch[0Ktravis_time:start:04c04a7f[0Ktravis_time:end:04c04a7f:start=1579947899758150814,finish=1579947899792198928,duration=34048114,event=fix_sudo_enabled_trusty[0Ktravis_time:start:1027f7d0[0Ktravis_time:end:1027f7d0:start=1579947899796140859,finish=1579947899798358089,duration=2217230,event=update_glibc[0Ktravis_time:start:32e8fcae[0Ktravis_time:end:32e8fcae:start=1579947899802036209,finish=1579947899810143110,duration=8106901,event=clean_up_path[0Ktravis_time:start:035efad8[0Ktravis_time:end:035efad8:start=1579947899813651641,finish=1579947899820845740,duration=7194099,event=fix_resolv_conf[0Ktravis_time:start:03912566[0Ktravis_time:end:03912566:start=1579947899824366861,finish=1579947899832612098,duration=8245237,event=fix_etc_hosts[0Ktravis_time:start:12ea5f80[0Ktravis_time:end:12ea5f80:start=1579947899835595382,finish=1579947899843292464,duration=7697082,event=fix_mvn_settings_xml[0Ktravis_time:start:001e2d60[0Ktravis_time:end:001e2d60:start=1579947899846872668,finish=1579947899855204276,duration=8331608,event=no_ipv6_localhost[0Ktravis_time:start:0b8fac64[0Ktravis_time:end:0b8fac64:start=1579947899859191150,finish=1579947899862391653,duration=3200503,event=fix_etc_mavenrc[0Ktravis_time:start:04c45b06[0Ktravis_time:end:04c45b06:start=1579947899866303214,finish=1579947899870258504,duration=3955290,event=fix_wwdr_certificate[0Ktravis_time:start:0fb3dc23[0Ktravis_time:end:0fb3dc23:start=1579947899878411189,finish=1579947899898757249,duration=20346060,event=put_localhost_first[0Ktravis_time:start:3580b4e0[0Ktravis_time:end:3580b4e0:start=1579947899902476240,finish=1579947899905753715,duration=3277475,event=home_paths[0Ktravis_time:start:07c8cbdc[0Ktravis_time:end:07c8cbdc:start=1579947899909785257,finish=1579947899923366405,duration=13581148,event=disable_initramfs[0Ktravis_time:start:116b0c0e[0Ktravis_time:end:116b0c0e:start=1579947899926925626,finish=1579947900162833361,duration=235907735,event=disable_ssh_roaming[0Ktravis_time:start:1be11ea8[0Ktravis_time:end:1be11ea8:start=1579947900166518151,finish=1579947900169215847,duration=2697696,event=debug_tools[0Ktravis_time:start:01515e6a[0Ktravis_time:end:01515e6a:start=1579947900173321799,finish=1579947900177254159,duration=3932360,event=uninstall_oclint[0Ktravis_time:start:1a855fb0[0Ktravis_time:end:1a855fb0:start=1579947900181340205,finish=1579947900184916817,duration=3576612,event=rvm_use[0Ktravis_time:start:1d1836d4[0Ktravis_time:end:1d1836d4:start=1579947900188255749,finish=1579947900196719222,duration=8463473,event=rm_etc_boto_cfg[0Ktravis_time:start:06b203c8[0Ktravis_time:end:06b203c8:start=1579947900200341466,finish=1579947900203201577,duration=2860111,event=rm_oraclejdk8_symlink[0Ktravis_time:start:01d3b253[0Ktravis_time:end:01d3b253:start=1579947900207270856,finish=1579947900255871967,duration=48601111,event=enable_i386[0Ktravis_time:start:2a94d8b6[0Ktravis_time:end:2a94d8b6:start=1579947900260152956,finish=1579947900263964637,duration=3811681,event=update_rubygems[0Ktravis_time:start:04392b40[0Ktravis_time:end:04392b40:start=1579947900268055149,finish=1579947901113033594,duration=844978445,event=ensure_path_components[0Ktravis_time:start:0050edd0[0Ktravis_time:end:0050edd0:start=1579947901117077657,finish=1579947901119349183,duration=2271526,event=redefine_curl[0Ktravis_time:start:0247e762[0Ktravis_time:end:0247e762:start=1579947901123215876,finish=1579947901165836903,duration=42621027,event=nonblock_pipe[0Ktravis_time:start:19853ac6[0Ktravis_time:end:19853ac6:start=1579947901169790223,finish=1579947907196773385,duration=6026983162,event=apt_get_update[0Ktravis_time:start:1c450040[0Ktravis_time:end:1c450040:start=1579947907200402896,finish=1579947907202731668,duration=2328772,event=deprecate_xcode_64[0Ktravis_time:start:2aa84956[0Ktravis_time:end:2aa84956:start=1579947907205818394,finish=1579947910832181519,duration=3626363125,event=update_heroku[0Ktravis_time:start:0303746e[0Ktravis_time:end:0303746e:start=1579947910836466720,finish=1579947910839045892,duration=2579172,event=shell_session_update[0Ktravis_time:start:0addbc84[0Ktravis_fold:start:docker_mtu[0Kdocker stop/waiting
docker start/running, process 3975
travis_fold:end:docker_mtu[0Ktravis_time:end:0addbc84:start=1579947910842497372,finish=1579947912019343554,duration=1176846182,event=set_docker_mtu[0Ktravis_time:start:22a3b740[0Ktravis_fold:start:resolvconf[0Kresolvconf stop/waiting
resolvconf start/running
travis_fold:end:resolvconf[0Ktravis_time:end:22a3b740:start=1579947912023196888,finish=1579947912075859410,duration=52662522,event=resolvconf[0Ktravis_time:start:00728dc0[0Ktravis_time:end:00728dc0:start=1579947912079814570,finish=1579947912158034990,duration=78220420,event=maven_central_mirror[0Ktravis_time:start:005fec28[0Ktravis_time:end:005fec28:start=1579947912162242485,finish=1579947912221834381,duration=59591896,event=maven_https[0K[33;1m3.5 is not installed; attempting download[0m
[33;1mDownloading archive: https://storage.googleapis.com/travis-ci-language-archives/python/binaries/ubuntu/14.04/x86_64/python-3.5.tar.bz2[0m
travis_time:start:0c30bfa6[0K$ curl -sSf --retry 5 -o python-3.5.tar.bz2 ${archive_url}
travis_time:end:0c30bfa6:start=1579947912290854176,finish=1579947913506715307,duration=1215861131,event=configure[0Ktravis_time:start:019e2d00[0K$ sudo tar xjf python-3.5.tar.bz2 --directory /
travis_time:end:019e2d00:start=1579947913511236368,finish=1579947921349392531,duration=7838156163,event=configure[0Ktravis_time:start:044ac31a[0Ktravis_fold:start:services[0Ktravis_time:start:25c20630[0K$ sudo service docker start
start: Job is already running: docker
travis_time:end:25c20630:start=1579947921372568338,finish=1579947921385442695,duration=12874357,event=prepare[0Ktravis_fold:end:services[0Ktravis_time:end:25c20630:start=1579947921372568338,finish=1579947924390886322,duration=3018317984,event=services[0Ktravis_time:start:14404d22[0Ktravis_time:end:14404d22:start=1579947924395280132,finish=1579947924397956771,duration=2676639,event=fix_ps4[0Ktravis_time:start:187d115c[0K
travis_fold:start:git.checkout[0Ktravis_time:start:2b917864[0K$ git clone --depth=50 https://github.com/[secure]/systemtests.git [secure]/systemtests
Cloning into '[secure]/systemtests'...
travis_time:end:2b917864:start=1579947924406319853,finish=1579947929756387431,duration=5350067578,event=checkout[0K$ cd [secure]/systemtests
travis_time:start:00b89248[0K$ git fetch origin +refs/pull/147/merge:
From https://github.com/[secure]/systemtests
 * branch            refs/pull/147/merge -> FETCH_HEAD
travis_time:end:00b89248:start=1579947929760979545,finish=1579947930214316844,duration=453337299,event=checkout[0K$ git checkout -qf FETCH_HEAD
travis_fold:end:git.checkout[0K
travis_time:end:00b89248:start=1579947929760979545,finish=1579947930927200261,duration=1166220716,event=checkout[0Ktravis_time:start:0f7edd58[0K
[33;1mSetting environment variables from repository settings[0m
$ export DOCKER_PASSWORD=[secure]
$ export DOCKER_USERNAME=[secure]
$ export TRAVIS_ACCESS_TOKEN=[secure]
$ export PRECICE_BOT_EMAIL=[secure]
$ export GH_TOKEN=[secure]

travis_time:end:0f7edd58:start=1579947930932095391,finish=1579947930942719750,duration=10624359,event=env[0Ktravis_time:start:008c3ef8[0K$ source ~/virtualenv/python3.5/bin/activate
travis_time:end:008c3ef8:start=1579947930946528346,finish=1579947930951414536,duration=4886190,event=[0K$ python --version
Python 3.5.6
$ pip --version
pip 18.0 from /home/travis/virtualenv/python3.5.6/lib/python3.5/site-packages/pip (python 3.5)
Could not locate requirements.txt. Override the install: key in your .travis.yml to install dependencies.
travis_time:start:13102ab2[0K$ python system_testing.py -s su2-ccx
networks:
  [secure]comm: {}
services:
  calculix-adapter:
    command: '/bin/bash -c "ln -sf /home/[secure]/Data/Input Solid; ln -sf /home/[secure]/calculix-adapter/configs/*
      . && ccx_preCICE -i Solid/flap -[secure]-participant Calculix && cp   Solid/*.dat  Solid/*.cvg
      Solid/*.sta *.log *.out /home/[secure]/Data/Output/"

      '
    container_name: calculix-adapter
    depends_on:
    - tutorial-data
    image: [secure]/calculix-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
    - input_solid:/home/[secure]/Data/Input:rw
    - configs:/home/[secure]/calculix-adapter/configs:rw
  su2-adapter:
    command: "/bin/bash -c \"ln -sf /home/[secure]/Data/Input Fluid &&\n  ln -sf /home/[secure]/su2-adapter/configs/*\
      \ . &&\n  SU2_CFD Fluid/euler_config_coupled.cfg &&\n  cp flow*.vtk *.csv *.dat\
      \ *SU2*.log /home/[secure]/Data/Output/\"\n"
    container_name: su2-adapter
    depends_on:
    - tutorial-data
    image: [secure]/su2-adapter-ubuntu1604.home-develop:latest
    networks:
      [secure]comm: null
    volumes:
    - exchange:/home/[secure]/Data/Exchange:rw
    - output:/home/[secure]/Data/Output:rw
    - input_fluid:/home/[secure]/Data/Input:rw
    - configs:/home/[secure]/su2-adapter/configs:rw
  tutorial-data:
    build:
      context: /home/travis/build/[secure]/systemtests/tests/TestCompose_su2-ccx
      dockerfile: Dockerfile.tutorial_data
    container_name: tutorial-data
    volumes:
    - input_solid:/tutorials/FSI/flap_perp/SU2-CalculiX/Solid:rw
    - input_fluid:/tutorials/FSI/flap_perp/SU2-CalculiX/Fluid:rw
    - configs:/configs:rw
    - output:/Output:rw
version: '3.0'
volumes:
  configs: {}
  exchange: {}
  input_fluid: {}
  input_solid: {}
  output: {}

Creating network "testcomposesu2ccx_default" with the default driver
Creating network "testcomposesu2ccx_[secure]comm" with the default driver
Creating volume "testcomposesu2ccx_output" with default driver
Creating volume "testcomposesu2ccx_configs" with default driver
Creating volume "testcomposesu2ccx_input_solid" with default driver
Creating volume "testcomposesu2ccx_input_fluid" with default driver
Creating volume "testcomposesu2ccx_exchange" with default driver
Building tutorial-data
Step 1/10 : FROM alpine
latest: Pulling from library/alpine
Digest: sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d
Status: Downloaded newer image for alpine:latest
 ---> e7d92cdc71fe
Step 2/10 : ENV tutorial_path tutorials/FSI/flap_perp/SU2-CalculiX
 ---> Running in f073aa997452
 ---> 922d7266f000
Removing intermediate container f073aa997452
Step 3/10 : RUN apk add git bash
 ---> Running in 7bd8089484bd
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
 ---> 906045ed9587
Removing intermediate container 7bd8089484bd
Step 4/10 : ARG branch=develop
 ---> Running in 28d6fe7940d8
 ---> 59663e71ac2d
Removing intermediate container 28d6fe7940d8
Step 5/10 : RUN git clone --branch $branch https://github.com/[secure]/tutorials
 ---> Running in d0f79c5a2b0c
[91mCloning into 'tutorials'...
[0m ---> 4f42f2be37b7
Removing intermediate container d0f79c5a2b0c
Step 6/10 : RUN mkdir configs && sed -e 's|exchange-directory="../"|exchange-directory="/home/[secure]/Data/Exchange/" network="eth0"|g'    $tutorial_path/[secure]-config.xml  > configs/[secure]-config.xml
 ---> Running in 95e7bd70cabd
 ---> 7d343c1fba31
Removing intermediate container 95e7bd70cabd
Step 7/10 : RUN rm $tutorial_path/[secure]-config.xml
 ---> Running in dca4bcd3c391
 ---> 7d4958cdb799
Removing intermediate container dca4bcd3c391
Step 8/10 : RUN cp $tutorial_path/config.yml configs/
 ---> Running in ba939b5cf650
 ---> cecafe9a7913
Removing intermediate container ba939b5cf650
Step 9/10 : RUN addgroup -g 1000 [secure] && adduser -u 1000 -G [secure] -D [secure] && chown -R [secure]:[secure] tutorials configs
 ---> Running in 40afd3fa665a
 ---> e2080a48b481
Removing intermediate container 40afd3fa665a
Step 10/10 : USER [secure]
 ---> Running in fbbd4f4889e3
 ---> 78712dbf47b6
Removing intermediate container fbbd4f4889e3
Successfully built 78712dbf47b6
Successfully tagged testcomposesu2ccx_tutorial-data:latest
Image for service tutorial-data was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling calculix-adapter ([secure]/calculix-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/calculix-adapter-ubuntu1604.home-develop
Digest: sha256:eed3979fbded39e8a23ede0f432ef6f195727d13ee124bb42462ecca63a1b1fe
Status: Downloaded newer image for [secure]/calculix-adapter-ubuntu1604.home-develop:latest
Pulling su2-adapter ([secure]/su2-adapter-ubuntu1604.home-develop:latest)...
latest: Pulling from [secure]/su2-adapter-ubuntu1604.home-develop
Digest: sha256:148a65e6a226fb094545135eaf2d809db0a9e2ea819f1f171b3fa5e60f8ee190
Status: Downloaded newer image for [secure]/su2-adapter-ubuntu1604.home-develop:latest
Creating tutorial-data ... 
Creating tutorial-data
[1A[2KCreating tutorial-data ... [32mdone[0m[1BCreating su2-adapter ... 
Creating calculix-adapter ... 
Creating su2-adapter
Creating calculix-adapter
[1A[2KCreating su2-adapter ... [32mdone[0m[1B[1A[2KCreating calculix-adapter ... [32mdone[0m[1BRunning the simulation...Be patient
Running the simulation...Be patient
Running the simulation...Be patient
All adapters finished!
EXECUTING: export PRECICE_BASE=-ubuntu1604.home-develop; docker-compose config && bash ../../silent_compose.sh 
EXECUTING: docker cp tutorial-data:/Output .
EXECUTING: mkdir Logs && docker-compose logs > Logs/container-logs.md
TEST SUCCEEDED - No difference to referenceOutput found.
travis_time:end:13102ab2:start=1579947931225694785,finish=1579948233374584771,duration=302148889986,event=script[0K[32;1mThe command "python system_testing.py -s su2-ccx" exited with 0.[0m
travis_time:start:01422300[0K$ python push.py -t su2-ccx
Cloning into '[secure]_st_output'...

```
