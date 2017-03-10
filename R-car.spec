#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-car
Version  : 2.1.4
Release  : 33
URL      : http://cran.r-project.org/src/contrib/car_2.1-4.tar.gz
Source0  : http://cran.r-project.org/src/contrib/car_2.1-4.tar.gz
Summary  : Companion to Applied Regression
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : R-Rcpp
BuildRequires : R-SparseM
BuildRequires : R-lme4
BuildRequires : R-minqa
BuildRequires : R-nloptr
BuildRequires : R-pbkrtest
BuildRequires : R-quantreg
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n car

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489127246

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1489127246
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library car
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library car


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/car/CITATION
/usr/lib64/R/library/car/DESCRIPTION
/usr/lib64/R/library/car/INDEX
/usr/lib64/R/library/car/Meta/Rd.rds
/usr/lib64/R/library/car/Meta/data.rds
/usr/lib64/R/library/car/Meta/hsearch.rds
/usr/lib64/R/library/car/Meta/links.rds
/usr/lib64/R/library/car/Meta/nsInfo.rds
/usr/lib64/R/library/car/Meta/package.rds
/usr/lib64/R/library/car/Meta/vignette.rds
/usr/lib64/R/library/car/NAMESPACE
/usr/lib64/R/library/car/NEWS
/usr/lib64/R/library/car/R/car
/usr/lib64/R/library/car/R/car.rdb
/usr/lib64/R/library/car/R/car.rdx
/usr/lib64/R/library/car/data/Rdata.rdb
/usr/lib64/R/library/car/data/Rdata.rds
/usr/lib64/R/library/car/data/Rdata.rdx
/usr/lib64/R/library/car/doc/embedding.R
/usr/lib64/R/library/car/doc/embedding.Rnw
/usr/lib64/R/library/car/doc/embedding.pdf
/usr/lib64/R/library/car/doc/index.html
/usr/lib64/R/library/car/help/AnIndex
/usr/lib64/R/library/car/help/aliases.rds
/usr/lib64/R/library/car/help/car.rdb
/usr/lib64/R/library/car/help/car.rdx
/usr/lib64/R/library/car/help/paths.rds
/usr/lib64/R/library/car/html/00Index.html
/usr/lib64/R/library/car/html/R.css
