#
# Conditional build:
%bcond_without	tests	# unit tests

%define		pdir	Module
%define		pnam	Build-XSUtil
Summary:	Module::Build::XSUtil - a Module::Build class for building XS modules
Summary(pl.UTF-8):	Module::Build::XSUtil - klasa Module::Build do budowania modułów XS
Name:		perl-Module-Build-XSUtil
Version:	0.19
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7ebe5859645989a556c333f3de7fc337
URL:		https://metacpan.org/dist/Module-Build-XSUtil
BuildRequires:	perl-Module-Build >= 0.4005
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Capture-Tiny
BuildRequires:	perl-Cwd-Guard
BuildRequires:	perl-Devel-CheckCompiler
BuildRequires:	perl-Devel-PPPort
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-File-Copy-Recursive-Reduced >= 0.002
BuildRequires:	perl-Test-Simple >= 0.98
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Build::XSUtil is subclass of Module::Build for support
building XS modules.

%description -l pl.UTF-8
Module::Build::XSUtil to podklasa Module::Build do obsługi budowania
modułów XS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Module/Build/XSUtil.pm
%{_mandir}/man3/Module::Build::XSUtil.3pm*
%{_examplesdir}/%{name}-%{version}
