%define	modname	Template-Toolkit
%define modver 3.100
%define	__noautoreq 'perl\\(CGI\\)'
%ifarch %{x86_64}
# FIXME bug workaround
%global _debugsource_template %{nil}
%endif

Summary:	%{modname} module for perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2
Group:		Development/Perl
Url:		http://www.template-toolkit.org
Source0:	http://www.cpan.org/modules/by-module/Template/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel >= 0:5.600
BuildRequires:	perl(AppConfig) >= 1.56
BuildRequires:	perl(File::Spec) >= 0.8
BuildRequires:	perl(File::Temp) >= 0.12
BuildRequires:	perl(Pod::POM) >= 0.1
BuildRequires:	perl(Text::Autoformat) >= 1.03

%description
The Template Toolkit is a collection of modules which implement a
fast, flexible, powerful and extensible template processing system.
It was originally designed and remains primarily useful for generating
dynamic web content, but it can be used equally well for processing
any other kind of text based documents: HTML, XML, POD, PostScript,
LaTeX, and so on.

%prep
%setup -qn %{modname}-%{modver} 

# perl path hack
find ./ -type f | \
    xargs perl -pi -e 's|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|'

%build
perl Makefile.PL \
	TT_XS_ENABLE="y" \
	TT_XS_DEFAULT="y" \
	INSTALLDIRS=vendor </dev/null
%make_build CFLAGS="%{optflags}"

%install
%make_install

%files
%doc Changes TODO HACKING
%{_bindir}/*
%{perl_vendorarch}/Template*
%{perl_vendorarch}/auto/Template
%{_mandir}/man1/*
%{_mandir}/man3/*
