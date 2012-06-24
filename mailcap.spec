Summary:	Defines multimedia helper applications for various programs
Summary(de):	Definiert Multimedia-Hilfsapplikationen f�r diverse Programme
Summary(es):	Define aplicaciones auxiliares multimedia para varios programas
Summary(fr):	D�finit une aide multim�dia pour de nombreuses applications
Summary(pl):	Definiuje rozszerzenia multimedialne dla r�znych program�w
Summary(pt_BR):	Define aplica��es auxiliares multim�dia para v�rios programas
Summary(tr):	�e�itli programlar i�in �okluortam yard�mc� uygulamalar� tan�mlar
Name:		mailcap
Version:	2.1.9
Release:	5
License:	Public Domain
Group:		Base
Source0:	%{name}-%{version}.tar.gz
#Source0-md5:	ae72570ee9b958f303f514df0cc775b3
Patch0:		%{name}-application.x-ns-proxy-autoconfig.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Buildarch:	noarch

%description
The mailcap file is used by the metamail program. Metamail reads the
mailcap file to determine how it should display non-text or multimedia
material. Basically, mailcap associates a particular type of file with
a particular program that a mail agent or other program can call in
order to handle the file.

%description -l de
Wenn es installiert ist, k�nnen Programme wie 'lynx' automatically
'zgv' zum Darstellen von Bildern verwenden (zgv mu� installiert sein).

%description -l es
Este es el paquete Red Hat Mailcap. Al instalarlo podr�s hacer que
programas como lynx usen autom�ticamente zgv para ense�ar im�genes
(con zgv instalado).

%description -l fr
L'installer permettra � des programmes come lynx d'utiliser
automatiquement zgv pour afficher des images (pourvu que zgv soit
install�).

%description -l pl
Plik mailcap jest u�ywany przez program metamail i inne. Pakiet ten
pozwoli na automatyczne wy�wietlanie grafiki przez programy takie jak
lynx, przy u�yciu zgv.

%description -l pt_BR
Este � o pacote Red Hat Mailcap. Instalando voc� poder� fazer com que
programas como lynx automaticamente usem zgv para mostrar figuras (com
o zgv instalado).

%description -l tr
lynx gibi programlar�n resim g�stermek i�in otomatik olarak zgv
paketini kullanamalar�na olanak sa�lar (zgv kurulmu� olmal�).

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc,%{_mandir}/man4}

install mailcap mime.types $RPM_BUILD_ROOT%{_sysconfdir}
install mailcap.4 $RPM_BUILD_ROOT%{_mandir}/man4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%{_mandir}/man4/*
