Summary:     Defines multimedia helper applications for various programs
Summary(de): Definiert Multimedia-Hilfsapplikationen f�r diverse Programme
Summary(fr): D�finit une aide multim�dia pour de nombreuses applications.
Summary(pl): Definiuje rozszerzenia multimedialne dla r�znych program�w.
Summary(tr): �e�itli programlar i�in �okluortam yard�mc� uygulamalar� tan�mlar
Name:        mailcap
Version:     1.0
Release:     3
Copyright:   public domain
Group:       Base
Group:       Podstawowe
Source:      %{name}-%{version}.tar.gz
Source1:     mime.types
Patch:       %{name}-%{version}-mikmod.patch
BuildRoot:   /tmp/%{name}-%{version}-root
Buildarch:   noarch

%description
This is the PLD Mailcap package.  Installing it will allow
programs like lynx to automatically use zgv to display pictures
(provided zgv is installed).

%description -l pl
To jest PLD Mailcap. Pakiet ten pozwoli na automatyczne wy�wietlanie
grafiki przez programy takie jak lynx, przy u�yciu zgv.

%description -l de
Dies ist das PLD-Mailcap-Paket. Wenn es installiert ist, k�nnen
Programme wie 'lynx' automatically 'zgv' zum Darstellen von Bildern
verwenden (zgv mu� installiert sein).

%description -l fr
Ceci est le package Mailcap de PLD. L'installer permettra �
des programmes come lynx d'utiliser automatiquement zgv pour 
afficher des images (pourvu que zgv soit install�).

%description -l tr
lynx gibi programlar�n resim g�stermek i�in otomatik olarak zgv paketini
kullanamalar�na olanak sa�lar (zgv kurulmu� olmal�).

%prep
%setup -q
%patch -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc,usr/share/man/man4}

install mailcap mailcap.vga $RPM_BUILD_ROOT/etc

install %{SOURCE1} $RPM_BUILD_ROOT/etc/mime.types

install mailcap.4 $RPM_BUILD_ROOT%{_mandir}/man4

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/man4/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%config /etc/*

%{_mandir}/man4/*
