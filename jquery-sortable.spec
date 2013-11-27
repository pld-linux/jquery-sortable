%define		plugin	sortable
Summary:	A flexible, opinionated sorting plugin for jQuery
Name:		jquery-%{plugin}
Version:	0.9.11
Release:	1
License:	Modified BSD License
Group:		Applications/WWW
Source0:	https://github.com/johnny/jquery-sortable/archive/%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	66eff7676421f96dd05c58451ca4ec61
Source1:	http://johnny.github.io/jquery-sortable/js/jquery-sortable.js
# Source1-md5:	d51d97a074b2d39fdc27b85c2c1a7f3f
Source2:	http://johnny.github.io/jquery-sortable/js/jquery-sortable-min.js
# Source2-md5:	1f36199dcb98956681fefc63fa3babef
URL:		http://johnny.github.io/jquery-sortable/
Requires:	jquery >= 1.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
jQuery Sortable is a flexible, opinionated sorting plugin. It enables
items in a list (or table etc.) to be sorted horizontally and
vertically using the mouse. Supports nested lists and pure drag/drop
containers.

jQuery Sortable does not depend on jQuery UI and works well with
Twitter's Bootstrap (You can even sort the Bootstrap navigation).

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -q
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%build
grep 'jquery-sortable.js v%{version}' jquery-%{plugin}.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p jquery-%{plugin}-min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
cp -p jquery-%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.mkd LICENSE CHANGELOG TODO
%{_appdir}
