%define upstream_name	 Kwiki-ModPerl
Name:		perl-%{upstream_name}
Version:	0.09
Release:	7
Summary:	Enable Kwiki to work under mod_perl 
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{upstream_name}-%{version}.tar.bz2
Patch0:		perl-Kwiki-ModPerl-0.09-Parenthesise-qw-explicitly.patch

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Kwiki)
BuildRequires:	apache-mod_perl
BuildArch:	noarch
Requires:	apache-mod_perl

%description
This module allows you to use Kwiki as a mod_perl content handler.

%prep
%setup -q -n %{upstream_name}-%{version}
%patch0 -p1 -b .fix-build

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*
