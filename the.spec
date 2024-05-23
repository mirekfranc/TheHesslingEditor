Summary: The Hessling Editor
Name: the
Version: 3.4
Release: 4
License: GPLv2
Group: Applications/Editors
Source: THE-3.3RC4.tar.gz
URL: https://github.com/mirekfranc/TheHesslingEditor
Requires: ooRexx
BuildRequires: ooRexx-devel
BuildRequires: ncurses-devel

%description
THE is a full-screen character mode text editor based on the VM/CMS editor
XEDIT and many features of KEDIT written by Mansfield Software.

THE uses Rexx as its macro language which provides a rich and powerful
capability to extend THE.

This port executes in text mode and can be run from within an xterm window
or over a telnet connection. It requires ncurses to function.

For more information on THE, visit http://hessling-editor.sourceforge.net/

For more information on Rexx, visit http://www.rexxla.org
%prep

%setup -n THE-3.3RC4

%build
./configure --with-rexx=oorexx --with-ncurses
make nthe the.man #THE_Help.txt helpviewer

%install
make install the the.man

%files
/usr/bin/nthe
/usr/man/man1/the.1
/usr/share/THE
%doc COPYING
%doc README
