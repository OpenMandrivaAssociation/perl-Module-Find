%define upstream_name	 Module-Find
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Find and use installed modules in a (sub)category
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Module::Find lets you find and use modules in categories. This can be
very useful for auto-detecting driver or plugin modules. You can
differentiate between looking in the category itself or in all
subcategories.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc Changes
%{_mandir}/man*/*
%{perl_vendorlib}/Module
