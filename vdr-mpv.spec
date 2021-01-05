%global pname   mpv

Name:           vdr-%{pname}
Version:        0.2.1
Release:        1%{?dist}
Summary:        A mpv player plugin for VDR
License:        AGPLv3+
URL:            https://github.com/ua0lnj/vdr-plugin-mpv
Source0:        https://github.com/ua0lnj/vdr-plugin-mpv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= 2.0.0
BuildRequires:  mpv-libs-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-wm-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       lxrandr

%description 
vdr-mpv is a fork of the vdr-play plugin from Johns. It uses libmpv for playing
media (video, audio, picture) in VDR and also displays the VDR OSD (On Screen
Display) during playback.

%prep
%setup -qn vdr-plugin-%{pname}-%{version}

%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="-std=gnu++14 %{optflags} -fPIC" %{?_smp_mflags} all

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc README*
%license AGPL-3.0
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%changelog
* Tue Jan 05 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.2.1-1
- Use fork because its under maintenance
- Update to 0.2.1

* Mon Jan 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.0.4-19
- Rebuilt for new VDR API version
- Force C++14 as this code is not C++17 ready, needed for gcc11

* Mon Nov 23 2020 Leigh Scott <leigh123linux@gmail.com> - 0.0.4-18
- Rebuild for new mpv

* Wed Oct 21 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.0.4-17
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.0.4-16
- Rebuilt for new VDR API version

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.0.4-12
- Rebuilt for new VDR API version 2.4.1

* Sun Jun 30 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.0.4-11
- Rebuilt for new VDR API version

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.0.4-10
- Rebuilt for new VDR API version

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.0.4-8
- Add BR gcc-c++

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.0.4-7
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

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
