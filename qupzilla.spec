%define		oname	QupZilla
%define		major	1
%define		libname	%mklibname %{oname} %{major}
%define		devname	%mklibname %{oname} -d

Summary:	Fast browser based on QtWebKit
Name:		qupzilla
Version:	1.6.5
Release:	1
License:	GPLv3+ and BSD and LGPLv2.1 and GPLv2+ and MPL
Group:		Networking/WWW
Url:		http://www.qupzilla.org/
# Packaged from git://github.com/QupZilla/qupzilla.git
Source0:	https://codeload.github.com/QupZilla/qupzilla/zip/v%{version}/qupzilla-%{version}.zip
Patch0:		qupzilla-1.3.5-mdv-linking.patch
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	qt5-linguist-tools
BuildRequires:	dos2unix
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-plugins = %{EVRD}
Requires:	qt5-database-plugin-sqlite
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
%setup -q
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

%if %{mdvver} >= 201200
%find_lang %{name} --all-name --with-qt
echo "%%lang(uz) /usr/share/qupzilla/locale/uz@Latn.qm" >>%{name}.lang
%else
cat > %{name}.lang << EOF
%lang(ja) %{_datadir}/qupzilla/locale/qt_ja.qm
%lang(ru) %{_datadir}/qupzilla/locale/ru_RU.qm
%lang(pt) %{_datadir}/qupzilla/locale/pt_PT.qm
%lang(it) %{_datadir}/qupzilla/locale/qt_it.qm
%lang(sr_RS) %{_datadir}/qupzilla/locale/sr_RS.qm
%lang(pt) %{_datadir}/qupzilla/locale/qt_pt.qm
%lang(uk) %{_datadir}/qupzilla/locale/qt_uk.qm
%lang(sk) %{_datadir}/qupzilla/locale/qt_sk.qm
%lang(el) %{_datadir}/qupzilla/locale/el_GR.qm
%lang(ja) %{_datadir}/qupzilla/locale/ja_JP.qm
%lang(ro) %{_datadir}/qupzilla/locale/ro_RO.qm
%lang(sr_RS) %{_datadir}/qupzilla/locale/qt_sr_RS.qm
%lang(zh_CN) %{_datadir}/qupzilla/locale/qt_zh_CN.qm
%lang(sv) %{_datadir}/qupzilla/locale/sv_SE.qm
%lang(cs) %{_datadir}/qupzilla/locale/cs_CZ.qm
%lang(es_VE) %{_datadir}/qupzilla/locale/es_VE.qm
%lang(id) %{_datadir}/qupzilla/locale/id_ID.qm
%lang(es) %{_datadir}/qupzilla/locale/qt_es.qm
%lang(de) %{_datadir}/qupzilla/locale/qt_de.qm
%lang(cs) %{_datadir}/qupzilla/locale/qt_cs.qm
%lang(ka_GE) %{_datadir}/qupzilla/locale/ka_GE.qm
%lang(es) %{_datadir}/qupzilla/locale/es_ES.qm
%lang(uk_UA) %{_datadir}/qupzilla/locale/uk_UA.qm
%lang(hu) %{_datadir}/qupzilla/locale/qt_hu.qm
%lang(it) %{_datadir}/qupzilla/locale/it_IT.qm
%lang(zh_CN) %{_datadir}/qupzilla/locale/zh_CN.qm
%lang(nl) %{_datadir}/qupzilla/locale/qt_nl.qm
%lang(sr_BA) %{_datadir}/qupzilla/locale/qt_sr_BA.qm
%lang(sk) %{_datadir}/qupzilla/locale/sk_SK.qm
%lang(sr_BA) %{_datadir}/qupzilla/locale/sr_BA.qm
%lang(zh_TW) %{_datadir}/qupzilla/locale/qt_zh_TW.qm
%lang(hu) %{_datadir}/qupzilla/locale/hu_HU.qm
%lang(pl) %{_datadir}/qupzilla/locale/pl_PL.qm
%lang(sv) %{_datadir}/qupzilla/locale/qt_sv.qm
%lang(de) %{_datadir}/qupzilla/locale/de_DE.qm
%lang(zh_TW) %{_datadir}/qupzilla/locale/zh_TW.qm
%lang(fr) %{_datadir}/qupzilla/locale/qt_fr.qm
%lang(nl) %{_datadir}/qupzilla/locale/nl_NL.qm
%lang(el) %{_datadir}/qupzilla/locale/qt_el.qm
%lang(pt_BR) %{_datadir}/qupzilla/locale/pt_BR.qm
%lang(pl) %{_datadir}/qupzilla/locale/qt_pl.qm
%lang(fr) %{_datadir}/qupzilla/locale/fr_FR.qm
%lang(ru) %{_datadir}/qupzilla/locale/qt_ru.qm
%lang(uz) %{_datadir}/qupzilla/locale/uz@Latn.qm
EOF
%endif
cat >>%{name}.lang <<EOF
%lang(lg) %{_datadir}/qupzilla/locale/lg.qm
%lang(nqo) %{_datadir}/qupzilla/locale/nqo.qm
EOF

