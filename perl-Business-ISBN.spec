%include	/usr/lib/rpm/macros.perl
%define	pdir	Business
%define	pnam	ISBN
Summary:	Business-ISBN perl module
Summary(pl):	Modu³ perla Business-ISBN
Name:		perl-Business-ISBN
Version:	20001010
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Business-ISBN - work with International Standard Book Numbers.

%description -l pl
Business-ISBN - modu³ umo¿liwiaj±cy pracê z ISBN (International
Standard Book Numbers).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Business/ISBN.pm
%{_mandir}/man3/*
