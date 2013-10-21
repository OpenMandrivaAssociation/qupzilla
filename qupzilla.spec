%define		oname	QupZilla
%define		major	1
%define		libname	%mklibname %{oname} %{major}
%define		develname	%mklibname %{oname} -d
Name:		qupzilla
Summary:	Fast browser based on QtWebKit
Version:	1.4.4
Release:	4
URL:		http://www.qupzilla.com/
# Packaged from git://github.com/QupZilla/qupzilla.git
Source0:	http://www.qupzilla.com/uploads/%{oname}-%{version}.tar.gz
Patch0:		qupzilla-1.3.5-mdv-linking.patch
Group:		Networking/WWW
License:	GPLv3+ and BSD and LGPLv2.1 and GPLv2+ and MPL
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	qt5-linguist-tools
BuildRequires:	dos2unix
Requires:	%{name}-core	= %{EVRD}
Requires:	%{name}-plugins	= %{EVRD}
Requires:	qt5-database-plugin-sqlite

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

%package core
Summary:	%{oname} web browser core package

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

%package plugins
Summary:	Various plugins for %{oname} web browser
Requires:	%{name} = %{version}

%description plugins
QupZilla Plugins are dynamically loaded shared libraries (*.so) that can extend
application in almost any way. This package contains the following plugins:

* Mouse Gestures
* Access Keys Navigation
* Personal Information Manager
* GreaseMonkey

%package -n %{libname}
Summary:	%{oname} shared library

%description -n %{libname}
Shared library used by %{oname} web browser.

%package -n %{develname}
Summary:	%{oname} development files
Requires:	%{libname} = %{version}

%description -n %{develname}
Development files for %{libname} library.

%prep
%setup -qn %{oname}-%{version}
%apply_patches
dos2unix COPYRIGHT README.md

%build
export USE_LIBPATH=%{_libdir}/
export USE_WEBGL="true"
%qmake_qt5
%make STRIP=true

%install
make install INSTALL_ROOT=%{buildroot} STRIP=true

%if %{mdvver} >= 201200
%find_lang %{name} --all-name --with-qt
%else
cat > %{name}.lang << EOF
%lang(ja) /usr/share/qupzilla/locale/qt_ja.qm
%lang(RU) /usr/share/qupzilla/locale/ru_RU.qm
%lang(PT) /usr/share/qupzilla/locale/pt_PT.qm
%lang(it) /usr/share/qupzilla/locale/qt_it.qm
%lang(RS) /usr/share/qupzilla/locale/sr_RS.qm
%lang(pt) /usr/share/qupzilla/locale/qt_pt.qm
%lang(uk) /usr/share/qupzilla/locale/qt_uk.qm
%lang(sk) /usr/share/qupzilla/locale/qt_sk.qm
%lang(GR) /usr/share/qupzilla/locale/el_GR.qm
%lang(JP) /usr/share/qupzilla/locale/ja_JP.qm
%lang(RO) /usr/share/qupzilla/locale/ro_RO.qm
%lang(sr_RS) /usr/share/qupzilla/locale/qt_sr_RS.qm
%lang(zh_CN) /usr/share/qupzilla/locale/qt_zh_CN.qm
%lang(SE) /usr/share/qupzilla/locale/sv_SE.qm
%lang(CZ) /usr/share/qupzilla/locale/cs_CZ.qm
%lang(VE) /usr/share/qupzilla/locale/es_VE.qm
%lang(ID) /usr/share/qupzilla/locale/id_ID.qm
%lang(es) /usr/share/qupzilla/locale/qt_es.qm
%lang(de) /usr/share/qupzilla/locale/qt_de.qm
%lang(cs) /usr/share/qupzilla/locale/qt_cs.qm
%lang(GE) /usr/share/qupzilla/locale/ka_GE.qm
%lang(ES) /usr/share/qupzilla/locale/es_ES.qm
%lang(UA) /usr/share/qupzilla/locale/uk_UA.qm
%lang(hu) /usr/share/qupzilla/locale/qt_hu.qm
%lang(IT) /usr/share/qupzilla/locale/it_IT.qm
%lang(CN) /usr/share/qupzilla/locale/zh_CN.qm
%lang(nl) /usr/share/qupzilla/locale/qt_nl.qm
%lang(sr_BA) /usr/share/qupzilla/locale/qt_sr_BA.qm
%lang(SK) /usr/share/qupzilla/locale/sk_SK.qm
%lang(BA) /usr/share/qupzilla/locale/sr_BA.qm
%lang(zh_TW) /usr/share/qupzilla/locale/qt_zh_TW.qm
%lang(HU) /usr/share/qupzilla/locale/hu_HU.qm
%lang(PL) /usr/share/qupzilla/locale/pl_PL.qm
%lang(sv) /usr/share/qupzilla/locale/qt_sv.qm
%lang(DE) /usr/share/qupzilla/locale/de_DE.qm
%lang(TW) /usr/share/qupzilla/locale/zh_TW.qm
%lang(fr) /usr/share/qupzilla/locale/qt_fr.qm
%lang(NL) /usr/share/qupzilla/locale/nl_NL.qm
%lang(el) /usr/share/qupzilla/locale/qt_el.qm
%lang(BR) /usr/share/qupzilla/locale/pt_BR.qm
%lang(pl) /usr/share/qupzilla/locale/qt_pl.qm
%lang(FR) /usr/share/qupzilla/locale/fr_FR.qm
%lang(ru) /usr/share/qupzilla/locale/qt_ru.qm
EOF
%endif

%files

%files core -f %{name}.lang
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
%{_datadir}/bash-completion/completions/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%doc AUTHORS COPYRIGHT FAQ README.md
%dir %{_datadir}/%{name}/locale
%dir %{_libdir}/qupzilla

%files plugins
%{_libdir}/qupzilla/*.so

%files -n %{libname}
%{_libdir}/lib%{oname}.so.%{major}*

%files -n %{develname}
%{_libdir}/lib%{oname}.so
