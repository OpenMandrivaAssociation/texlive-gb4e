# revision 19216
# category Package
# catalog-ctan /macros/latex/contrib/gb4e
# catalog-date 2010-07-03 20:09:25 +0200
# catalog-license lppl1.2
# catalog-version undef
Name:		texlive-gb4e
Version:	20180303
Release:	2
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

%description
Provides an environment for linguistic examples, tools for
glosses, and various other goodies. The code was developed from
the midnight and covington packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gb4e/cgloss4e.sty
%{_texmfdistdir}/tex/latex/gb4e/gb4e.sty
%doc %{_texmfdistdir}/doc/latex/gb4e/README
%doc %{_texmfdistdir}/doc/latex/gb4e/gb4e-doc.pdf
%doc %{_texmfdistdir}/doc/latex/gb4e/gb4e-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100703-2
+ Revision: 752188
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100703-1
+ Revision: 718524
- texlive-gb4e
- texlive-gb4e
- texlive-gb4e
- texlive-gb4e

