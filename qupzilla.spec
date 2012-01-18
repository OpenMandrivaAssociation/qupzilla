%define gitrev	43a0295
Name:		qupzilla
Summary:	Fast browser based on QtWebKit
Version:	1.1.5
Release:	1
Source0:	nowrep-QupZilla-v%{version}-0-g%{gitrev}.tar.gz
Patch0:		qupzilla-1.1.5-mdv-desktop.patch
Group:		Networking/WWW
License:	GPLv3+ and BSD and LGPLv2.1 and GPLv2+ and MPL
BuildRequires:	qt-devel
BuildRequires:	dos2unix

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

%prep
%setup -q -n nowrep-QupZilla-ac7abdc
#patch0 -p1
dos2unix COPYRIGHT README.md

%build
%qmake_qt4
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

# find_lang is broken :,(
#find_lang %{name} --with-qt

%__install -d %{buildroot}%{_defaultdocdir}/%{name}

%files
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
%{_iconsbasedir}/*/apps/*.png
%{_datadir}/pixmaps/%{name}.png
%{_desktopdir}/%{name}.desktop
%doc AUTHORS COPYRIGHT FAQ README.md TODO
%lang(cs) %{_datadir}/%{name}/locale/cs_CZ.qm
%lang(de) %{_datadir}/%{name}/locale/de_DE.qm
%lang(el) %{_datadir}/%{name}/locale/el_GR.qm
%lang(es) %{_datadir}/%{name}/locale/es_ES.qm
%lang(fr) %{_datadir}/%{name}/locale/fr_FR.qm
%lang(it) %{_datadir}/%{name}/locale/it_IT.qm
%lang(nl) %{_datadir}/%{name}/locale/nl_NL.qm
%lang(pl) %{_datadir}/%{name}/locale/pl_PL.qm
%lang(pt) %{_datadir}/%{name}/locale/pt_PT.qm
%lang(cs) %{_datadir}/%{name}/locale/qt_cs.qm
%lang(de) %{_datadir}/%{name}/locale/qt_de.qm
%lang(el) %{_datadir}/%{name}/locale/qt_el.qm
%lang(es) %{_datadir}/%{name}/locale/qt_es.qm
%lang(fr) %{_datadir}/%{name}/locale/qt_fr.qm
%lang(it) %{_datadir}/%{name}/locale/qt_it.qm
%lang(nl) %{_datadir}/%{name}/locale/qt_nl.qm
%lang(pl) %{_datadir}/%{name}/locale/qt_pl.qm
%lang(pt) %{_datadir}/%{name}/locale/qt_pt.qm
%lang(ru) %{_datadir}/%{name}/locale/qt_ru.qm
%lang(sk) %{_datadir}/%{name}/locale/qt_sk.qm
%lang(zh) %{_datadir}/%{name}/locale/qt_zh_CN.qm
%lang(ru) %{_datadir}/%{name}/locale/ru_RU.qm
%lang(sk) %{_datadir}/%{name}/locale/sk_SK.qm
%lang(zh) %{_datadir}/%{name}/locale/zh_CN.qm
