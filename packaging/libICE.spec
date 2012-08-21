Summary: X.Org X11 ICE runtime library
Name: libICE
Version: 1.0.8
Release: 1
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires: xorg-x11-xtrans-devel >= 1.0.3-5

%description
The X.Org X11 ICE (Inter-Client Exchange) runtime library.

%package devel
Summary: X.Org X11 ICE development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The X.Org X11 ICE (Inter-Client Exchange) development package.

%prep
%setup -q

%build
%reconfigure --disable-static \
           LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libICE.so.6
%{_libdir}/libICE.so.6.3.0

%files devel
%defattr(-,root,root,-)
#%{_docdir}/%{name}
%{_includedir}/X11/ICE
%{_libdir}/libICE.so
%{_libdir}/pkgconfig/ice.pc
