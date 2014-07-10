# TODO:
# - dir /usr/include/KF5 not packaged
# /usr/lib/qt5/plugins/kf5 not packaged
%define         _state          stable
%define		orgname		ki18n

Summary:	KDE Gettext-based UI text internationalization
Name:		kf5-%{orgname}
Version:	5.0.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/frameworks/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	2f57ce764c7f08a1feb0f5ad75ba7afe
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
Summary:	Header files for %{orgname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{orgname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{orgname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{orgname}.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DBIN_INSTALL_DIR=%{_bindir} \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DPLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQT_PLUGIN_INSTALL_DIR=%{qt5dir}/plugins \
	-DQML_INSTALL_DIR=%{qt5dir}/qml \
	-DIMPORTS_INSTALL_DIR=%{qt5dirs}/imports \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_LIBEXEC_INSTALL_DIR=%{_libexecdir} \
	-DKF5_INCLUDE_INSTALL_DIR=%{_includedir} \
	-DECM_MKSPECS_INSTALL_DIR=%{qt5dir}/mkspecs/modules \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{orgname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{orgname}5.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %ghost %{_libdir}/libKF5I18n.so.5
%attr(755,root,root) %{_libdir}/libKF5I18n.so.5.0.0
%attr(755,root,root) %{qt5dir}/plugins/kf5/ktranscript.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KI18n
%{_includedir}/KF5/ki18n_version.h
%{_libdir}/cmake/KF5I18n
%attr(755,root,root) %{_libdir}/libKF5I18n.so
%{qt5dir}/mkspecs/modules/qt_KI18n.pri
