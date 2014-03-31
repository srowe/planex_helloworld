Summary: An example package
Name: helloworld
Version: 0.1
Release: 1
License: GPL
Group: Applications/System
Source: https://github.com/srowe/planex_helloworld/archive/v%{version}.tar.gz


%description
A very simple package to demonstrate planex.

%prep
%setup -q -n planex_%{name}-%{version}/%{name}

%install
rm -rf %{buildroot}
find . | cpio -pdmv %{buildroot}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/share/%{name}/README

%changelog
