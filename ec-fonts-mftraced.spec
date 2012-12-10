Name:           ec-fonts-mftraced
Version:        1.0.12
Release:        6
Epoch:          0
Summary:        Type1 PostScript fonts for TeX with european accents
License:        Public Domain
Group:          Publishing
URL:            http://lilypond.org/download/
Source0:        http://lilypond.org/download/old/ec-fonts-mftraced/ec-fonts-mftraced-%{version}.tar.gz
Requires(post): tetex
BuildRequires:  mftrace
BuildRequires:  potrace
BuildRequires:  texlive
BuildRequires:  texlive-dvips
BuildArch:      noarch

%description
These are Type1 renderings of the EC variants of the standard CMR
family.

%prep
%setup -q
%{__perl} -pi -e 's|--potrace |--potrace="%{_bindir}/potrace" |' ./GNUmakefile

%build
%{configure2_5x}
%{__make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

# handle doc files in %%doc instead
%{__rm} -r %{buildroot}%{_docdir}


%post
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 2>/dev/null

%files
%defattr(0644,root,root,0755)
%doc COPYING ChangeLog INSTALL LICENSE README VERSION
%{_datadir}/texmf/fonts/map/dvips/%{name}
%{_datadir}/texmf/fonts/type1/public/%{name}
%{_datadir}/texmf/fonts/tfm/public/%{name}


%changelog
* Sun Oct 14 2012 Giovanni Mariani <mc2374@mclink.it> 0:1.0.12-6
- Tetex is gone: changed BReqs to texlive ones
- Dropped BuildRoot, %%mkrel and %%clean section

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.0.12-5mdv2011.0
+ Revision: 617973
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0:1.0.12-4mdv2010.0
+ Revision: 428444
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0:1.0.12-3mdv2009.0
+ Revision: 244610
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0:1.0.12-1mdv2008.1
+ Revision: 140723
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Apr 18 2007 David Walluck <walluck@mandriva.org> 0:1.0.12-1mdv2008.0
+ Revision: 14344
- BuildRequires: tetex-dvips
- 1.0.12
- Import ec-fonts-mftraced



* Fri Jan 14 2005 Abel Cheung <deaddog@mandrakesoft.com> 1.0.9-1mdk
- New release 1.0.9

* Sun Dec 26 2004 Abel Cheung <deaddog@mandrake.org> 1.0.8-2mdk
- Fix BuildRequires

* Mon Dec 06 2004 Abel Cheung <deaddog@mandrake.org> 1.0.8-1mdk
- First Mandrakelinux package, based on work from Noam Meltzer

* Thu Nov 11 2004 Noam Meltzer <tsnoam@zahav.net.il> ec-fonts-mftraced-1_tsn
- change release to the _tsn suffix
- add to buildrequires the potrace package

* Sun Apr 11 2004 Han-Wen Nienhuys  <hanwen@xs4all.nl> - fonts-1
- Initial build.
