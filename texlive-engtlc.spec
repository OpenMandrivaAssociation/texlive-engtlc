Name:		texlive-engtlc
Version:	28571
Release:	2
Summary:	Support for users in Telecommunications Engineering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/engtlc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engtlc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engtlc.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a wide range of abbreviations for terms
used in Telecommunications Engineering.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/engtlc/engtlc.sty
%doc %{_texmfdistdir}/doc/latex/engtlc/README
%doc %{_texmfdistdir}/doc/latex/engtlc/engtlc.pdf
%doc %{_texmfdistdir}/doc/latex/engtlc/engtlc.tex
%doc %{_texmfdistdir}/doc/latex/engtlc/itengtlc.pdf
%doc %{_texmfdistdir}/doc/latex/engtlc/itengtlc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
