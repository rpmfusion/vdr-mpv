%global pname   mpv

Name:           vdr-%{pname}
Version:        0.0.4
Release:        5%{?dist}
Summary:        A mpv player plugin for VDR
Group:          Applications/Multimedia
License:        AGPLv3+
URL:            http://projects.vdr-developer.org/projects/plg-mpv
Source0:        http://projects.vdr-developer.org/git/vdr-plugin-mpv.git/snapshot/vdr-plugin-mpv-%{version}.tar.bz2 

BuildRequires:  vdr-devel >= 2.0.0
BuildRequires:  libmpv-devel >= 0.9.2
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-wm-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       lxrandr

%description 
A mpv player plugin for VDR

%prep
%setup -qn vdr-plugin-%{pname}-%{version}

%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" %{?_smp_mflags} all

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc README*
%license AGPL-3.0
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%changelog
* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.0.4-5
- Rebuilt for vdr-2.4.0

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 30 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.0.4-1
- Update to 0.0.4

* Tue Jun 09 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.0.2-1
- initial build
