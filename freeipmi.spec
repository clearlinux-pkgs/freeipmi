#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0x3EFB7C4BE8303927 (chu11@llnl.gov)
#
Name     : freeipmi
Version  : 1.6.14
Release  : 19
URL      : https://mirrors.kernel.org/gnu/freeipmi/freeipmi-1.6.14.tar.gz
Source0  : https://mirrors.kernel.org/gnu/freeipmi/freeipmi-1.6.14.tar.gz
Source1  : https://mirrors.kernel.org/gnu/freeipmi/freeipmi-1.6.14.tar.gz.sig
Source2  : 3EFB7C4BE8303927.pkey
Summary  : FreeIPMI
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0+ GPL-3.0
Requires: freeipmi-bin = %{version}-%{release}
Requires: freeipmi-info = %{version}-%{release}
Requires: freeipmi-lib = %{version}-%{release}
Requires: freeipmi-license = %{version}-%{release}
Requires: freeipmi-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gnupg
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : pkgconfig(libgcrypt)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The FreeIPMI project provides "Remote-Console" (out-of-band) and
"System Management Software" (in-band) based on Intelligent
Platform Management Interface specification.

%package bin
Summary: bin components for the freeipmi package.
Group: Binaries
Requires: freeipmi-license = %{version}-%{release}

%description bin
bin components for the freeipmi package.


%package dev
Summary: dev components for the freeipmi package.
Group: Development
Requires: freeipmi-lib = %{version}-%{release}
Requires: freeipmi-bin = %{version}-%{release}
Provides: freeipmi-devel = %{version}-%{release}
Requires: freeipmi = %{version}-%{release}

%description dev
dev components for the freeipmi package.


%package doc
Summary: doc components for the freeipmi package.
Group: Documentation
Requires: freeipmi-man = %{version}-%{release}
Requires: freeipmi-info = %{version}-%{release}

%description doc
doc components for the freeipmi package.


%package info
Summary: info components for the freeipmi package.
Group: Default

%description info
info components for the freeipmi package.


%package lib
Summary: lib components for the freeipmi package.
Group: Libraries
Requires: freeipmi-license = %{version}-%{release}

%description lib
lib components for the freeipmi package.


%package license
Summary: license components for the freeipmi package.
Group: Default

%description license
license components for the freeipmi package.


%package man
Summary: man components for the freeipmi package.
Group: Default

