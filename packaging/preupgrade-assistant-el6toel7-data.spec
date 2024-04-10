%global pkg_name %{name}

Name:       preupgrade-assistant-el6toel7-data
Version:    0.20200704
Release:    2%{?dist}
Summary:    Static data about differences between systems.

Group:      System Environment/Libraries
License:    GPLv3+
Source0:    %{name}-%{version}.tar.gz
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
# URL: missing - Red Hat upstream and source URL is not available

# requires due to install path
Requires: preupgrade-assistant-el6toel7

%description
The package provides a set of static data about differences
between CentOS 6 and CentOS 7 systems

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p -m 755 $RPM_BUILD_ROOT%{_datadir}/doc/preupgrade-assistant-el6toel7-data
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/preupgrade/RHEL6_7/common
mv RHEL6_7/LICENSE $RPM_BUILD_ROOT%{_datadir}/doc/preupgrade-assistant-el6toel7-data/
mv RHEL6_7/* $RPM_BUILD_ROOT%{_datadir}/preupgrade/RHEL6_7/common

rm -rf $RPM_BUILD_ROOT%{_datadir}/preupgrade/RHEL5_*

find $RPM_BUILD_ROOT%{_datadir}/preupgrade/ -name "*.ignore" -delete
find $RPM_BUILD_ROOT%{_datadir}/preupgrade/ -name "*.log" -delete

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_datadir}/doc/preupgrade-assistant-el6toel7-data
%doc %{_datadir}/doc/preupgrade-assistant-el6toel7-data/LICENSE
%dir %{_datadir}/preupgrade/RHEL6_7/common
%{_datadir}/preupgrade/RHEL6_7/common/*

%changelog
* Fri Apr 5 2024 Yuriy Kohut <ykohut@almalinux.org> - 0.20200704-2
- use data with CentOS branding

* Thu Jul 28 2022 Petr Stodulka <pstodulk@redhat.com> - 0.20200704-1
- rebase to 0.20200704
- data for RHEL 6.10 -> 7.9
- Resolves: #2091519

* Tue Jan 16 2018 Petr Stodulka <pstodulk@redhat.com> - 0.20180503-1
- rebase to 0.20180503
- data for RHEL 6.10 -> 7.4
  Resolves: rhbz#1581662
