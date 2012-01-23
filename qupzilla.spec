%define gitrev	43a0295
Name:		qupzilla
Summary:	Fast browser based on QtWebKit
Version:	1.1.5
Release:	1
Source0:	nowrep-QupZilla-v%{version}-0-g%{gitrev}.tar.gz
Patch0:		qupzilla-1.1.5-mdv-desktop.patch
Group:		Networking/WWW
License:	GPLv3+ and BSD and LGPLv2.1 and GPLv2+ and MPL
BuildRequires:	qt4-devel
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
%patch0 -p1
dos2unix COPYRIGHT README.md

%build
%qmake_qt4
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%find_lang %{name} --all-name --with-qt

%__install -d %{buildroot}%{_defaultdocdir}/%{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%doc AUTHORS COPYRIGHT FAQ README.md TODO
%dir %{_datadir}/%{name}/locale
