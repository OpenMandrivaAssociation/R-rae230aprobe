%global packname  rae230aprobe
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.12.0
Release:          1
Summary:          Probe sequence data for microarrays of type rae230a
Group:            Sciences/Mathematics
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/rae230aprobe_2.12.0.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-AnnotationDbi 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-AnnotationDbi

%description
This package was automatically created by package AnnotationDbi version
1.15.34. The probe sequence data was obtained from
http://www.affymetrix.com. The file name was RAE230A\_probe\_tab.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
