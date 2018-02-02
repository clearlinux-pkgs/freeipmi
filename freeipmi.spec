#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3EFB7C4BE8303927 (chu11@llnl.gov)
#
Name     : freeipmi
Version  : 1.5.7
Release  : 3
URL      : https://ftp.gnu.org/gnu/freeipmi/freeipmi-1.5.7.tar.gz
Source0  : https://ftp.gnu.org/gnu/freeipmi/freeipmi-1.5.7.tar.gz
Source99 : https://ftp.gnu.org/gnu/freeipmi/freeipmi-1.5.7.tar.gz.sig
Summary  : FreeIPMI
Group    : Development/Tools
License  : GPL-2.0+ GPL-3.0
Requires: freeipmi-bin
Requires: freeipmi-lib
Requires: freeipmi-doc
Requires: freeipmi-config
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : pkgconfig(systemd)
BuildRequires : systemd-dev

%description
The FreeIPMI project provides "Remote-Console" (out-of-band) and
"System Management Software" (in-band) based on Intelligent
Platform Management Interface specification.

%package bin
Summary: bin components for the freeipmi package.
Group: Binaries
Requires: freeipmi-config

%description bin
bin components for the freeipmi package.


%package config
Summary: config components for the freeipmi package.
Group: Default

%description config
config components for the freeipmi package.


%package dev
Summary: dev components for the freeipmi package.
Group: Development
Requires: freeipmi-lib
Requires: freeipmi-bin
Provides: freeipmi-devel

%description dev
dev components for the freeipmi package.


%package doc
Summary: doc components for the freeipmi package.
Group: Documentation

%description doc
doc components for the freeipmi package.


%package lib
Summary: lib components for the freeipmi package.
Group: Libraries

%description lib
lib components for the freeipmi package.


%prep
%setup -q -n freeipmi-1.5.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507222371
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1507222371
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%exclude /var/lib/freeipmi/ipckey

%files bin
%defattr(-,root,root,-)
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

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/bmc-watchdog.service
/usr/lib/systemd/system/ipmidetectd.service
/usr/lib/systemd/system/ipmiseld.service

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
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
/usr/lib64/libfreeipmi.so
/usr/lib64/libipmiconsole.so
/usr/lib64/libipmidetect.so
/usr/lib64/libipmimonitoring.so
/usr/lib64/pkgconfig/libfreeipmi.pc
/usr/lib64/pkgconfig/libipmiconsole.pc
/usr/lib64/pkgconfig/libipmidetect.pc
/usr/lib64/pkgconfig/libipmimonitoring.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/freeipmi/*
%doc /usr/share/info/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfreeipmi.so.17
/usr/lib64/libfreeipmi.so.17.1.4
/usr/lib64/libipmiconsole.so.2
/usr/lib64/libipmiconsole.so.2.3.4
/usr/lib64/libipmidetect.so.0
/usr/lib64/libipmidetect.so.0.0.0
/usr/lib64/libipmimonitoring.so.6
/usr/lib64/libipmimonitoring.so.6.0.6
