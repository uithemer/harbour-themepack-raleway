Name:          harbour-themepack-raleway
Version:       0.0.1
Release:       5
Summary:       Raleway theme pack
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:      harbour-themepacksupport >= 0.8.8-1
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPLv3
Source0:       %{name}-%{version}.tar.gz
BuildArch:     noarch

%description
Raleway font package for Theme pack support for Sailfish OS.

%prep
%setup -q -n %{name}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/%{name}
cp -a theme/. %{buildroot}/usr/share/%{name}/

%files
%defattr(-,root,root,-)
/usr/share/%{name}

%post
mkdir -p /home/defaultuser/.themepack/%{name}
if [ -d "/usr/share/%{name}/font" ]; then
        mv /usr/share/%{name}/font /home/defaultuser/.themepack/%{name}/
        ln -s /home/defaultuser/.themepack/%{name}/font /usr/share/%{name}/font
fi
if [ -d "/usr/share/%{name}/font-nonlatin" ]; then
        mv /usr/share/%{name}/font-nonlatin /home/defaultuser/.themepack/%{name}/
        ln -s /home/defaultuser/.themepack/%{name}/font-nonlatin /usr/share/%{name}/font-nonlatin
fi

%postun
if [ "$1" = "0" ]; then
        rm -rf /home/defaultuser/.themepack/%{name}
fi

%changelog
* Sun May 31 2026 0.0.1-5
- Migrate to theme/ + rpm/ layout.

* Fri Jan 8 2016 0.0.1
- First build.
