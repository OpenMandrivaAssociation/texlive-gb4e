Name:		texlive-gb4e
Version:	19216
Release:	2
Summary:	Linguistic tools
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gb4e
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gb4e.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gb4e.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
