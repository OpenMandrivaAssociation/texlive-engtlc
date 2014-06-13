# revision 28571
# category Package
# catalog-ctan /macros/latex/contrib/engtlc
# catalog-date 2012-12-18 12:17:57 +0100
# catalog-license lppl1.3
# catalog-version 3.2
Name:		texlive-engtlc
Version:	3.2
Release:	6
Summary:	Support for users in Telecommunications Engineering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/engtlc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engtlc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engtlc.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
