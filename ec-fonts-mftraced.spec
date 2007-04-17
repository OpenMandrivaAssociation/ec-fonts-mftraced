%define version 1.0.9
%define release 1mdk

Summary:	TeX EC fonts, PostScript Type1 format
Summary:	Type1 PostScript fonts for TeX with european accents
Name:		ec-fonts-mftraced
Version:	%{version}
Release:	%{release}
License:	Public Domain
Group:		Publishing
URL:		http://www.xs4all.nl/~hanwen/ec-mftrace/
Source0:	http://lilypond.org/download/fonts/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	mftrace >= 1.0.36-2mdk
BuildRequires:	tetex potrace
Prereq:		tetex
BuildArch:	noarch

%description
These are Type1 renderings of the EC variants of the standard CMR
family.

%prep
%setup -q

%build
make ./tfm.make
make

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}%{_prefix}

# handle doc files in %%doc instead
rm -rf %{buildroot}%{_docdir}

%post
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 2>/dev/null

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog README LICENSE
%{_datadir}/texmf/fonts/type1/public/%{name}
%{_datadir}/texmf/fonts/tfm/public/%{name}
%{_datadir}/texmf/dvips/%{name}
