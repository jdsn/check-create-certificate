#
# spec file for package check-create-certificate
#
# Copyright 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# norootforbuild 


Name:           check-create-certificate
Version:        0.1
Release:        0
License:        GPLv2
Group:          Productivity/Networking/System
Summary:        A non-interactive script that creates an SSL certificate if it does not exist
Url:            http://gitorious.org/server-administration/check-create-certificate

Requires:       perl perl-base
Requires:       openssl

BuildRequires:  coreutils
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Source:         %{name}-%{version}.tar.bz2


%description
A script that checks for the existance of an SSL certificate or creates a new self signed one.
It runs non-interactively and uses either predefined values or automatically guesses the best values.

Authors:
--------
    J. Daniel Schmidt <jdsn@suse.de>


%prep

%setup -q

%build

%install
    mkdir -p ${RPM_BUILD_ROOT}/usr/sbin
    cp -a script/%{name} ${RPM_BUILD_ROOT}/usr/sbin

%clean
    rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,root)
%attr(0755,root,root) /usr/sbin/%{name}
