%define		plugin	mobile
%define		subver	rc1
%define		rel		1
Summary:	jQuery Mobile: Touch-Optimized Web Framework for Smartphones & Tablets
Name:		jquery-%{plugin}
Version:	1.0
Release:	0.%{subver}.%{rel}
License:	MIT / GPL v2
Group:		Applications/WWW
Source0:	http://code.jquery.com/mobile/%{version}%{subver}/jquery.mobile-%{version}%{subver}.zip
# Source0-md5:	ddb843aad9da5446463275e96784527f
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
# install minified and original css/js
cp -p jquery.mobile-%{version}%{subver}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.mobile-%{version}%{subver}.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.css
cp -p jquery.mobile-%{version}%{subver}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
cp -p jquery.mobile-%{version}%{subver}.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.css

# versionless symlinks, to minified version
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
