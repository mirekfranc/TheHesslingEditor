Name: the
Version: 3.4
Release: 4
Summary: The Hessling Editor
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
make

%install
install -b -D -m 755 the %{buildroot}/%{_bindir}/the
gzip -f the.1
install -b -D -m 644 the.1.gz %{buildroot}/%{_mandir}/man1/the.1.gz
install -b -D -m 644 THE_Help.txt %{buildroot}/%{_datadir}/THE/THE_Help.txt
install -b -D -m 644 append.the   %{buildroot}/%{_datadir}/THE/append.the
install -b -D -m 644 comm.the     %{buildroot}/%{_datadir}/THE/comm.the
install -b -D -m 644 build.the    %{buildroot}/%{_datadir}/THE/build.the
install -b -D -m 644 uncomm.the   %{buildroot}/%{_datadir}/THE/uncomm.the
install -b -D -m 644 total.the    %{buildroot}/%{_datadir}/THE/total.the
install -b -D -m 644 match.the    %{buildroot}/%{_datadir}/THE/match.the
install -b -D -m 644 rm.the       %{buildroot}/%{_datadir}/THE/rm.the
install -b -D -m 644 nl.the       %{buildroot}/%{_datadir}/THE/nl.the
install -b -D -m 644 words.the    %{buildroot}/%{_datadir}/THE/words.the
install -b -D -m 644 l.the        %{buildroot}/%{_datadir}/THE/l.the
install -b -D -m 644 compile.the  %{buildroot}/%{_datadir}/THE/compile.the
install -b -D -m 644 spell.the    %{buildroot}/%{_datadir}/THE/spell.the
install -b -D -m 644 demo.the     %{buildroot}/%{_datadir}/THE/demo.the
install -b -D -m 644 cua.the      %{buildroot}/%{_datadir}/THE/cua.the
install -b -D -m 644 config.the   %{buildroot}/%{_datadir}/THE/config.the
install -b -D -m 644 tags.the     %{buildroot}/%{_datadir}/THE/tags.the
install -b -D -m 644 codecomp.the %{buildroot}/%{_datadir}/THE/codecomp.the
install -b -D -m 644 complete.the %{buildroot}/%{_datadir}/THE/complete.the
install -b -D -m 644 syntax.the   %{buildroot}/%{_datadir}/THE/syntax.the

%files
%{_bindir}/the
%doc %{_mandir}/man1/the.1.gz
%{_datadir}/THE/THE_Help.txt
%{_datadir}/THE/append.the
%{_datadir}/THE/comm.the
%{_datadir}/THE/build.the
%{_datadir}/THE/uncomm.the
%{_datadir}/THE/total.the
%{_datadir}/THE/match.the
%{_datadir}/THE/rm.the
%{_datadir}/THE/nl.the
%{_datadir}/THE/words.the
%{_datadir}/THE/l.the
%{_datadir}/THE/compile.the
%{_datadir}/THE/spell.the
%{_datadir}/THE/demo.the
%{_datadir}/THE/cua.the
%{_datadir}/THE/config.the
%{_datadir}/THE/tags.the
%{_datadir}/THE/codecomp.the
%{_datadir}/THE/complete.the
%{_datadir}/THE/syntax.the

%changelog