%description man
man components for the freeipmi package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 3EFB7C4BE8303927' gpg.status
%setup -q -n freeipmi-1.6.14
cd %{_builddir}/freeipmi-1.6.14
pushd ..
cp -a freeipmi-1.6.14 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713287917
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1713287917
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/freeipmi
cp %{_builddir}/freeipmi-%{version}/COPYING %{buildroot}/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/freeipmi-%{version}/COPYING.ZRESEARCH %{buildroot}/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/freeipmi-%{version}/COPYING.bmc-watchdog %{buildroot}/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/freeipmi-%{version}/COPYING.ipmi-dcmi %{buildroot}/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/freeipmi-%{version}/COPYING.ipmi-fru %{buildroot}/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/freeipmi-%{version}/COPYING.ipmiconsole %{buildroot}/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/freeipmi-%{version}/COPYING.ipmidetect %{buildroot}/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/freeipmi-%{version}/COPYING.ipmimonitoring %{buildroot}/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/freeipmi-%{version}/COPYING.ipmiping %{buildroot}/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/freeipmi-%{version}/COPYING.ipmipower %{buildroot}/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/freeipmi-%{version}/COPYING.ipmiseld %{buildroot}/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/freeipmi-%{version}/COPYING.pstdout %{buildroot}/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/freeipmi-%{version}/COPYING.sunbmc %{buildroot}/usr/share/package-licenses/freeipmi/6213979ebc8593e5f131c3b495c9b7c717a6526d || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## Remove excluded files
rm -f %{buildroot}*/var/lib/freeipmi/ipckey
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/bmc-device
/V3/usr/bin/bmc-info
/V3/usr/bin/bmc-watchdog
/V3/usr/bin/ipmi-chassis
/V3/usr/bin/ipmi-config
/V3/usr/bin/ipmi-dcmi
/V3/usr/bin/ipmi-fru
/V3/usr/bin/ipmi-locate
/V3/usr/bin/ipmi-oem
/V3/usr/bin/ipmi-pet
/V3/usr/bin/ipmi-raw
/V3/usr/bin/ipmi-sel
/V3/usr/bin/ipmi-sensors
/V3/usr/bin/ipmiconsole
/V3/usr/bin/ipmidetect
/V3/usr/bin/ipmidetectd
/V3/usr/bin/ipmiping
/V3/usr/bin/ipmipower
/V3/usr/bin/ipmiseld
/V3/usr/bin/rmcpping
/usr/bin/bmc-config
/usr/bin/bmc-device
/usr/bin/bmc-info
/usr/bin/bmc-watchdog
/usr/bin/ipmi-chassis
/usr/bin/ipmi-chassis-config
/usr/bin/ipmi-config
/usr/bin/ipmi-console
/usr/bin/ipmi-dcmi
/usr/bin/ipmi-detect
/usr/bin/ipmi-fru
/usr/bin/ipmi-locate
/usr/bin/ipmi-oem
/usr/bin/ipmi-pef-config
/usr/bin/ipmi-pet
/usr/bin/ipmi-ping
/usr/bin/ipmi-power
/usr/bin/ipmi-raw
/usr/bin/ipmi-sel
/usr/bin/ipmi-sensors
/usr/bin/ipmi-sensors-config
/usr/bin/ipmiconsole
/usr/bin/ipmidetect
/usr/bin/ipmidetectd
/usr/bin/ipmimonitoring
/usr/bin/ipmiping
/usr/bin/ipmipower
/usr/bin/ipmiseld
/usr/bin/pef-config
/usr/bin/rmcp-ping
/usr/bin/rmcpping

