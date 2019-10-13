%?mingw_package_header

Name:           mingw-libexif
Version:        0.6.21
Release:        2%{?dist}
Summary:        mingw port of tool for extracting extra information from image files

License:        LGPLv2+
URL:            http://libexif.sourceforge.net/
Source0:        http://downloads.sourceforge.net/libexif/libexif-%{version}.tar.bz2
Patch0:         41bd04234b104312f54d25822f68738ba8d7133d.patch
BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc, mingw64-gcc
BuildRequires:  mingw32-binutils, mingw64-binutils
BuildRequires:  autoconf, automake, libtool
BuildRequires:  gettext-devel,  mingw32-gettext
BuildRequires:  pkgconfig


%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.


# Win32
%package -n     mingw32-libexif
Summary:        32 Bit version of libexif for Windows

%description -n mingw32-libexif
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

This package contains development tools and libraries for use when
cross-compiling 32-bits Windows software in Fedora.


%package -n     mingw32-libexif-static
Summary:        Static library for mingw32-libexif development
Requires:       mingw32-libexif = %{version}-%{release}

%description -n mingw32-libexif-static
Static library for mingw32-libexif development.


# Win64
%package -n     mingw64-libexif
Summary:        64 Bit version of libexif for Windows

%description -n mingw64-libexif
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

This package contains development tools and libraries for use when
cross-compiling 64-bits Windows software in Fedora.


%package -n     mingw64-libexif-static
Summary:        Static library for mingw64-libexif development
Requires:       mingw64-libexif = %{version}-%{release}

%description -n mingw64-libexif-static
Static library for mingw64-libexif development.


%?mingw_debug_package


%prep
%setup -q -n libexif-%{version}
%patch0 -p1 


%build
autoreconf -fiv
%mingw_configure
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la -delete

rm -rf %{buildroot}%{_datadir}/doc/libexif
rm -rf doc/doxygen-output
iconv -f latin1 -t utf-8 < COPYING > COPYING.utf8; cp COPYING.utf8 COPYING
iconv -f latin1 -t utf-8 < README > README.utf8; cp README.utf8 README
rm -rf %{buildroot}%{mingw32_datadir}/doc/libexif/libexif-api.html
rm -rf %{buildroot}%{mingw64_datadir}/doc/libexif/libexif-api.html


# Win32
%files -n mingw32-libexif
%doc COPYING
%{mingw32_bindir}/libexif-12.dll*
%{mingw32_includedir}/libexif
%{mingw32_libdir}/libexif.dll.a
%{mingw32_libdir}/pkgconfig/libexif.pc
%{mingw32_datadir}/doc/libexif
%{mingw32_datadir}/locale/*/LC_MESSAGES/libexif-12.mo
%files -n mingw32-libexif-static
%{mingw32_libdir}/libexif.a

# Win64
%files -n mingw64-libexif
%doc COPYING
%{mingw64_bindir}/libexif-12.dll*
%{mingw64_includedir}/libexif
%{mingw64_libdir}/libexif.dll.a
%{mingw64_libdir}/pkgconfig/libexif.pc
%{mingw64_datadir}/doc/libexif

%files -n mingw64-libexif-static
%{mingw64_libdir}/libexif.a


%changelog
* Sun Oct 13 2019 Alec Leamas <leamas.alec@gmail.com> - 0.6.21-2
- rebuilt

* Fri Mar 01 2019 Alec Leamas <leamas.alec@gmail.com> - 0.6.21-1
- INitial release


