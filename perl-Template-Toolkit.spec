%define	modname	Template-Toolkit
%define	modver	2.22
%define	__noautoreq 'perl\\(CGI\\)'

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	8

Summary:	%{modname} module for perl
License:	GPL
Group:		Development/Perl
URL:		http://www.template-toolkit.org
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
%setup -q -n %{modname}-%{modver} 

# perl path hack
find ./ -type f | \
    xargs perl -pi -e 's|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|'

%build
perl Makefile.PL \
    TT_XS_ENABLE="y" \
    TT_XS_DEFAULT="y" \
    INSTALLDIRS=vendor </dev/null
%make CFLAGS="%{optflags}"

%install
%makeinstall_std

%files
%doc README Changes TODO HACKING
%{perl_vendorarch}/Template*
%{perl_vendorarch}/auto/Template
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Fri Dec 21 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.220.0-8
- update dependency filter to use internal dependency generator
- cleanups

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.220.0-7mdv2012.0
+ Revision: 765670
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.220.0-6
+ Revision: 764181
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.220.0-5
+ Revision: 667320
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.220.0-4mdv2011.0
+ Revision: 564582
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.220.0-3mdv2011.0
+ Revision: 556155
- rebuild for perl 5.12

* Fri Apr 30 2010 Funda Wang <fwang@mandriva.org> 2.220.0-2mdv2010.1
+ Revision: 541166
- fix summary

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 2.220.0-1mdv2010.0
+ Revision: 399469
- update to 2.22

* Tue Jul 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.210.0-1mdv2010.0
+ Revision: 393194
- new version
- spec cleanup

* Tue Jun 09 2009 Jérôme Quelin <jquelin@mandriva.org> 2.20-1mdv2010.0
+ Revision: 384330
- patching makefile.pl to go through all the steps
- update to 2.20

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.19-3mdv2009.0
+ Revision: 224064
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 2.19-2mdv2008.1
+ Revision: 151257
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 21 2007 Michael Scherer <misc@mandriva.org> 2.19-1mdv2008.0
+ Revision: 29091
- Update to new version 2.19


* Wed Mar 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.18-1mdv2007.1
+ Revision: 134809
- new version
- Import perl-Template-Toolkit

* Sat May 27 2006 Scott Karns <scottk@mandriva.org> 2.15-2mdv2007.0
- Added versioned provides for perl-Template

* Sat May 27 2006 Scott Karns <scottk@mandriva.org> 2.15-1mdv2007.0
- 2.15
- Updated BuildRequires per version 2.15
- Updated _provides_exceptions to eliminate bogus provide perl(My::*)
- Template::Plugin::DBI modules are now provided by perl-Template-DBI
- Template::Plugin::XML modules are now provided by perl-Template-XML

* Fri Jul 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.14-3mdk 
- fix package name to be policy compliant
- drop tetex requires

* Thu Mar 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.14-2mdk
- Don't provide perl(CGI) and other perl modules already found otherwise

* Tue Nov 16 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.14-1mdk
- 2.14

* Tue Jul 27 2004 Stefan van der Eijk <stefan@mandrake.org> 2.13-1mdk
- 2.13

