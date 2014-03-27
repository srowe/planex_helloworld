Summary: An example package
Name: helloworld
Version: 1.0
Release: 1
License: GPL
Group: Applications/System
Source: file:///root/helloworld.tar.bz2


%description
A very simple package to demonstrate planex.

%prep
%setup -n %{name}

%install
rm -rf %{buildroot}
find . | cpio -pdmv %{buildroot}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/share/%{name}/README

%changelog
