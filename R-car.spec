#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-car
Version  : 3.1.2
Release  : 119
URL      : https://cran.r-project.org/src/contrib/car_3.1-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/car_3.1-2.tar.gz
Summary  : Companion to Applied Regression
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-abind
Requires: R-carData
Requires: R-lme4
Requires: R-pbkrtest
Requires: R-quantreg
Requires: R-scales
BuildRequires : R-abind
BuildRequires : R-carData
BuildRequires : R-lme4
BuildRequires : R-pbkrtest
BuildRequires : R-quantreg
BuildRequires : R-scales
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Functions to Accompany J. Fox and S. Weisberg, 
  An R Companion to Applied Regression, Third Edition, Sage, 2019.

%prep
%setup -q -n car

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680188471

%install
export SOURCE_DATE_EPOCH=1680188471
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/car/CITATION
/usr/lib64/R/library/car/DESCRIPTION
/usr/lib64/R/library/car/INDEX
/usr/lib64/R/library/car/Meta/Rd.rds
/usr/lib64/R/library/car/Meta/features.rds
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
/usr/lib64/R/library/car/misc/car-hex.pdf
