Summary:	SGML/Linuxdoc-SGML editing mode macros
Summary(pl):	Makra do tryb edycji dokumentów SGML/Linuxdoc-SGML
Name:		xemacs-sgml-pkg
%define 	srcname	sgml
Version:	1.08
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGML/Linuxdoc-SGML editing mode.

%description -l pl 
Makra do tryb edycji dokumentów SGML/Linuxdoc-SGML.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/sgml/ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/sgml/ChangeLog.gz
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
