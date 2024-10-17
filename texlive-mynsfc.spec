Name:		texlive-mynsfc
Version:	60280
Release:	2
Summary:	XeLaTeX template for writing the main body of NSFC proposals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mynsfc
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mynsfc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mynsfc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mynsfc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a XeLaTeX template for writing the main
body of National Natural Science Foundation of China (NSFC)
proposals, which are allowed to apply online. The package
defines styles of the outlines and uses BibLaTeX/biber for the
management of references.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/xelatex/mynsfc
%{_texmfdistdir}/tex/xelatex/mynsfc
%doc %{_texmfdistdir}/doc/xelatex/mynsfc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
