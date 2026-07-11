%global tl_name metalogox
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.07
Release:	%{tl_revision}.1
Summary:	Adjust TeX logos, with font detection
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/metalogox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metalogox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metalogox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/metalogox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package extends the metalogo package to automatically adjust the
appearance of the logos TeX, LaTeX, LaTeX2e, XeLaTeX, and LuaLaTeX,
depending on the font detected or the option given to metalogox. Most of
the serif and sans fonts listed at The LaTeX Font Catalogue are
supported. The package also supports the hologo and hvlogos packages.

