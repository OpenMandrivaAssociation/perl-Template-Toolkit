%define module  Template-Toolkit
%define name	perl-%{module}
%define	modprefix Template

%define version 2.19

%define	rel	1
%define release %mkrel 2

%define _provides_exceptions perl(CGI)\\|perl(My::

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	%{module} module for perl
License:	GPL
Group:		Development/Perl
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
URL:		http://www.template-toolkit.org
Requires:	perl >= 0:5.600
BuildRequires:	perl-devel >= 0:5.600
BuildRequires:	perl(AppConfig) >= 1.56
BuildRequires:	perl(File::Spec) >= 0.8
BuildRequires:	perl(File::Temp) >= 0.12
BuildRequires:	perl(Pod::POM) >= 0.1
BuildRequires:	perl(Text::Autoformat) >= 1.03
BuildRoot:	%{_tmppath}/%{name}-%{version}
Obsoletes:	perl-Template
Provides:	perl-Template = %{version}

%description
The Template Toolkit is a collection of modules which implement a
fast, flexible, powerful and extensible template processing system.
It was originally designed and remains primarily useful for generating
dynamic web content, but it can be used equally well for processing
any other kind of text based documents: HTML, XML, POD, PostScript,
LaTeX, and so on.

%prep
%setup -q -n %{module}-%{version}

# perl path hack
find ./ -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%{__perl} Makefile.PL \
    TT_PREFIX=%{_datadir}/tt2 \
    TT_IMAGES=%{_datadir}/tt2/images \
    TT_DOCS="y" \
    TT_SPLASH="y" \
    TT_THEME="aqua" \
    TT_EXAMPLES="y" \
    TT_EXTRAS="y" \
    TT_XS_ENABLE="y" \
    TT_XS_DEFAULT="y" \
    TT_ACCEPT=y \
    INSTALLDIRS=vendor </dev/null
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot} 

# ==> ugly hack, begin
find ./ -name "ttree.cfg" | xargs perl -p -i -e "s|%{_datadir}|%{buildroot}%{_datadir}|g"

make install DESTDIR=%{buildroot} \
    PREFIX=%{buildroot}%{_prefix} \
    TT_PREFIX="%{buildroot}%{_datadir}/tt2"

find %{buildroot}%{_datadir}/tt2 -name "ttree.cfg" | xargs perl -p -i -e "s|%{buildroot}%{_datadir}|%{_datadir}|g"
# <== ugly hack, end

# maybe the "%{_datadir}/tt2/docs" and "%{_datadir}/tt2/examples" directories
# should be moved to the docdir?

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README Changes TODO HACKING INSTALL
%{perl_vendorarch}/%{modprefix}*
%{perl_vendorarch}/auto/%{modprefix}
%{_mandir}/*/*
%{_datadir}/tt2
%{_bindir}/*


