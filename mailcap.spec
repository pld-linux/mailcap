# TODO
# - use IANA as source http://www.iana.org/assignments/media-types/ ?
Summary:	Defines multimedia helper applications for various programs
Summary(de):	Definiert Multimedia-Hilfsapplikationen für diverse Programme
Summary(es):	Define aplicaciones auxiliares multimedia para varios programas
Summary(fr):	Définit une aide multimédia pour de nombreuses applications
Summary(pl):	Definicje rozszerzeñ multimedialnych dla ró¿nych programów
Summary(pt_BR):	Define aplicações auxiliares multimídia para vários programas
Summary(tr):	Çeþitli programlar için çokluortam yardýmcý uygulamalarý tanýmlar
Name:		mailcap
Version:	2.1.14
Release:	8
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

%description -l de
Wenn es installiert ist, können Programme wie 'lynx' automatically
'zgv' zum Darstellen von Bildern verwenden (zgv muß installiert sein).

%description -l es
Este es el paquete Red Hat Mailcap. Al instalarlo podrás hacer que
programas como lynx usen automáticamente zgv para enseñar imágenes
(con zgv instalado).

%description -l fr
L'installer permettra à des programmes come lynx d'utiliser
automatiquement zgv pour afficher des images (pourvu que zgv soit
installé).

%description -l pl
Plik mailcap jest u¿ywany przez program metamail i inne. Pakiet ten
pozwoli na automatyczne wy¶wietlanie grafiki przez programy takie jak
lynx, przy u¿yciu zgv.

%description -l pt_BR
Este é o pacote Red Hat Mailcap. Instalando você poderá fazer com que
programas como lynx automaticamente usem zgv para mostrar figuras (com
o zgv instalado).

%description -l tr
lynx gibi programlarýn resim göstermek için otomatik olarak zgv
paketini kullanamalarýna olanak saðlar (zgv kurulmuþ olmalý).

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
