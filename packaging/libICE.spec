
Name:       libICE
Summary:    X.Org X11 libICE runtime library
Version:    1.0.7
Release:    2.25
Group:      System/Libraries
License:    MIT/X11
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source1001: packaging/libICE.manifest 
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(xorg-macros)


%description
The X.Org X11 ICE (Inter-Client Exchange) runtime library.


%package devel
Summary:    X.Org X11 libICE development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   xorg-x11-filesystem

%description devel
The X.Org X11 ICE (Inter-Client Exchange) development package.


%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .

%reconfigure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig







%files
%manifest libICE.manifest
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libICE.so.6
%{_libdir}/libICE.so.6.3.0
%exclude /usr/share/doc/libICE/ICElib.xml
%exclude /usr/share/doc/libICE/ice.xml


%files devel
%manifest libICE.manifest
%defattr(-,root,root,-)
%dir %{_includedir}/X11
%dir %{_includedir}/X11/ICE
%{_includedir}/X11/ICE/*.h
%{_libdir}/libICE.so
%{_libdir}/pkgconfig/ice.pc

