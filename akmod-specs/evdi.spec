# SPDX-FileCopyrightText: 2022 ffgiff <ffgiff@gmail.com>
#
# SPDX-License-Identifier: MIT

Name:		evdi
Version:	1.14.10
Release:	1%{?dist}
Summary:	User-land library for Extensible Virtual Display Interface Kernel module
URL:		https://github.com/DisplayLink/evdi
%global evdi_commit 600ed4342a7251d4575ee4810756649f9e77cdf0
Source0:	%{url}/archive/%{evdi_commit}.tar.gz
License:	LGPLv2
BuildRequires:	libdrm-devel
Provides:	evdi-kmod-common = %{version}-%{release}
Provides:	libevdi = %{version}-%{release}

%files
%{_libdir}/libevdi.so
%{_libdir}/libevdi.so.1
%{_libdir}/libevdi.so.%{version}
%{_modprobedir}/evdi.conf
%doc evdi-%{evdi_commit}/docs/index.md

%global _hardened_build 1

%description
User-land library for Extensible Virtual Display Interface Kernel module

%prep
%setup -q -c evdi-%{evdi_commit}

%build
pushd evdi-%{evdi_commit}
CFLAGS="$RPM_OPT_FLAGS" %{make_build} -C library

%install
# Library
pushd evdi-%{evdi_commit}
LIBDIR=%{_libdir} %{make_install} -C library
mkdir -p %{buildroot}%{_modprobedir}
cat > %{buildroot}%{_modprobedir}/evdi.conf <<< "options evdi initial_device_count=4"


%changelog
* Sun May 18 2025 regulad <regulad@regulad.xyz> 1.14.10
- Latest 1.14.10 release
* Sun Jan 05 2025 ullebe1 <ullebe1@gmail.com> 1.14.8-1
- Latest 1.14.8-1 release
* Sun Jan 05 2025 ullebe1 <ullebe1@gmail.com> 1.14.7-1
- Latest 1.14.7-1 release
* Mon Oct 31 2022 ffgiff <ffgiff@gmail.com> 1.12.0-1
- Use latest devel commit to support 6.0
* Mon Jun 20 2022 ffgiff <ffgiff@gmail.com> 1.11.0-1
- Use latest tagged commit
* Tue Mar 22 2022 ffgiff <ffgiff@gmail.com> 1.10.1-1
- Use latest tagged commit
* Thu Feb 10 2022 ffgiff <ffgiff@gmail.com> 1.10.0-1
- Use latest tagged commit
* Wed Dec 01 2021 ffgiff <ffgiff@gmail.com> 1.9.1-3
- Use latest devel commit to support 5.15
* Sat Jul 24 2021 ffgiff <ffgiff@gmail.com> 1.9.1-2
- Use latest devel commit to support 5.13 and 5.14
* Sat May 01 2021 ffgiff <ffgiff@gmail.com> 1.9.1-1
- First version
