%include	/usr/lib/rpm/macros.perl
Summary:	Business-ISBN perl module
Summary(pl):	Modu� perla Business-ISBN
Name:		perl-Business-ISBN
Version:	20001010
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Business/Business-ISBN-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Business-ISBN - work with International Standard Book Numbers.

%description -l pl
Business-ISBN - modu� umo�liwiaj�cy prac� z ISBN (International
Standard Book Numbers).

%prep
%setup -q -n Business-ISBN-%{version}

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
