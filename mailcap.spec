# TODO
# - use IANA as source http://www.iana.org/assignments/media-types/ ?
Summary:	Defines multimedia helper applications for various programs
Summary(de.UTF-8):	Definiert Multimedia-Hilfsapplikationen für diverse Programme
Summary(es.UTF-8):	Define aplicaciones auxiliares multimedia para varios programas
Summary(fr.UTF-8):	Définit une aide multimédia pour de nombreuses applications
Summary(pl.UTF-8):	Definicje rozszerzeń multimedialnych dla różnych programów
Summary(pt_BR.UTF-8):	Define aplicações auxiliares multimídia para vários programas
Summary(tr.UTF-8):	Çeşitli programlar için çokluortam yardımcı uygulamaları tanımlar
Name:		mailcap
Version:	2.1.14
Release:	10
License:	Public Domain
Group:		Base
Source0:	%{name}
Source1:	%{name}.4
Source2:	mime.types
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man4}

install %{SOURCE0} %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%{_mandir}/man4/*