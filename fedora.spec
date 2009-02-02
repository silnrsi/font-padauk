%define fontname 
%define fontdir %{_datadir}/fonts/%{fontname}
%define fontconfdir %{_sysconfdir}/fonts/conf.d
%define archivename 

Name: %{fontname}-fonts
Version: %TTF_VERSION%
Release: 1
Summary: Burmese Unicode 5.1 truetype font with OT and Graphite tables
Group: User Interface/X
License: 

Source0: %{archivename}.tar.gz

BuildRoot: %{mktemp -ud %{_tmppath}/%{name}-2.5-%{release}}

BuildArch: noarch

%description
Padauk is a Burmese font designed to handle all the needs of minority
languages that use the script. It has complete coverage of the Unicode
5.1 Myanmar block and smart code primarily in Graphite. There are
OpenType tables which support Burmese.
.
The font was designed by Debbi Hosken and includes an ASCII block taken
from Sophia

%prep

%setup -q -n ${archivename}

%build

%install
rm -fr ${buildroot}
install -m 0755 -d %{buildroot}%{fontdir}
install -m 0644 -p *.ttf %{buildroot}%{fontdir}

%clean
rm -fr %{buildroot}

%post
if [ -x %{_bindir}/fc-cache ]; then
    %{_bindir}/fc-cache -f %{fontdir} || ;
fi

%postun
if [ "$1" = "0" ]; then
    if [ -x %{_bindir}/fc-cache ]; then
        %{_bindir}/fc-cache -f %{fontdir} || ;
    fi
fi

%files
%defattr(0644,root,root,0755)

%doc *.txt
%dir %{fontdir}
%{fontdir}/*.ttf

%changelog



