# TODO
# - package demos
%define		plugin	mobile
Summary:	jQuery Mobile: Touch-Optimized Web Framework for Smartphones & Tablets
Name:		jquery-%{plugin}
Version:	1.0
Release:	1
License:	MIT / GPL v2
Group:		Applications/WWW
Source0:	http://code.jquery.com/mobile/%{version}/jquery.mobile-%{version}.zip
# Source0-md5:	224e8512a157f83b9419b819e983b18a
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
%setup -q -n jquery.mobile-%{version}

# rename for better version diffs
mv jquery.mobile{-%{version},}.min.js
mv jquery.mobile{-%{version},}.min.css
mv jquery.mobile{-%{version},}.js
mv jquery.mobile{-%{version},}.css
mv jquery.mobile.structure{-%{version},}.css
mv jquery.mobile.structure{-%{version},}.min.css

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a images $RPM_BUILD_ROOT%{_appdir}
# install minified and original css/js
cp -p jquery.mobile.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p jquery.mobile.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.css
cp -p jquery.mobile.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
cp -p jquery.mobile.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.css
cp -p jquery.mobile.structure.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.structure-%{version}.min.css
cp -p jquery.mobile.structure.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.structure-%{version}.css

# versionless symlinks, to minified version
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.css
ln -s %{plugin}.structure-%{version}.min.css $RPM_BUILD_ROOT%{_appdir}/%{plugin}.structure.css

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
