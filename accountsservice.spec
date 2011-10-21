%define _localstatedir %_var
%define _libexecdir %_prefix/libexec


Name: accountsservice
Version: 0.6.15
Release: alt1
Summary: D-Bus interfaces for querying and manipulating user account information

Group: System/Base
License: GPLv3+
Url: http://www.fedoraproject.org/wiki/Features/UserAccountDialog
#VCS: git://anongit.freedesktop.org/accountsservice

Source: %name-%version.tar
Patch1: %name-%version-%release.patch

BuildRequires: intltool
BuildRequires: glib2-devel libgio-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libpolkit1-devel
BuildRequires: gobject-introspection-devel

Requires: polkit
Requires: ConsoleKit
Requires: shadow-utils
Requires: lib%name = %version-%release

%package -n lib%name
Summary: Client-side library to talk to accountservice
Group: System/Libraries

%description -n lib%name
The libaccountsservice package contains a library that can
be used by applications that want to interact with the accountsservice
daemon.

%package -n lib%name-devel
Summary: Development files for accountsservice
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
The libaccountsservice-devel package contains headers and other
files needed to build applications that use accountsservice.

%description
The accountsservice project provides a set of D-Bus interfaces for
querying and manipulating user account information and an implementation
of these interfaces, based on the useradd, usermod and userdel commands.

%package -n lib%name-gir
Summary: GObject introspection data for the accountsservice library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the accountsservice library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the accountsservice library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %version-%release lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the accountsservice library

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure --disable-static --with-systemdsystemunitdir=%systemd_unitdir
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang accounts-service

%files -f accounts-service.lang
%doc COPYING README AUTHORS
%_sysconfdir/dbus-1/system.d/org.freedesktop.Accounts.conf
%_libexecdir/accounts-daemon
%_datadir/dbus-1/interfaces/org.freedesktop.Accounts.xml
%_datadir/dbus-1/interfaces/org.freedesktop.Accounts.User.xml
%_datadir/dbus-1/system-services/org.freedesktop.Accounts.service
%_datadir/polkit-1/actions/org.freedesktop.accounts.policy
%dir %_localstatedir/lib/AccountsService/
%dir %_localstatedir/lib/AccountsService/users
%dir %_localstatedir/lib/AccountsService/icons
%systemd_unitdir/accounts-daemon.service

%files -n lib%name
%_libdir/libaccountsservice.so.*

%files -n lib%name-gir
%_libdir/girepository-1.0/AccountsService-1.0.typelib

%files -n lib%name-devel
%_includedir/accountsservice-1.0
%_libdir/libaccountsservice.so
%_pkgconfigdir/*.pc

%files -n lib%name-gir-devel
%_datadir/gir-1.0/AccountsService-1.0.gir

%changelog
* Fri Oct 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.15-alt1
- 0.6.15

* Wed Sep 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.14-alt1
- 0.6.14

* Wed Aug 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.13-alt1
- 0.6.13

* Tue May 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.12-alt1
- pre 0.6.13

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.10-alt1
- 0.6.10

* Fri Apr 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.8-alt1
- 0.6.8
- use global %%systemd_unitdir macros

* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- initial build for ALT Linux Sisyphus
