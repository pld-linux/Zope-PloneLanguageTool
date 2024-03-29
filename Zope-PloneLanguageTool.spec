%define		zope_subname	PloneLanguageTool
Summary:	Multilanguage content tool
Summary(pl.UTF-8):	Narzędzie dla wielojęzycznych dokumentów
Name:		Zope-%{zope_subname}
Version:	0.9
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://plone.org/products/plonelanguagetool/releases/%{version}/PloneLanguageTool-%{version}.tar.gz
# Source0-md5:	385425aa6f392d1d15de2d98e928e688
URL:		http://plone.org/Members/longsleep/I18NLayer/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMFPlone

Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PloneLanguageTool is a multilanguage content tool.

%description -l pl.UTF-8
PloneLanguageTool dostarcza narzędzia dla wielojęzycznych dokumentów.

%prep
%setup -q -n %{zope_subname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,skins,www,*.py,*.gif,version.txt} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt
%{_datadir}/%{name}
