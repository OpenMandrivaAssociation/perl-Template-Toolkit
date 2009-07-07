%define upstream_name       Template-Toolkit
%define upstream_version    2.21
%define _provides_exceptions perl(CGI)\\|perl(My::

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary: 	%{module} module for perl
License:	GPL
Group:		Development/Perl
URL:		http://www.template-toolkit.org
Source:     http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.gz
Requires:	perl >= 0:5.600
BuildRequires:	perl-devel >= 0:5.600
BuildRequires:	perl(AppConfig) >= 1.56
BuildRequires:	perl(File::Spec) >= 0.8
BuildRequires:	perl(File::Temp) >= 0.12
BuildRequires:	perl(Pod::POM) >= 0.1
BuildRequires:	perl(Text::Autoformat) >= 1.03
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Template Toolkit is a collection of modules which implement a
fast, flexible, powerful and extensible template processing system.
It was originally designed and remains primarily useful for generating
dynamic web content, but it can be used equally well for processing
any other kind of text based documents: HTML, XML, POD, PostScript,
LaTeX, and so on.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

# perl path hack
find ./ -type f | \
    xargs perl -pi -e 's|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|'

%build
%{__perl} Makefile.PL \
    TT_XS_ENABLE="y" \
    TT_XS_DEFAULT="y" \
    INSTALLDIRS=vendor </dev/null
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README Changes TODO HACKING INSTALL
%{perl_vendorarch}/Template*
%{perl_vendorarch}/auto/Template
%{_mandir}/*/*
%{_bindir}/*
