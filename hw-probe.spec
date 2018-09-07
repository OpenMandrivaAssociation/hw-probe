%define debug_package %{nil}

Summary:	Hardware Probe Tool
Name:		hw-probe
Version:	1.4
Release:	1
Group:		System/Base
License:	GPLv1+ or LGPLv2+
URL:		https://github.com/linuxhw/hw-probe
Source0:	%{name}-%{version}.tar.gz
Requires:	hwinfo
Requires:	dmidecode
Requires:	pciutils
Requires:	usbutils
Requires:	pnputils
Requires:	curl
Requires:	perl
Requires:	hdparm
Requires:	smartmontools
Requires:	inxi
Requires:	pnputils

%description
A tool to probe for hardware, check its operability and load result
to http://linux-hardware.org .

%prep
%setup -q

%build
# Nothing to build yet

%install
mkdir -p %{buildroot}%{_prefix}
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}

%files
%doc README
%{_bindir}/%{name}
