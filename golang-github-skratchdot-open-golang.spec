# https://github.com/skratchdot/open-golang
%global goipath         github.com/skratchdot/open-golang
%global commit          75fb7ed4208cf72d323d7d02fd1a5964a7a9073c

%gometa

Name:           golang-github-skratchdot-open-golang
Version:        0
Release:        0.13%{?dist}
Summary:        Open a file, directory, or URI using the OS's default application
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgeautosetup


%install
%goinstall


%check
# Tests depend on Firefox
# %%gochecks


%files devel -f devel.file-list
%doc README.md
%license LICENSE-MIT


%changelog
* Sat Oct 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.13.20181006git75fb7ed
- Bump to commit 75fb7ed4208cf72d323d7d02fd1a5964a7a9073c
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitba570a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitba570a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitba570a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitba570a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitba570a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitba570a1
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.gitba570a1
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gitba570a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 17 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.gitba570a1
- Remove superfluous Provides
  related: #1250507

* Mon Aug 10 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.3.gitba570a1
- Update spec file to spec-2.0
  resolves: #1250507

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitba570a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Eric Paris <eparis@redhat.com - 0-0.1.gitba570a1
- Bump to upstream ba570a111973b539baf23c918213059543b5bb6e
