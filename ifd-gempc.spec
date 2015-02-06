%define _disable_ld_no_undefined 1

Summary:	Gemplus 410 and 430 Smartcard reader driver
Name:		ifd-gempc
Version:	1.0.7
Release:	2
License:	GPL/BSD
Group:		System/Libraries
Url:		http://ludovic.rousseau.free.fr/softwares/ifd-GemPC/index.html
Source0:	http://ludovic.rousseau.free.fr/softwares/ifd-GemPC/ifd-gempc-%{version}.tar.gz
Source1:	http://ludovic.rousseau.free.fr/softwares/ifd-GemPC/ifd-gempc-%{version}.tar.gz.asc
BuildRequires:	pkgconfig(libpcsclite)
BuildRequires:	pkgconfig(libusb)

%description
This package provides a PCSC-lite driver for Gemplus 410 and 430
smartcard readers.

#----------------------------------------------------------------------------

%package -n ifd-gempc410
Summary:	Gemplus 410 smartcard reader driver
Group:		System/Libraries
Requires(post,postun):	pcsc-lite
Requires:	pcsc-lite

%description -n ifd-gempc410
This package provides a PCSC-lite driver for the following
serial Gemplus smartcard readers:
 * GemPC410
 * GemPC412
 * GemPC413-SL
 * GemPC415

%files -n ifd-gempc410
%doc README README.410
%config(noreplace) %{_sysconfdir}/reader.conf.d/*.conf
%{_libdir}/pcsc/drivers/serial/*

%post -n ifd-gempc410
%{_sbindir}/update-reader.conf

%postun -n ifd-gempc410
if [ "$1" = "0" ]; then
	%{_sbindir}/update-reader.conf
fi

#----------------------------------------------------------------------------

%package -n ifd-gempc430
Summary:	Gemplus 430 smartcard reader driver
Group:		System/Libraries
Requires:	pcsc-lite

%description -n ifd-gempc430
This package provides a PCSC-lite driver for the following usb
Gemplus smartcard readers:
 * GemPC430
 * GemPC432
 * GemPC435

%files -n ifd-gempc430
%doc README README.430
%{_libdir}/pcsc/drivers/ifd-GemPC430.bundle

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%setup_compile_flags
%make

%install
%makeinstall_std
mkdir -p %{buildroot}%{_sysconfdir}/reader.conf.d
cat > %{buildroot}%{_sysconfdir}/reader.conf.d/gempc410.conf <<_EOF
FRIENDLYNAME      "GemPC410"
DEVICENAME        /dev/ttyS0
LIBPATH           %{_libdir}/pcsc/drivers/serial/libGemPC410.so.%{version}
CHANNELID         1
_EOF