%files dev
%defattr(-,root,root,-)
/usr/include/freeipmi/api/ipmi-api.h
/usr/include/freeipmi/api/ipmi-chassis-cmds-api.h
/usr/include/freeipmi/api/ipmi-dcmi-cmds-api.h
/usr/include/freeipmi/api/ipmi-device-global-cmds-api.h
/usr/include/freeipmi/api/ipmi-event-cmds-api.h
/usr/include/freeipmi/api/ipmi-firmware-firewall-command-discovery-cmds-api.h
/usr/include/freeipmi/api/ipmi-fru-inventory-device-cmds-api.h
/usr/include/freeipmi/api/ipmi-lan-cmds-api.h
/usr/include/freeipmi/api/ipmi-messaging-support-cmds-api.h
/usr/include/freeipmi/api/ipmi-oem-intel-node-manager-cmds-api.h
/usr/include/freeipmi/api/ipmi-pef-and-alerting-cmds-api.h
/usr/include/freeipmi/api/ipmi-rmcpplus-support-and-payload-cmds-api.h
/usr/include/freeipmi/api/ipmi-sdr-repository-cmds-api.h
/usr/include/freeipmi/api/ipmi-sel-cmds-api.h
/usr/include/freeipmi/api/ipmi-sensor-cmds-api.h
/usr/include/freeipmi/api/ipmi-serial-modem-cmds-api.h
/usr/include/freeipmi/api/ipmi-sol-cmds-api.h
/usr/include/freeipmi/cmds/ipmi-bmc-watchdog-timer-cmds.h
/usr/include/freeipmi/cmds/ipmi-chassis-cmds.h
/usr/include/freeipmi/cmds/ipmi-dcmi-cmds.h
/usr/include/freeipmi/cmds/ipmi-dcmi-oem-cmds.h
/usr/include/freeipmi/cmds/ipmi-device-global-cmds.h
/usr/include/freeipmi/cmds/ipmi-event-cmds.h
/usr/include/freeipmi/cmds/ipmi-firmware-firewall-command-discovery-cmds.h
/usr/include/freeipmi/cmds/ipmi-fru-inventory-device-cmds.h
/usr/include/freeipmi/cmds/ipmi-lan-cmds.h
/usr/include/freeipmi/cmds/ipmi-messaging-support-cmds.h
/usr/include/freeipmi/cmds/ipmi-oem-intel-node-manager-cmds.h
/usr/include/freeipmi/cmds/ipmi-pef-and-alerting-cmds.h
/usr/include/freeipmi/cmds/ipmi-rmcpplus-support-and-payload-cmds.h
/usr/include/freeipmi/cmds/ipmi-sdr-repository-cmds.h
/usr/include/freeipmi/cmds/ipmi-sel-cmds.h
/usr/include/freeipmi/cmds/ipmi-sensor-cmds.h
/usr/include/freeipmi/cmds/ipmi-serial-modem-cmds.h
/usr/include/freeipmi/cmds/ipmi-sol-cmds.h
/usr/include/freeipmi/cmds/rmcp-cmds.h
/usr/include/freeipmi/debug/ipmi-debug.h
/usr/include/freeipmi/driver/ipmi-inteldcmi-driver.h
/usr/include/freeipmi/driver/ipmi-kcs-driver.h
/usr/include/freeipmi/driver/ipmi-openipmi-driver.h
/usr/include/freeipmi/driver/ipmi-ssif-driver.h
/usr/include/freeipmi/driver/ipmi-sunbmc-driver.h
/usr/include/freeipmi/fiid/fiid.h
/usr/include/freeipmi/freeipmi.h
/usr/include/freeipmi/fru/ipmi-fru.h
/usr/include/freeipmi/interface/ipmi-interface.h
/usr/include/freeipmi/interface/ipmi-ipmb-interface.h
/usr/include/freeipmi/interface/ipmi-kcs-interface.h
/usr/include/freeipmi/interface/ipmi-lan-interface.h
/usr/include/freeipmi/interface/ipmi-rmcpplus-interface.h
/usr/include/freeipmi/interface/rmcp-interface.h
/usr/include/freeipmi/interpret/ipmi-interpret.h
/usr/include/freeipmi/locate/ipmi-locate.h
/usr/include/freeipmi/payload/ipmi-sol-payload.h
/usr/include/freeipmi/record-format/ipmi-cipher-suite-record-format.h
/usr/include/freeipmi/record-format/ipmi-fru-dimmspd-record-format.h
/usr/include/freeipmi/record-format/ipmi-fru-information-record-format.h
/usr/include/freeipmi/record-format/ipmi-fru-oem-record-format.h
/usr/include/freeipmi/record-format/ipmi-platform-event-trap-record-format.h
/usr/include/freeipmi/record-format/ipmi-sdr-oem-record-format.h
/usr/include/freeipmi/record-format/ipmi-sdr-record-format.h
/usr/include/freeipmi/record-format/ipmi-sel-oem-record-format.h
/usr/include/freeipmi/record-format/ipmi-sel-record-format.h
/usr/include/freeipmi/record-format/oem/ipmi-fru-wistron-oem-record-format.h
/usr/include/freeipmi/record-format/oem/ipmi-fru-xilinx-oem-record-format.h
/usr/include/freeipmi/record-format/oem/ipmi-sdr-oem-intel-node-manager-record-format.h
/usr/include/freeipmi/record-format/oem/ipmi-sdr-oem-intel-record-format.h
/usr/include/freeipmi/record-format/oem/ipmi-sel-oem-intel-record-format.h
/usr/include/freeipmi/record-format/oem/ipmi-sel-oem-linux-kernel-record-format.h
/usr/include/freeipmi/sdr/ipmi-sdr-oem.h
/usr/include/freeipmi/sdr/ipmi-sdr.h
/usr/include/freeipmi/sdr/oem/ipmi-sdr-oem-intel-node-manager.h
/usr/include/freeipmi/sel/ipmi-sel.h
/usr/include/freeipmi/sensor-read/ipmi-sensor-read.h
/usr/include/freeipmi/spec/ipmi-authentication-type-spec.h
/usr/include/freeipmi/spec/ipmi-channel-spec.h
/usr/include/freeipmi/spec/ipmi-cmd-dcmi-spec.h
/usr/include/freeipmi/spec/ipmi-cmd-spec.h
/usr/include/freeipmi/spec/ipmi-comp-code-dcmi-spec.h
/usr/include/freeipmi/spec/ipmi-comp-code-oem-spec.h
/usr/include/freeipmi/spec/ipmi-comp-code-spec.h
/usr/include/freeipmi/spec/ipmi-device-types-oem-spec.h
/usr/include/freeipmi/spec/ipmi-device-types-spec.h
/usr/include/freeipmi/spec/ipmi-entity-ids-spec.h
/usr/include/freeipmi/spec/ipmi-event-reading-type-code-oem-spec.h
/usr/include/freeipmi/spec/ipmi-event-reading-type-code-spec.h
/usr/include/freeipmi/spec/ipmi-fru-chassis-types-spec.h
/usr/include/freeipmi/spec/ipmi-fru-language-codes-spec.h
/usr/include/freeipmi/spec/ipmi-iana-enterprise-numbers-spec.h
/usr/include/freeipmi/spec/ipmi-ipmb-lun-spec.h
/usr/include/freeipmi/spec/ipmi-jedec-manufacturer-identification-code-spec.h
/usr/include/freeipmi/spec/ipmi-lan-configuration-parameters-oem-spec.h
/usr/include/freeipmi/spec/ipmi-lan-configuration-parameters-spec.h
/usr/include/freeipmi/spec/ipmi-netfn-oem-spec.h
/usr/include/freeipmi/spec/ipmi-netfn-spec.h
/usr/include/freeipmi/spec/ipmi-oem-spec.h
/usr/include/freeipmi/spec/ipmi-pef-configuration-parameters-oem-spec.h
/usr/include/freeipmi/spec/ipmi-pef-configuration-parameters-spec.h
/usr/include/freeipmi/spec/ipmi-privilege-level-spec.h
/usr/include/freeipmi/spec/ipmi-product-id-spec.h
/usr/include/freeipmi/spec/ipmi-rmcpplus-status-spec.h
/usr/include/freeipmi/spec/ipmi-sensor-and-event-code-tables-oem-spec.h
/usr/include/freeipmi/spec/ipmi-sensor-and-event-code-tables-spec.h
/usr/include/freeipmi/spec/ipmi-sensor-numbers-oem-spec.h
/usr/include/freeipmi/spec/ipmi-sensor-types-oem-spec.h
/usr/include/freeipmi/spec/ipmi-sensor-types-spec.h
/usr/include/freeipmi/spec/ipmi-sensor-units-spec.h
/usr/include/freeipmi/spec/ipmi-serial-modem-configuration-parameters-oem-spec.h
/usr/include/freeipmi/spec/ipmi-serial-modem-configuration-parameters-spec.h
/usr/include/freeipmi/spec/ipmi-slave-address-oem-spec.h
/usr/include/freeipmi/spec/ipmi-slave-address-spec.h
/usr/include/freeipmi/spec/ipmi-sol-configuration-parameters-oem-spec.h
/usr/include/freeipmi/spec/ipmi-sol-configuration-parameters-spec.h
/usr/include/freeipmi/spec/ipmi-system-boot-option-parameters-oem-spec.h
/usr/include/freeipmi/spec/ipmi-system-boot-option-parameters-spec.h
/usr/include/freeipmi/spec/ipmi-system-info-parameters-oem-spec.h
/usr/include/freeipmi/spec/ipmi-system-info-parameters-spec.h
/usr/include/freeipmi/spec/ipmi-system-software-id-spec.h
/usr/include/freeipmi/spec/ipmi-timestamp-spec.h
/usr/include/freeipmi/spec/oem/ipmi-cmd-oem-dell-spec.h
/usr/include/freeipmi/spec/oem/ipmi-cmd-oem-fujitsu-spec.h
/usr/include/freeipmi/spec/oem/ipmi-cmd-oem-gigabyte-spec.h
/usr/include/freeipmi/spec/oem/ipmi-cmd-oem-ibm-spec.h
/usr/include/freeipmi/spec/oem/ipmi-cmd-oem-intel-node-manager-spec.h
/usr/include/freeipmi/spec/oem/ipmi-cmd-oem-intel-spec.h
/usr/include/freeipmi/spec/oem/ipmi-cmd-oem-inventec-spec.h
/usr/include/freeipmi/spec/oem/ipmi-cmd-oem-quanta-spec.h
/usr/include/freeipmi/spec/oem/ipmi-cmd-oem-sun-microsystems-spec.h
/usr/include/freeipmi/spec/oem/ipmi-cmd-oem-supermicro-spec.h
/usr/include/freeipmi/spec/oem/ipmi-cmd-oem-wistron-spec.h
/usr/include/freeipmi/spec/oem/ipmi-comp-code-oem-dell-spec.h
/usr/include/freeipmi/spec/oem/ipmi-comp-code-oem-fujitsu-spec.h
/usr/include/freeipmi/spec/oem/ipmi-comp-code-oem-intel-node-manager-spec.h
/usr/include/freeipmi/spec/oem/ipmi-comp-code-oem-intel-spec.h
/usr/include/freeipmi/spec/oem/ipmi-comp-code-oem-wistron-spec.h
/usr/include/freeipmi/spec/oem/ipmi-event-reading-type-code-oem-dell-spec.h
/usr/include/freeipmi/spec/oem/ipmi-event-reading-type-code-oem-hp-spec.h
/usr/include/freeipmi/spec/oem/ipmi-event-reading-type-code-oem-intel-node-manager-spec.h
/usr/include/freeipmi/spec/oem/ipmi-event-reading-type-code-oem-intel-spec.h
/usr/include/freeipmi/spec/oem/ipmi-event-reading-type-code-oem-inventec-spec.h
/usr/include/freeipmi/spec/oem/ipmi-event-reading-type-code-oem-supermicro-spec.h
/usr/include/freeipmi/spec/oem/ipmi-lan-configuration-parameters-oem-inventec-spec.h
/usr/include/freeipmi/spec/oem/ipmi-lan-configuration-parameters-oem-wistron-spec.h
/usr/include/freeipmi/spec/oem/ipmi-netfn-oem-dell-spec.h
/usr/include/freeipmi/spec/oem/ipmi-netfn-oem-fujitsu-spec.h
/usr/include/freeipmi/spec/oem/ipmi-netfn-oem-ibm-spec.h
/usr/include/freeipmi/spec/oem/ipmi-netfn-oem-intel-spec.h
/usr/include/freeipmi/spec/oem/ipmi-netfn-oem-inventec-spec.h
/usr/include/freeipmi/spec/oem/ipmi-netfn-oem-quanta-spec.h
/usr/include/freeipmi/spec/oem/ipmi-netfn-oem-supermicro-spec.h
/usr/include/freeipmi/spec/oem/ipmi-netfn-oem-wistron-spec.h
/usr/include/freeipmi/spec/oem/ipmi-oem-dell-spec.h
/usr/include/freeipmi/spec/oem/ipmi-oem-fujitsu-spec.h
/usr/include/freeipmi/spec/oem/ipmi-oem-gigabyte-spec.h
/usr/include/freeipmi/spec/oem/ipmi-oem-ibm-spec.h
/usr/include/freeipmi/spec/oem/ipmi-oem-intel-spec.h
/usr/include/freeipmi/spec/oem/ipmi-oem-inventec-spec.h
/usr/include/freeipmi/spec/oem/ipmi-oem-quanta-spec.h
/usr/include/freeipmi/spec/oem/ipmi-oem-sun-microsystems-spec.h
/usr/include/freeipmi/spec/oem/ipmi-oem-supermicro-spec.h
/usr/include/freeipmi/spec/oem/ipmi-oem-wistron-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-dell-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-fujitsu-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-gigabyte-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-hp-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-intel-node-manager-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-intel-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-inventec-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-quanta-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-supermicro-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-and-event-code-tables-oem-wistron-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-numbers-oem-dell-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-numbers-oem-intel-node-manager-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-numbers-oem-intel-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-numbers-oem-inventec-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-numbers-oem-quanta-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-numbers-oem-wistron-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-dell-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-fujitsu-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-hp-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-intel-node-manager-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-intel-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-inventec-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-supermicro-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sensor-types-oem-wistron-spec.h
/usr/include/freeipmi/spec/oem/ipmi-slave-address-oem-intel-spec.h
/usr/include/freeipmi/spec/oem/ipmi-slave-address-oem-inventec-spec.h
/usr/include/freeipmi/spec/oem/ipmi-slave-address-oem-linux-kernel-spec.h
/usr/include/freeipmi/spec/oem/ipmi-slave-address-oem-quanta-spec.h
/usr/include/freeipmi/spec/oem/ipmi-slave-address-oem-wistron-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sol-configuration-parameters-oem-inventec-spec.h
/usr/include/freeipmi/spec/oem/ipmi-sol-configuration-parameters-oem-wistron-spec.h
/usr/include/freeipmi/spec/oem/ipmi-system-info-parameters-oem-dell-spec.h
/usr/include/freeipmi/spec/oem/ipmi-system-info-parameters-oem-wistron-spec.h
/usr/include/freeipmi/templates/ipmi-bmc-watchdog-timer-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-chassis-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-cipher-suite-record-format-templates.h
/usr/include/freeipmi/templates/ipmi-dcmi-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-device-global-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-event-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-firmware-firewall-command-discovery-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-fru-dimmspd-record-format-templates.h
/usr/include/freeipmi/templates/ipmi-fru-information-record-format-templates.h
/usr/include/freeipmi/templates/ipmi-fru-inventory-device-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-ipmb-interface-templates.h
/usr/include/freeipmi/templates/ipmi-kcs-interface-templates.h
/usr/include/freeipmi/templates/ipmi-lan-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-lan-interface-templates.h
/usr/include/freeipmi/templates/ipmi-messaging-support-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-oem-intel-node-manager-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-pef-and-alerting-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-rmcpplus-interface-templates.h
/usr/include/freeipmi/templates/ipmi-rmcpplus-support-and-payload-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-sdr-record-format-templates.h
/usr/include/freeipmi/templates/ipmi-sdr-repository-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-sel-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-sel-record-format-templates.h
/usr/include/freeipmi/templates/ipmi-sensor-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-serial-modem-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-sol-cmds-templates.h
/usr/include/freeipmi/templates/ipmi-sol-payload-templates.h
/usr/include/freeipmi/templates/oem/ipmi-sdr-oem-intel-node-manager-record-format-templates.h
/usr/include/freeipmi/templates/rmcp-cmds-templates.h
/usr/include/freeipmi/templates/rmcp-interface-templates.h
/usr/include/freeipmi/util/ipmi-channel-util.h
/usr/include/freeipmi/util/ipmi-cipher-suite-util.h
/usr/include/freeipmi/util/ipmi-dcmi-util.h
/usr/include/freeipmi/util/ipmi-device-types-util.h
/usr/include/freeipmi/util/ipmi-entity-ids-util.h
/usr/include/freeipmi/util/ipmi-error-dcmi-util.h
/usr/include/freeipmi/util/ipmi-error-util.h
/usr/include/freeipmi/util/ipmi-iana-enterprise-numbers-util.h
/usr/include/freeipmi/util/ipmi-ipmb-util.h
/usr/include/freeipmi/util/ipmi-jedec-manufacturer-identification-code-util.h
/usr/include/freeipmi/util/ipmi-lan-util.h
/usr/include/freeipmi/util/ipmi-outofband-util.h
/usr/include/freeipmi/util/ipmi-rmcpplus-util.h
/usr/include/freeipmi/util/ipmi-sensor-and-event-code-tables-util.h
/usr/include/freeipmi/util/ipmi-sensor-util.h
/usr/include/freeipmi/util/ipmi-timestamp-util.h
/usr/include/freeipmi/util/ipmi-util.h
/usr/include/freeipmi/util/rmcp-util.h
/usr/include/ipmi_monitoring.h
/usr/include/ipmi_monitoring_bitmasks.h
/usr/include/ipmi_monitoring_offsets.h
/usr/include/ipmiconsole.h
/usr/include/ipmidetect.h
/usr/lib64/libfreeipmi.so
/usr/lib64/libipmiconsole.so
/usr/lib64/libipmidetect.so
/usr/lib64/libipmimonitoring.so
/usr/lib64/pkgconfig/libfreeipmi.pc
/usr/lib64/pkgconfig/libipmiconsole.pc
/usr/lib64/pkgconfig/libipmidetect.pc
/usr/lib64/pkgconfig/libipmimonitoring.pc
/usr/share/man/man3/libfreeipmi.3
/usr/share/man/man3/libipmiconsole.3
/usr/share/man/man3/libipmidetect.3
/usr/share/man/man3/libipmimonitoring.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/freeipmi/*

%files info
%defattr(0644,root,root,0755)
/usr/share/info/freeipmi-faq.info

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libfreeipmi.so.17.2.12
/V3/usr/lib64/libipmiconsole.so.2.3.6
/V3/usr/lib64/libipmidetect.so.0.0.1
/V3/usr/lib64/libipmimonitoring.so.6.0.9
/usr/lib64/libfreeipmi.so.17
/usr/lib64/libfreeipmi.so.17.2.12
/usr/lib64/libipmiconsole.so.2
/usr/lib64/libipmiconsole.so.2.3.6
/usr/lib64/libipmidetect.so.0
/usr/lib64/libipmidetect.so.0.0.1
/usr/lib64/libipmimonitoring.so.6
/usr/lib64/libipmimonitoring.so.6.0.9

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/freeipmi/6213979ebc8593e5f131c3b495c9b7c717a6526d
/usr/share/package-licenses/freeipmi/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/bmc-config.conf.5
/usr/share/man/man5/freeipmi.conf.5
/usr/share/man/man5/freeipmi_interpret_sel.conf.5
/usr/share/man/man5/freeipmi_interpret_sensor.conf.5
/usr/share/man/man5/ipmi-config.conf.5
/usr/share/man/man5/ipmi_monitoring_sensors.conf.5
/usr/share/man/man5/ipmiconsole.conf.5
/usr/share/man/man5/ipmidetect.conf.5
/usr/share/man/man5/ipmidetectd.conf.5
/usr/share/man/man5/ipmimonitoring.conf.5
/usr/share/man/man5/ipmimonitoring_sensors.conf.5
/usr/share/man/man5/ipmipower.conf.5
/usr/share/man/man5/ipmiseld.conf.5
/usr/share/man/man5/libipmiconsole.conf.5
/usr/share/man/man5/libipmimonitoring.conf.5
/usr/share/man/man7/freeipmi.7
/usr/share/man/man8/bmc-config.8
/usr/share/man/man8/bmc-device.8
/usr/share/man/man8/bmc-info.8
/usr/share/man/man8/bmc-watchdog.8
/usr/share/man/man8/ipmi-chassis-config.8
/usr/share/man/man8/ipmi-chassis.8
/usr/share/man/man8/ipmi-config.8
/usr/share/man/man8/ipmi-console.8
/usr/share/man/man8/ipmi-dcmi.8
/usr/share/man/man8/ipmi-detect.8
/usr/share/man/man8/ipmi-fru.8
/usr/share/man/man8/ipmi-locate.8
/usr/share/man/man8/ipmi-oem.8
/usr/share/man/man8/ipmi-pef-config.8
/usr/share/man/man8/ipmi-pet.8
/usr/share/man/man8/ipmi-ping.8
/usr/share/man/man8/ipmi-power.8
/usr/share/man/man8/ipmi-raw.8
/usr/share/man/man8/ipmi-sel.8
/usr/share/man/man8/ipmi-sensors-config.8
/usr/share/man/man8/ipmi-sensors.8
/usr/share/man/man8/ipmiconsole.8
/usr/share/man/man8/ipmidetect.8
/usr/share/man/man8/ipmidetectd.8
/usr/share/man/man8/ipmimonitoring.8
/usr/share/man/man8/ipmiping.8
/usr/share/man/man8/ipmipower.8
/usr/share/man/man8/ipmiseld.8
/usr/share/man/man8/pef-config.8
/usr/share/man/man8/rmcp-ping.8
/usr/share/man/man8/rmcpping.8
