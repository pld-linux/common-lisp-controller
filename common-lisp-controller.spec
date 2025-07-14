Summary:	Common Lisp source and compiler manager
Summary(pl.UTF-8):	Zarządca źródeł i kompilatorów Common Lispa
Name:		common-lisp-controller
Version:	7.10
Release:	1
License:	LLGPL (Lisp LGPL)
Group:		Development/Tools
Source0:	http://ftp.debian.org/debian/pool/main/c/common-lisp-controller/%{name}_%{version}.tar.gz
# Source0-md5:	d396f0be70b71be642aca3f962562132
Patch0:		%{name}-pld.patch
URL:		https://alioth.debian.org/projects/clc
Requires:	common-lisp-asdf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package helps installing Common Lisp sources and compilers.
It creates a user-specific cache of compiled objects. When a library
or an implementation is upgraded, all compiled objects in the cache
are flushed. It also provides tools to recompile all libraries.

%description -l pl.UTF-8
Ten pakiet pomaga przy instalowaniu źródeł i kompilatorów Common
Lispa. Tworzy pamięć podręczną skompilowanych obiektów dla
użytkownika. Przy aktualizacji biblioteki lub implementacji, wszystkie
pliki w pamięci podręcznej są czyszczone. Pakiet udostępnia również
narzędzia do rekompilacji wszystkich bibliotek.

%prep 
%setup -q
%patch -P0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/common-lisp
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,3,8}
install -d $RPM_BUILD_ROOT%{_datadir}/common-lisp/{source/common-lisp-controller,systems}
install -d $RPM_BUILD_ROOT%{_localstatedir}/cache/common-lisp-controller
# Not %{_libdir} because we really want /usr/lib even on 64-bit systems.
install -d $RPM_BUILD_ROOT/usr/lib/common-lisp/bin

install clc-{clbuild,lisp,slime,register-user-package,unregister-user-package} $RPM_BUILD_ROOT%{_bindir}
install clc-update-customized-images $RPM_BUILD_ROOT%{_sbindir}
install register-common-lisp-* unregister-common-lisp-* $RPM_BUILD_ROOT%{_sbindir}

cp -p common-lisp-controller.lisp post-sysdef-install.lisp $RPM_BUILD_ROOT%{_datadir}/common-lisp/source/common-lisp-controller
cp -p lisp-config.lisp $RPM_BUILD_ROOT%{_sysconfdir}/lisp-config.lisp

cp -p man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p man/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
cp -p man/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
for f in clc-update-customized-images register-common-lisp-source unregister-common-lisp-implementation unregister-common-lisp-source ; do
echo '.so man8/register-common-lisp-implementation.8' > $RPM_BUILD_ROOT%{_mandir}/man8/${f}.8
done
echo '.so man1/clc-register-user-package.1' > $RPM_BUILD_ROOT%{_mandir}/man1/clc-unregister-user-package.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DESIGN.txt debian/{NEWS,changelog,copyright}
%attr(755,root,root) %{_bindir}/clc-clbuild
%attr(755,root,root) %{_bindir}/clc-lisp
%attr(755,root,root) %{_bindir}/clc-register-user-package
%attr(755,root,root) %{_bindir}/clc-slime
%attr(755,root,root) %{_bindir}/clc-unregister-user-package
%attr(755,root,root) %{_sbindir}/clc-update-customized-images
%attr(755,root,root) %{_sbindir}/register-common-lisp-implementation
%attr(755,root,root) %{_sbindir}/register-common-lisp-source
%attr(755,root,root) %{_sbindir}/unregister-common-lisp-implementation
%attr(755,root,root) %{_sbindir}/unregister-common-lisp-source
%dir %{_sysconfdir}/common-lisp
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lisp-config.lisp
%dir /usr/lib/common-lisp
%dir /usr/lib/common-lisp/bin
%attr(1777,root,root) %dir %{_localstatedir}/cache/common-lisp-controller
%{_datadir}/common-lisp/source/common-lisp-controller
%dir %{_datadir}/common-lisp/systems
%{_mandir}/man1/clc-clbuild.1*
%{_mandir}/man1/clc-lisp.1*
%{_mandir}/man1/clc-register-user-package.1*
%{_mandir}/man1/clc-slime.1*
%{_mandir}/man1/clc-unregister-user-package.1*
%{_mandir}/man3/common-lisp-controller.3*
%{_mandir}/man8/clc-update-customized-images.8*
%{_mandir}/man8/register-common-lisp-implementation.8*
%{_mandir}/man8/register-common-lisp-source.8*
%{_mandir}/man8/unregister-common-lisp-implementation.8*
%{_mandir}/man8/unregister-common-lisp-source.8*
