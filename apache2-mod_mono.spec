#
# spec file for package apache2-mod_mono
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           apache2-mod_mono
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
%define apxs /usr/bin/apxs
%define apache2_sysconfdir %(%{apxs} -q PREFIX)/conf.d
%else
%define apxs /usr/sbin/apxs2
%define apache2_sysconfdir %(%{apxs} -q SYSCONFDIR)/conf.d
%endif
Obsoletes:      mod_mono
%define modname mod_mono
%define apache2_libexecdir %(%{apxs} -q LIBEXECDIR)
%define apache_mmn        %(MMN=$(%{apxs} -q LIBEXECDIR)_MMN; test -x $MMN && $MMN)
Url:            http://go-mono.com/
Version:        3.12
Release:        0
Summary:        Run ASP.NET Pages on Unix with Apache and Mono
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
Source:         %{modname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       mod_mono = %{version}-%{release}
# This must be manually entered according to xsp's protocol version
Requires:       xsp >= %{version}
BuildRequires:  libtool
############### Suse based options
%if 0%{?suse_version}
BuildRequires:  pkg-config
BuildRequires:  apache2-devel
BuildRequires:  mono-devel
Requires:       %{apache_mmn}
Requires:       apache2
%if %{suse_version} >= 1010
BuildRequires:  libapr-util1-devel
%endif
%if %{sles_version} == 9
BuildRequires:  pkgconfig
%endif
%endif
############### redhat based options
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos}
BuildRequires:  pkgconfig
BuildRequires:  httpd-devel
BuildRequires:  pkgconfig
Requires:       httpd
%endif

%description
mod_mono is a module that interfaces Apache with Mono and allows
running ASP.NET pages on Unix and Unix-like systems. To load the module
into Apache, run the command "a2enmod mono" as root.



%prep
%setup -n %{modname}-%{version} -q

%build
autoreconf -fiv
%if 0%{?sles_version} == 10
%define _with_remove_display --with-remove-display
%endif
%configure %_with_remove_display --disable-quiet-build
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT APXS_SYSCONFDIR="%{apache2_sysconfdir}"

%files
%defattr(-,root,root)
%{apache2_libexecdir}/*
%{apache2_sysconfdir}/*
%{_mandir}/man8/mod_mono.8*

%changelog

