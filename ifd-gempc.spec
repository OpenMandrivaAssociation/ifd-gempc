Name: ifd-gempc
Summary: Gemplus 410 and 430 Smartcard reader driver
Version: 1.0.1
Release: %mkrel 1
License: GPL/BSD
Group: System/Libraries
Source0: http://ludovic.rousseau.free.fr/softwares/ifd-GemPC/ifd-gempc-%{version}.tar.gz
Source1: http://ludovic.rousseau.free.fr/softwares/ifd-GemPC/ifd-gempc-%{version}.tar.gz.asc
URL: http://ludovic.rousseau.free.fr/softwares/ifd-GemPC/index.html
BuildRequires: libpcsclite-devel
BuildRequires: libusb-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a PCSC-lite driver for Gemplus 410 and 430
smartcard readers.

%package -n ifd-gempc410
Summary: Gemplus 410 smartcard reader driver
Group: System/Libraries
Requires(post,postun): pcsc-lite
Requires: pcsc-lite

%description -n ifd-gempc410
This package provides a PCSC-lite driver for the following
serial Gemplus smartcard readers:
 * GemPC410
 * GemPC412
 * GemPC413-SL
 * GemPC415


%package -n ifd-gempc430
Summary: Gemplus 430 smartcard reader driver
Group: System/Libraries
Requires: pcsc-lite

%description -n ifd-gempc430
This package provides a PCSC-lite driver for the following usb
Gemplus smartcard readers:
 * GemPC430
 * GemPC432
 * GemPC435


%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p %{buildroot}%{_sysconfdir}/reader.conf.d
cat > %{buildroot}%{_sysconfdir}/reader.conf.d/gempc410.conf <<_EOF
FRIENDLYNAME      "GemPC410"
DEVICENAME        /dev/ttyS0
LIBPATH           %{_libdir}/pcsc/drivers/serial/libGemPC410.so.%{version}
CHANNELID         1
_EOF

%post -n ifd-gempc410
%{_sbindir}/update-reader.conf

%postun -n ifd-gempc410
if [ "$1" = "0" ]; then
	%{_sbindir}/update-reader.conf
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -n ifd-gempc430
%defattr(-,root,root)
%doc README README.430
%{_libdir}/pcsc/drivers/ifd-GemPC430.bundle

%files -n ifd-gempc410
%doc README README.410
%config(noreplace) %{_sysconfdir}/reader.conf.d/*.conf
%{_libdir}/pcsc/drivers/serial/*


