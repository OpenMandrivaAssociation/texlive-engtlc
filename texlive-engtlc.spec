# revision 17077
# category Package
# catalog-ctan /macros/latex/contrib/engtlc
# catalog-date 2010-03-16 18:34:36 +0100
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-engtlc
Version:	2.0
Release:	1
Summary:	Support for users in Telecommunications Engineering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/engtlc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engtlc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/engtlc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides a wide range of abbreviations for terms
used in Telecommunications Engineering.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/engtlc/engtlc.sty
%doc %{_texmfdistdir}/doc/latex/engtlc/README
%doc %{_texmfdistdir}/doc/latex/engtlc/eng_engtlc.pdf
%doc %{_texmfdistdir}/doc/latex/engtlc/engtlc.tex
%doc %{_texmfdistdir}/doc/latex/engtlc/ita_engtlc.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
