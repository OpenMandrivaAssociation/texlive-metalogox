Name:		texlive-metalogox
Version:	69497
Release:	1
Summary:	Adjust TeX logos, with font detection
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/metalogox
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metalogox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metalogox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metalogox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package extends the metalogo package to automatically
adjust the appearance of the logos TeX, LaTeX, LaTeX2e,
XeLaTeX, and LuaLaTeX, depending on the font detected or the
option given to metalogox. Most of the serif and sans fonts
listed at The LaTeX Font Catalogue are supported. The package
depends on metalogo, xparse, and etoolbox.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/metalogox
%{_texmfdistdir}/tex/latex/metalogox
%doc %{_texmfdistdir}/doc/latex/metalogox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
