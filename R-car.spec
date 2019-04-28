#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-car
Version  : 3.0.2
Release  : 74
URL      : https://cran.r-project.org/src/contrib/car_3.0-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/car_3.0-2.tar.gz
Summary  : Companion to Applied Regression
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-cellranger
Requires: R-forcats
Requires: R-lmtest
Requires: R-maptools
Requires: R-sandwich
Requires: R-zip
BuildRequires : R-Rcpp
BuildRequires : R-SparseM
BuildRequires : R-abind
BuildRequires : R-carData
BuildRequires : R-cellranger
BuildRequires : R-forcats
BuildRequires : R-leaps
BuildRequires : R-lme4
BuildRequires : R-lmtest
BuildRequires : R-maptools
BuildRequires : R-minqa
BuildRequires : R-nloptr
BuildRequires : R-pbkrtest
BuildRequires : R-quantreg
BuildRequires : R-rgl
BuildRequires : R-rio
BuildRequires : R-sandwich
BuildRequires : R-survey
BuildRequires : R-zip
BuildRequires : buildreq-R

%description
Functions to Accompany J. Fox and S. Weisberg, 
  An R Companion to Applied Regression, Third Edition, Sage, in press.

%prep
%setup -q -c -n car

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556467919

%install
export SOURCE_DATE_EPOCH=1556467919
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library car
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library car
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library car
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc car || :


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
