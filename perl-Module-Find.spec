%define upstream_name	 Module-Find
%define upstream_version 0.17
Name:		perl-%{upstream_name}
Version:	0.17
Release:	1

Summary:	Find and use installed modules in a (sub)category
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://github.com/crenz/Module-Find
Source0:	https://cpan.metacpan.org/authors/id/C/CR/CRENZ/Module-Find-0.17.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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


