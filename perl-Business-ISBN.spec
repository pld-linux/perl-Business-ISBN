%include	/usr/lib/rpm/macros.perl
Summary:	Business-ISBN perl module
Summary(pl):	Modu� perla Business-ISBN
Name:		perl-Business-ISBN
Version:	19990112
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Business/Business-ISBN-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Business-ISBN - work with International Standard Book Numbers

%description -l pl
Business-ISBN - modu� umo�liwiaj�cy prac� z ISBN (International Standard 
Book Numbers)

%prep
%setup -q -n Business-ISBN-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Business/ISBN
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Business/ISBN.pm
%{perl_sitearch}/auto/Business/ISBN

%{_mandir}/man3/*
