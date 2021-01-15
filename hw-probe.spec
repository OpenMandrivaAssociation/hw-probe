%define debug_package %{nil}

Summary:	Check operability of computer hardware and find drivers
Name:		hw-probe
Version:	1.5
Release:	1
Group:		System/Base
License:	LGPLv2+
URL:		https://github.com/linuxhw/hw-probe
Source0:	%{name}-%{version}.tar.gz
Requires:	hwinfo
Requires:	dmidecode
Requires:	pciutils
Requires:	usbutils
Requires:	curl
Requires:	perl
Requires:	hdparm
Requires:	smartmontools
Requires:	inxi
Requires:	perl-Digest-SHA
Requires:	perl-libwww-perl
Requires:	edid-decode

%description
A tool to probe for hardware, check operability and find drivers
with the help of Linux Hardware Database.

WWW: http://linux-hardware.org/

%prep
%setup -q

%build
# Nothing to build yet

%install
mkdir -p %{buildroot}%{_prefix}
make install prefix=%{_prefix} DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}
