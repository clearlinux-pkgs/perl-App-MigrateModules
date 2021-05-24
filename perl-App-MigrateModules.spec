#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-App-MigrateModules
Version  : 0.004
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/D/DB/DBOOK/App-MigrateModules-0.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DB/DBOOK/App-MigrateModules-0.004.tar.gz
Summary  : 'Migrate installed CPAN modules from one Perl to another'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-App-MigrateModules-bin = %{version}-%{release}
Requires: perl-App-MigrateModules-license = %{version}-%{release}
Requires: perl-App-MigrateModules-man = %{version}-%{release}
Requires: perl-App-MigrateModules-perl = %{version}-%{release}
Requires: perl(Getopt::Long::Modern)
Requires: perl(HTTP::Tinyish)
BuildRequires : buildreq-cpan
BuildRequires : perl(Getopt::Long::Modern)
BuildRequires : perl(HTTP::Tinyish)

%description
NAME
perl-migrate-modules - Migrate installed CPAN modules from one Perl to
another

%package bin
Summary: bin components for the perl-App-MigrateModules package.
Group: Binaries
Requires: perl-App-MigrateModules-license = %{version}-%{release}

%description bin
bin components for the perl-App-MigrateModules package.


%package dev
Summary: dev components for the perl-App-MigrateModules package.
Group: Development
Requires: perl-App-MigrateModules-bin = %{version}-%{release}
Provides: perl-App-MigrateModules-devel = %{version}-%{release}
Requires: perl-App-MigrateModules = %{version}-%{release}

%description dev
dev components for the perl-App-MigrateModules package.


%package license
Summary: license components for the perl-App-MigrateModules package.
Group: Default

%description license
license components for the perl-App-MigrateModules package.


%package man
Summary: man components for the perl-App-MigrateModules package.
Group: Default

%description man
man components for the perl-App-MigrateModules package.


%package perl
Summary: perl components for the perl-App-MigrateModules package.
Group: Default
Requires: perl-App-MigrateModules = %{version}-%{release}

%description perl
perl components for the perl-App-MigrateModules package.


%prep
%setup -q -n App-MigrateModules-0.004
cd %{_builddir}/App-MigrateModules-0.004

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-App-MigrateModules
cp %{_builddir}/App-MigrateModules-0.004/LICENSE %{buildroot}/usr/share/package-licenses/perl-App-MigrateModules/5ed759308c4d22624a19e86e9b25fcbbb4b62e59
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/perl-migrate-modules

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/App::MigrateModules.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-App-MigrateModules/5ed759308c4d22624a19e86e9b25fcbbb4b62e59

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/perl-migrate-modules.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/App/MigrateModules.pm
