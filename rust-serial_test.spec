# Generated by rust2rpm 15
%bcond_without check
%global debug_package %{nil}

%global crate serial_test

Name:           rust-%{crate}
Version:        0.5.0
Release:        1%{?dist}
Summary:        Allows for the creation of serialised Rust tests

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/serial_test
Source:         %{crates_source}
# Initial patched metadata
# * Change parking_lot crate dependency version
Patch0:         serial_test-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Allows for the creation of serialised Rust tests.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Oct 08 13:16:52 CEST 2020 Javier Martinez Canillas <javierm@redhat.com> - 0.5.0-1
- Initial package
