#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Module
%define		pnam	Build-XSUtil
%include	/usr/lib/rpm/macros.perl
Summary:	Module::Build::XSUtil - A Module::Build class for building XS modules
Name:		perl-Module-Build-XSUtil
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	40045cdd0730d09abc05423f7c103adb
URL:		http://search.cpan.org/dist/Module-Build-XSUtil/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Cwd::Guard)
BuildRequires:	perl(Devel::CheckCompiler) >= 0.02
BuildRequires:	perl(File::Copy::Recursive)
BuildRequires:	perl-Capture-Tiny
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Build::XSUtil is subclass of Module::Build for support
building XS modules.

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
%{perl_vendorlib}/Module/Build/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
