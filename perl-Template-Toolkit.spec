%define	modname	Template-Toolkit
%define	__noautoreq 'perl\\(CGI\\)'

Summary:	%{modname} module for perl
Name:		perl-%{modname}
Version:	3.102
Release:	2
License:	GPLv2
Group:		Development/Perl
Url:		https://www.template-toolkit.org
Source0:	http://www.cpan.org/modules/by-module/Template/%{modname}-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(AppConfig)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Pod::POM)
BuildRequires:	perl(Text::Autoformat)

%description
The Template Toolkit is a collection of modules which implement a
fast, flexible, powerful and extensible template processing system.
It was originally designed and remains primarily useful for generating
dynamic web content, but it can be used equally well for processing
any other kind of text based documents: HTML, XML, POD, PostScript,
LaTeX, and so on.

%prep
%autosetup -p1 -n %{modname}-%{version} 

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
%doc Changes TODO
%{_bindir}/*
%{perl_vendorarch}/Template*
%{perl_vendorarch}/auto/Template
%{_mandir}/man1/*
%{_mandir}/man3/*
