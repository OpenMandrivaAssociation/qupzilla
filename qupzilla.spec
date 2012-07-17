%define		oname	QupZilla
%define		major	1
%define		libname	%mklibname %{oname} %{major}
%define		develname	%mklibname %{oname} -d
Name:		qupzilla
Summary:	Fast browser based on QtWebKit
Version:	1.3.1
Release:	1
URL:		http://www.qupzilla.com/
Source0:	%{oname}-%{version}.tar.gz
Group:		Networking/WWW
License:	GPLv3+ and BSD and LGPLv2.1 and GPLv2+ and MPL
BuildRequires:	qt4-devel
BuildRequires:	dos2unix
Requires:	%{name}-core	= %{EVRD}
Requires:	%{name}-plugins	= %{EVRD}

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

%description -n %{libname}
Development files for %{libname} library.

%prep
%setup -q -n %{oname}-%{version}
dos2unix COPYRIGHT README.md

%build
export USE_LIBPATH=%{_libdir}/
%qmake_qt4
%make

%install
make install INSTALL_ROOT=%{buildroot}

%find_lang %{name} --all-name --with-qt

%files core -f %{name}.lang
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%doc AUTHORS COPYRIGHT FAQ README.md TODO
%dir %{_datadir}/%{name}/locale
%dir %{_libdir}/qupzilla

%files plugins
%{_libdir}/qupzilla/*.so

%files -n %{libname}
%{_libdir}/lib%{oname}.so.%{major}*

%files -n %{develname}
%{_libdir}/lib%{oname}.so
