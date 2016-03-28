%define		oname	QupZilla
%define		major	1
%define		libname	%mklibname %{oname} %{major}
%define		devname	%mklibname %{oname} -d
%define		snapshot 20160328

Summary:	Fast browser based on QtWebKit
Name:		qupzilla
Version:	1.9.0
%if 0%snapshot
Release:	0.%{snapshot}.1
Source0:	%{oname}-%{snapshot}.tar.xz
%else
Release:	6
Source0:	https://github.com/QupZilla/qupzilla/releases/download/v%{version}/%{oname}-%{version}.tar.xz
%endif
License:	GPLv3+ and BSD and LGPLv2.1 and GPLv2+ and MPL
Group:		Networking/WWW
Url:		http://www.qupzilla.org/
Patch0:		qupzilla-1.3.5-mdv-linking.patch
BuildRequires:	qt5-devel
BuildRequires:	qt5-linguist-tools
BuildRequires:	dos2unix
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5WebEngineWidgets)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5X11Extras)
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-plugins = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	qt5-qtbase-database-plugin-sqlite
Requires:	qt5-output-driver-default
Conflicts:	rosa-media-player-plugin

%description
QupZilla is a new and very fast QtWebKit browser. It aims to be a lightweight
web browser available through all major platforms. This project has been
originally started only for educational purposes. But from its start, QupZilla
has grown into a feature-rich browser.

QupZilla has all standard functions you expect from a web browser. It includes
bookmarks, history (both also in sidebar) and tabs. Above that, you can manage
RSS feeds with an included RSS reader, block ads with a builtin AdBlock plugin,
block Flash content with Click2Flash and edit the local CA Certificates
database with an SSL Manager.

QupZilla's main aim is to be a very fast and very stable QtWebKit browser
available to everyone. There are already a lot of QtWebKit browsers available,
but they are either bound to the KDE environment (rekonq), are not actively
developed or very unstable and miss important features. But there is missing
a multiplatform, modern and actively developed browser. QupZilla is trying
to fill this gap by providing a very stable browsing experience.

%files

#----------------------------------------------------------------------------

%package core
Summary:	%{oname} web browser core package
Group:		Networking/WWW

%description core
QupZilla is a new and very fast QtWebKit browser. It aims to be a lightweight
web browser available through all major platforms. This project has been
originally started only for educational purposes. But from its start, QupZilla
has grown into a feature-rich browser.

QupZilla has all standard functions you expect from a web browser. It includes
bookmarks, history (both also in sidebar) and tabs. Above that, you can manage
RSS feeds with an included RSS reader, block ads with a builtin AdBlock plugin,
block Flash content with Click2Flash and edit the local CA Certificates
database with an SSL Manager.

QupZilla's main aim is to be a very fast and very stable QtWebKit browser
available to everyone. There are already a lot of QtWebKit browsers available,
but they are either bound to the KDE environment (rekonq), are not actively
developed or very unstable and miss important features. But there is missing
a multiplatform, modern and actively developed browser. QupZilla is trying
to fill this gap by providing a very stable browsing experience.

%files core -f %{name}.lang
%doc AUTHORS COPYRIGHT FAQ README.md
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
%{_datadir}/bash-completion/completions/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/qupzilla.appdata.xml
%dir %{_datadir}/%{name}/locale
%dir %{_libdir}/qupzilla

#----------------------------------------------------------------------------

%package plugins
Summary:	Various plugins for %{oname} web browser
Group:		Networking/WWW
Requires:	%{name} = %{EVRD}

%description plugins
QupZilla Plugins are dynamically loaded shared libraries (*.so) that can extend
application in almost any way. This package contains the following plugins:

* Mouse Gestures
* Access Keys Navigation
* Personal Information Manager
* GreaseMonkey

%files plugins
%{_libdir}/qupzilla/*.so

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	%{oname} shared library
Group:		System/Libraries

%description -n %{libname}
Shared library used by %{oname} web browser.

%files -n %{libname}
%{_libdir}/lib%{oname}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	%{oname} development files
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for %{libname} library.

%files -n %{devname}
%{_libdir}/lib%{oname}.so

#----------------------------------------------------------------------------

%prep
%if 0%{snapshot}
%setup -q -n %{oname}-%{snapshot}
%else
%setup -q -n %{oname}-%{version}
%endif
%apply_patches
dos2unix COPYRIGHT README.md
# remove outdated prebuilt localizations
rm -rf bin/locale


%build
export USE_LIBPATH=%{_libdir}/
export USE_WEBGL="true"
%qmake_qt5
%make STRIP=true

%install
make install INSTALL_ROOT=%{buildroot} STRIP=true

%find_lang %{name} --all-name --with-qt
echo "%%lang(uz) /usr/share/qupzilla/locale/uz@Latn.qm" >>%{name}.lang
cat >>%{name}.lang <<EOF
%lang(lg) %{_datadir}/qupzilla/locale/lg.qm
%lang(nqo) %{_datadir}/qupzilla/locale/nqo.qm
%lang(sr) %{_datadir}/qupzilla/locale/sr.qm
%lang(sr) %{_datadir}/qupzilla/locale/sr@ijekavian.qm
%lang(sr) %{_datadir}/qupzilla/locale/sr@ijekavianlatin.qm
%lang(sr) %{_datadir}/qupzilla/locale/sr@latin.qm
EOF

