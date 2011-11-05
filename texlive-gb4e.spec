# revision 19216
# category Package
# catalog-ctan /macros/latex/contrib/gb4e
# catalog-date 2010-07-03 20:09:25 +0200
# catalog-license lppl1.2
# catalog-version undef
Name:		texlive-gb4e
Version:	20100703
Release:	1
Summary:	Linguistic tools
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gb4e
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gb4e.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gb4e.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides an environment for linguistic examples, tools for
glosses, and various other goodies. The code was developed from
the midnight and covington packages.

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
%{_texmfdistdir}/tex/latex/gb4e/cgloss4e.sty
%{_texmfdistdir}/tex/latex/gb4e/gb4e.sty
%doc %{_texmfdistdir}/doc/latex/gb4e/README
%doc %{_texmfdistdir}/doc/latex/gb4e/gb4e-doc.pdf
%doc %{_texmfdistdir}/doc/latex/gb4e/gb4e-doc.tex
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
