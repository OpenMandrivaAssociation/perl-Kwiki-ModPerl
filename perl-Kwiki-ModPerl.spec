%define upstream_name	 Kwiki-ModPerl
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Enable Kwiki to work under mod_perl 
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Kwiki)
BuildRequires:	apache-mod_perl
BuildArch:	noarch
Requires:	apache-mod_perl

%description
This module allows you to use Kwiki as a mod_perl content handler.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 403380
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.09-7mdv2009.0
+ Revision: 257454
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.09-6mdv2009.0
+ Revision: 245424
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-4mdv2008.1
+ Revision: 133635
- rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-3mdv2007.0
- Rebuild

* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.09-2mdk
- Fix According to perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdk
- New release 0.09

* Thu Jun 02 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdk 
- New release 0.08
- fix source URL for rpmbuildupdate
- tests in %%check

* Tue May 03 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-3mdk 
- fix requires

* Fri Apr 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-2mdk 
- requires apache-mod_perl

* Mon Apr 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdk 
- first mandriva release

