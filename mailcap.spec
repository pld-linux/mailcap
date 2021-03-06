# TODO
# - use IANA as source http://www.iana.org/assignments/media-types/ ?
#   nb. fedorahosted mailcap project is synchronized with IANA
#
# Conditional build:
%bcond_without	tests	# do not perform "make check"

%define		fcver	2.1.45
%define		ver		2.3.%(v=%{fcver}; echo ${v#2.1.})
Summary:	Defines multimedia helper applications for various programs
Summary(de.UTF-8):	Definiert Multimedia-Hilfsapplikationen für diverse Programme
Summary(es.UTF-8):	Define aplicaciones auxiliares multimedia para varios programas
Summary(fr.UTF-8):	Définit une aide multimédia pour de nombreuses applications
Summary(pl.UTF-8):	Definicje rozszerzeń multimedialnych dla różnych programów
Summary(pt_BR.UTF-8):	Define aplicações auxiliares multimídia para vários programas
Summary(tr.UTF-8):	Çeşitli programlar için çokluortam yardımcı uygulamaları tanımlar
Name:		mailcap
Version:	%{ver}
Release:	4
License:	Public Domain
Group:		Base
Source0:	https://fedorahosted.org/released/mailcap/%{name}-%{fcver}.tar.xz
# Source0-md5:	d8d66b3a458f0da327a7c4edfff911a1
Source1:	%{name}
Source2:	%{name}.4
# https://anonscm.debian.org/git/collab-maint/mime-support.git/log/run-mailcap
Source3:	run-%{name}
Source4:	run-%{name}.man
Patch0:		mime.types.patch
Patch1:		run-mailcap-mktemp.patch
URL:		http://git.fedorahosted.org/git/?p=mailcap.git
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Suggests:	ImageMagick-coder-jpeg
Suggests:	ImageMagick-coder-png
Suggests:	aview
Suggests:	colordiff
Suggests:	dvi2tty
Suggests:	elinks
Suggests:	eog
Suggests:	ghostscript
Suggests:	gplflash
Suggests:	gv
Suggests:	id3v2
Suggests:	libcaca-img
Suggests:	metamail
Suggests:	mikmod
Suggests:	mplayer
Suggests:	odt2txt
Suggests:	perl-base
Suggests:	qiv
Suggests:	soffice2html
Suggests:	tar
Suggests:	tnef
Suggests:	unrar
Suggests:	unrtf
Suggests:	unzip
Suggests:	wv
Suggests:	xdvi
Suggests:	xlhtml
Suggests:	xpdf
Suggests:	xpdf-tools
%if "%{pld_release}" == "ac"
Suggests:	X11
%else
Suggests:	xterm
%endif
%{?with_tests:BuildRequires:perl-base}
Conflicts:	lesspipe < 1.57-4
Conflicts:	rpm < 4.4.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqfiles	%{_bindir}/run-%{name}

%description
The mailcap file is used by the metamail program. Metamail reads the
mailcap file to determine how it should display non-text or multimedia
material. Basically, mailcap associates a particular type of file with
a particular program that a mail agent or other program can call in
order to handle the file.

%description -l de.UTF-8
Wenn es installiert ist, können Programme wie 'lynx' automatically
'zgv' zum Darstellen von Bildern verwenden (zgv muß installiert sein).

%description -l es.UTF-8
Este es el paquete Red Hat Mailcap. Al instalarlo podrás hacer que
programas como lynx usen automáticamente zgv para enseñar imágenes
(con zgv instalado).

%description -l fr.UTF-8
L'installer permettra à des programmes come lynx d'utiliser
automatiquement zgv pour afficher des images (pourvu que zgv soit
installé).

%description -l pl.UTF-8
Plik mailcap jest używany przez program metamail i inne. Pakiet ten
pozwoli na automatyczne wyświetlanie grafiki przez programy takie jak
lynx, przy użyciu zgv.

%description -l pt_BR.UTF-8
Este é o pacote Red Hat Mailcap. Instalando você poderá fazer com que
programas como lynx automaticamente usem zgv para mostrar figuras (com
o zgv instalado).

%description -l tr.UTF-8
lynx gibi programların resim göstermek için otomatik olarak zgv
paketini kullanamalarına olanak sağlar (zgv kurulmuş olmalı).

%prep
%setup -q -n %{name}-%{fcver}
%patch0 -p1
cp -a %{SOURCE1} %{SOURCE3} .
%patch1

%if "%{pld_release}" == "ac"
%{__sed} -i -e 's,/usr/bin/xterm,/usr/X11R6/bin/xterm,g' mailcap
%endif

%build
%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man{1,4},%{_bindir}}

cp -p mailcap mime.types $RPM_BUILD_ROOT%{_sysconfdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man4
cp -p %{SOURCE4} $RPM_BUILD_ROOT%{_mandir}/man1/run-%{name}.1
cp -p run-mailcap $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mailcap
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mime.types
%attr(755,root,root) %{_bindir}/run-mailcap
%{_mandir}/man1/run-mailcap.1*
%{_mandir}/man4/mailcap.4*
