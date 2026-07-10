%global tl_name gb4e
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Linguistic tools
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gb4e
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gb4e.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gb4e.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides an environment for linguistic examples, tools for glosses, and
various other goodies. The code was developed from the midnight and
covington packages.

