# TODO:
# find_lang needs to be updated (to handle pmap, pmapc, js files)
%define		kdeframever	5.24
%define		qtver		5.3.2
%define		kfname		ki18n

Summary:	KDE Gettext-based UI text internationalization
Name:		kf5-%{kfname}
Version:	5.24.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	dce1577097eec63a478c6968e3611100
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Script-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf5-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KI18n provides functionality for internationalizing user interface
text in applications, based on the GNU Gettext translation system. It
wraps the standard Gettext functionality, so that the programmers and
translators can use the familiar Gettext tools and workflows.

KI18n provides additional functionality as well, for both programmers
and translators, which can help to achieve a higher overall quality of
source and translated text. This includes argument capturing,
customizable markup, and translation scripting.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kfname}5 --with-qm --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %ghost %{_libdir}/libKF5I18n.so.5
%attr(755,root,root) %{_libdir}/libKF5I18n.so.*.*
%attr(755,root,root) %{qt5dir}/plugins/kf5/ktranscript.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KI18n
%{_includedir}/KF5/ki18n_version.h
%{_libdir}/cmake/KF5I18n
%attr(755,root,root) %{_libdir}/libKF5I18n.so
%{qt5dir}/mkspecs/modules/qt_KI18n.pri
