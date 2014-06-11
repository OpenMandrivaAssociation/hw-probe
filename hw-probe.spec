Summary:	ROSA Hardware Probe Tool
Name:		hw-probe
Version:	0.1
Release:	1
Group:		Development/Other
License:	GPLv1+ or LGPLv2+
URL:		http://hw.rosalinux.ru
Source0:	rosa-hw-probe-%{version}.tar.gz
Requires:	hwinfo
Requires:	pciutils
Requires:   usbutils
Requires:   dmidecode
Requires:   curl
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%define debug_package %{nil}

%description
A tool to probe for hardware, check its operability and load result
to the ROSA hardware DB.

%prep
%setup -q -n rosa-hw-probe-%{version}
chmod 0644 README

%build
# Nothing to build yet

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{_bindir}/%{name}
