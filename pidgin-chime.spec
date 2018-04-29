#global gitsnapshot 1
%if 0%{?gitsnapshot}
%global snapcommit @SNAPCOMMIT@
%global snapcount @SNAPCOUNT@
%global shortcommit %(c=%{snapcommit}; echo ${c:0:7})
%global snapver .git.%{snapcount}.%{shortcommit}
%endif

%global tagver 0.9

%bcond_without evolution # with

Name:           pidgin-chime
Summary:        libpurple / Pidgin protocol plugin for Amazon Chime
Version:        %{tagver}%{?snapver}
Release:        1%{?dist}

Group:          Applications/Communications
License:        LGPLv2
URL:            https://github.com/awslabs/%{name}
%if 0%{?gitsnapshot:1}
Source0:        https://github.com/awslabs/%{name}/archive/%{snapcommit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        %{name}-%{version}.tar.gz
%endif

BuildRequires:  pkgconfig(pidgin) >= 2.4.0
BuildRequires:  pkgconfig(purple) >= 2.4.0
BuildRequires:  pkgconfig(gnutls) >= 3.2.0
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-rtp-1.0)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.50
%if %{with evolution}
BuildRequires:  pkgconfig(evolution-calendar-3.0)
BuildRequires:  pkgconfig(evolution-shell-3.0)
BuildRequires:  pkgconfig(evolution-data-server-1.2)
BuildRequires:  pkgconfig(libebook-1.2)
BuildRequires:  pkgconfig(libecal-1.2)
%endif # with evolution
BuildRequires:  gcc
BuildRequires:  gettext
%if 0%{?gitsnapshot:1}
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
%endif
Requires:       purple-sipe%{?_isa} = %{version}-%{release}

%description
A plugin for the Pidgin multi-protocol instant messenger, to support Amazon
Chime.

This package provides the icon set for Pidgin, and a UI plugin to indicate
seen messages.

%package -n purple-chime
Summary:  Libpurple protocol plugin for Amazon Chime
Group:    Applications/Communications

%description -n purple-chime
A plugin for the Pidgin multi-protocol instant messenger, to support Amazon
Chime.

This package provides the Amazon Chime protocol support for the libpurple
messaging library, which is used by Pidgin and other tools.


%if %{with evolution}
%package -n evolution-chime
Summary:  Evolution plugin for Amazon Chime
Group:    Applications/Productivity
Requires: pidgin-chime = %{version}-%{release}

%description -n evolution-chime
A plugin for Evolution that allows you to create meetings in Amazon Chime.
%endif # with evolution

%prep
%if 0%{?gitsnapshot:1}
%setup -q -n %{name}-%{snapcommit}
NOCONFIGURE=x ./autogen.sh
%else
%setup -q
%endif

%build
%configure \
%if %{without evolution}
  --without-evolution \
%endif # without evolution
  ;
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%check
make %{?_smp_mflags} check

%files
%defattr(-,root,root,-)
%{_datadir}/pixmaps/pidgin/protocols/*/chime*
%{_libdir}/pidgin/chimeseen.so

%files -n purple-chime -f %{name}.lang
%{_libdir}/purple-2/libchimeprpl.so
%{_libdir}/farstream-0.2/libapp-transmitter.so
%{_libdir}/gstreamer-1.0/libgstchime.so
%defattr(-,root,root,-)
%license LICENSE
%doc README TODO

%if %{with evolution}
%files -n evolution-chime
%defattr(-,root,root,-)
%{_libdir}/evolution/modules/module-event-from-template.so
%endif # with evolution

%changelog
* Fri Apr 13 2018 Andrew Jorgensen <ajorgens@amazon.com> - 0.02-0
- Initial packaging.
