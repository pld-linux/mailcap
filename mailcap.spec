Summary:	Defines multimedia helper applications for various programs
Summary(de):	Definiert Multimedia-Hilfsapplikationen für diverse Programme
Summary(fr):	Définit une aide multimédia pour de nombreuses applications.
Summary(pl):	Definiuje rozszerzenia multimedialne dla róznych programów.
Summary(tr):	Çeþitli programlar için çokluortam yardýmcý uygulamalarý tanýmlar
Name:		mailcap
Version:	2.0.9
Release:	3
Copyright:	public domain
Group:		Base
Group(pl):	Bazowe
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Buildarch:	noarch

%description
The mailcap file is used by the metamail program. Metamail reads the
mailcap file to determine how it should display non-text or multimedia
material. Basically, mailcap associates a particular type of file with
a particular program that a mail agent or other program can call in
order to handle the file.

%description -l pl
Plik mailcap jest u¿ywany przez program metamail i inne. Pakiet ten
pozwoli na automatyczne wy¶wietlanie grafiki przez programy takie jak
lynx, przy u¿yciu zgv.

%description -l de
Wenn es installiert ist, können Programme wie 'lynx' automatically
'zgv' zum Darstellen von Bildern verwenden (zgv muß installiert sein).

%description -l fr
L'installer permettra à des programmes come lynx d'utiliser
automatiquement zgv pour afficher des images (pourvu que zgv soit
installé).

%description -l tr
lynx gibi programlarýn resim göstermek için otomatik olarak zgv
paketini kullanamalarýna olanak saðlar (zgv kurulmuþ olmalý).

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc,%{_mandir}/man4}

install mailcap mailcap.vga mime.types $RPM_BUILD_ROOT%{_sysconfdir}

install mailcap.4 $RPM_BUILD_ROOT%{_mandir}/man4

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man4/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%config %{_sysconfdir}/*

%{_mandir}/man4/*
