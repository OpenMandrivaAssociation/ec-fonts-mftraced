Name:           ec-fonts-mftraced
Version:        1.0.12
Release:        %mkrel 5
Epoch:          0
Summary:        Type1 PostScript fonts for TeX with european accents
License:        Public Domain
Group:          Publishing
URL:            http://lilypond.org/download/
Source0:        http://lilypond.org/download/old/ec-fonts-mftraced/ec-fonts-mftraced-%{version}.tar.gz
Requires(post): tetex
BuildRequires:  mftrace
BuildRequires:  potrace
BuildRequires:  tetex
BuildRequires:  tetex-dvips
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{epoch}:%{version}-%{release}-root

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

%clean
%{__rm} -rf %{buildroot}

%post
[ -x %{_bindir}/texhash ] && %{_bindir}/texhash 2>/dev/null

%files
%defattr(0644,root,root,0755)
%doc COPYING ChangeLog INSTALL LICENSE README VERSION
%{_datadir}/texmf/fonts/map/dvips/%{name}
%{_datadir}/texmf/fonts/type1/public/%{name}
%{_datadir}/texmf/fonts/tfm/public/%{name}
