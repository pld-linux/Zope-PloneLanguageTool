%include	/usr/lib/rpm/macros.python
%define		zope_subname	PloneLanguageTool
Summary:	Multilanguage content tool
Summary(pl):	Narzêdzie dla wielojêzykowych dokumentów
Name:		Zope-%{zope_subname}
Version:	0.3.1
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/collective/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	35384a1383d9b611cbfd3c7b759c03a7
URL:		http://plone.org/Members/longsleep/I18NLayer/
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	Zope-CMFPlone

Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PloneLanguageTool is a multilanguage content tool.

%description -l pl
PloneLanguageTool dostarcza narzêdzia dla wielojêzykowych dokumentów.

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
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc ChangeLog CREDITS.txt
%{_datadir}/%{name}
