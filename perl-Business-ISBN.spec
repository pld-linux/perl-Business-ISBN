%include	/usr/lib/rpm/macros.perl
%define		pdir	Business
%define		pnam	ISBN
Summary:	Business::ISBN - work with International Standard Book Numbers
Summary(pl):	Business::ISBN - obs�uga numer�w ISBN
Name:		perl-Business-ISBN
Version:	20001010
Release:	9
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9f3be82ae9ab251a1d3780d243f10d6f
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Business::ISBN - work with International Standard Book Numbers.

%description -l pl
Business::ISBN to modu� Perla umo�liwiaj�cy prac� z ISBN
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
