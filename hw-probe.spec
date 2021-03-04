%define debug_package %{nil}

Summary:	Check operability of computer hardware and find drivers
Name:		hw-probe
Version:	1.5
Release:	5
Group:		System/Base
License:	LGPLv2+
URL:		https://github.com/linuxhw/hw-probe
Source0:	https://github.com/linuxhw/hw-probe/archive/%{name}-%{version}.tar.gz
Source1:	hw-probe.service
Source2:	hw-probe.timer
BuildRequires:	systemd-macros
Requires:	hwinfo
Requires:	dmidecode
Requires:	pciutils
Requires:	usbutils
Requires:	curl
Requires:	perl
Requires:	perl(Digest::SHA)
Requires:	perl(Data::Dumper)
Requires:	hdparm
Requires:	smartmontools
Requires:	inxi
Requires:	edid-decode
Requires:	systemd-analyze
Requires:	kmod
Requires:	acpica
Recommends:	vulkan-tools
Recommends:	mesa-demos
Recommends:	libva-utils
Recommends:	xinput
Recommends:	i2c-tools
Recommends:	opensc
%ifarch %{x86_64} aarch64 %{riscv}
Recommends:	efivar
Recommends:	efibootmgr
%endif
Suggests:	avahi
%ifarch %{x86_64}
Suggests:	sane-backends
Suggests:	hplip
Suggests:	numactl
%endif
%systemd_requires

%description
A tool to probe for hardware, check operability and find drivers
with the help of Linux Hardware Database.

WWW: http://linux-hardware.org/

%prep
%autosetup -p1

%build
# Nothing to build yet

%install
mkdir -p %{buildroot}%{_prefix}
make install prefix=%{_prefix} DESTDIR=%{buildroot}

install -D -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.timer

install -d %{buildroot}%{_presetdir}
cat > %{buildroot}%{_presetdir}/86-%{name}.preset << EOF
enable %{name}.timer
EOF

%post
%systemd_post %{name}.timer

%postun
%systemd_postun %{name}.timer

%files
%{_bindir}/%{name}
%{_presetdir}/86-%{name}.preset
%{_unitdir}/%{name}.*
