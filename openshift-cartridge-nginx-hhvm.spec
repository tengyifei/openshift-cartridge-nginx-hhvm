%global cartridgedir %{_libexecdir}/openshift/cartridges/nginx-hhvm
%global frameworkdir %{_libexecdir}/openshift/cartridges/nginx-hhvm

Name:          openshift-cartridge-nginx-hhvm
Version:       0.0.0.8
Release:       1%{?dist}
Summary:       HHVM cartridge
Group:         Development/Languages
License:       ASL 2.0
URL:           https://github.com/tengyifei/openshift-cartridge-nginx-hhvm
Source0:       https://github.com/tengyifei/origin-server/%{name}/%{name}-%{version}.tar.gz
Requires:      rubygem(openshift-origin-node)

#Obsoletes: openshift-origin-cartridge-php-5.3

%description
HHVM cartridge for openshift. (Cartridge Format V2)

%prep
%setup -q

%build

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__mkdir -p %{buildroot}%{cartridgedir}/versions/shared/configuration/etc/conf/

%files
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.md


%changelog
* Sat Jun 21 2014 Teng Yifei <tengyifei88@gmail.com> 0.0.0.3-1
- initial commit
