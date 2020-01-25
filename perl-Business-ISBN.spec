%define		pdir	Business
%define		pnam	ISBN
Summary:	Business::ISBN - work with International Standard Book Numbers
Summary(pl.UTF-8):	Business::ISBN - obsługa numerów ISBN
Name:		perl-Business-ISBN
Version:	20001010
Release:	10
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9f3be82ae9ab251a1d3780d243f10d6f
URL:		http://search.cpan.org/dist/Business-ISBN/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Business::ISBN - work with International Standard Book Numbers.

%description -l pl.UTF-8
Business::ISBN to moduł Perla umożliwiający pracę z ISBN
(International Standard Book Numbers).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Business/ISBN.pm
%{_mandir}/man3/*
