%define upstream_name	 Module-Find
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Find and use installed modules in a (sub)category
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Module/Module-Find-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Module::Find lets you find and use modules in categories. This can be
very useful for auto-detecting driver or plugin modules. You can
differentiate between looking in the category itself or in all
subcategories.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc Changes
%{_mandir}/man*/*
%{perl_vendorlib}/Module


%changelog
* Sun Feb 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.1
+ Revision: 512596
- update to 0.10

* Fri Feb 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 511456
- update to 0.09

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 435715
- update to 0.08

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 406380
- rebuild using %%perl_convert_version

* Sun Jan 27 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2008.1
+ Revision: 158618
- update to new version 0.06

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-2mdv2008.0
+ Revision: 86640
- rebuild


* Mon Jun 26 2006 Scott Karns <scottk@mandriva.org> 0.05-1mdv2007.0
- Initial MDV release



