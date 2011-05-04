%define		plugin	mobile
%define		subver	a4.1
%define		rel		1
Summary:	jQuery Mobile: Touch-Optimized Web Framework for Smartphones & Tablets
Name:		jquery-%{plugin}
Version:	1.0
Release:	0.%{subver}.%{rel}
License:	MIT / GPL v2
Group:		Applications/WWW
Source0:	http://code.jquery.com/mobile/%{version}%{subver}/jquery.mobile-%{version}%{subver}.zip
# Source0-md5:	92fa39077c49d25d6a319ebf20fbfe0f
URL:		http://jquerymobile.com/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
A unified user interface system across all popular mobile device
platforms, built on the rock-solid jQuery and jQuery UI foundation.
Its lightweight code is built with progressive enhancement, and has a
flexible, easily themeable design.

%prep
%setup -q -n jquery.mobile-%{version}%{subver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a images $RPM_BUILD_ROOT%{_appdir}
cp -p jquery.mobile-*.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
cp -p jquery.mobile-*.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
