%global pname   mpv

# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 43
%global vdr_version 2.7.6
%elif 0%{?fedora} == 42
%global vdr_version 2.7.4
%else
%global vdr_version 2.6.9
%endif

Name:           vdr-%{pname}
Version:        1.8.1
Release:        5%{?dist}
Summary:        A mpv player plugin for VDR
License:        AGPL-3.0-or-later
URL:            https://github.com/ua0lnj/vdr-plugin-mpv
Source0:        https://github.com/ua0lnj/vdr-plugin-mpv/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  mpv-libs-devel
BuildRequires:  libdrm-devel
BuildRequires:  libxcb-devel
BuildRequires:	libX11-devel
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
%autosetup -p1 -n vdr-plugin-%{pname}-%{version}

%build
DRM_CFLAGS="$(pkg-config --cflags libdrm)"
%make_build CFLAGS="%{optflags} -fPIC $DRM_CFLAGS" CXXFLAGS="%{optflags} -fPIC $DRM_CFLAGS" all

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc README*
%license AGPL-3.0
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%changelog
* Sun Jul 27 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jun 21 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.8.1-4
- Rebuilt for new VDR API version 2.7.6

* Tue May 27 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.8.1-3
- Rebuilt for new VDR API version 2.7.5

* Sun Mar 16 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.8.1-2
- Rebuilt for new VDR API version 2.7.4

* Sat Mar 01 2025 Martin Gansser <martinkg@fedoraproject.org> - 1.8.1-1
- Update to 1.8.1

* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.7.4-2
- Rebuilt for new VDR API version 2.7.3

* Mon Sep 30 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.7.4-1
- Update to 1.7.4

* Fri Jul 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.7.3-1
- Rebuilt for new VDR API version 2.6.9
- Update to 1.7.3

* Fri Jul 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.7.2-2
- Update to 1.7.2
- Rebuilt for new VDR API version 2.6.8

* Sat Apr 27 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Sun Apr 21 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.6.1-2
- Rebuilt for new VDR API version

* Sun Mar 24 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 28 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.6.0-1
- Rebuilt for new VDR API version
- Update to 1.6.0

* Sun Jan 14 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.5.2-1
- Update to 1.5.2

* Tue Jan 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.5.0-1
- Rebuilt for new VDR API version
- Add BR gettext for rawhide
- Update to 1.5.0

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.4.4-1
- Update to 1.4.4

* Wed Mar 29 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2

* Sun Dec 18 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.1-2
- Rebuilt for new VDR API version

* Sat Dec 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.1-1
- Rebuilt for new VDR API version
- Update to 1.4.1

* Thu Nov 17 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3.4-3
- Rebuilt due to mpv update.

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Aug 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4

* Mon Apr 11 2022 Sérgio Basto <sergio@serjux.com> - 1.2.3-5
- Rebuilt for VDR 2.6.x

* Fri Feb 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.3-4
- Rebuilt for new VDR API version

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.2.3-3
- Rebuilt for new VDR API version

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Apr 26 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3
- Add DRM_CFLAGS
- Add BR libdrm-devel

* Wed Apr 14 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Sat Mar 27 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Mon Mar 22 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Thu Mar 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Wed Mar 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Sat Feb 13 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.5.2-1
- Update to 0.5.2

* Fri Feb 12 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 31 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Thu Jan 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Wed Jan 20 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Sat Jan 16 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0
- Add BR libX11-devel

* Wed Jan 06 2021 Martin Gansser <martinkg@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

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
