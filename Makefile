#
# Simple Makefile to create the source tarball, specfile for the package
#

PACKAGE=check-create-certificate
VERSION=`grep "^Version:" package/${PACKAGE}.spec | head -1 | sed -e "s/^Version:\s\+//" -e "s/\s\+//" `
SOURCES="script"

package:   make-tarball
	echo
	ls -l package

make-tarball:
	rm -rf ${PACKAGE}-*
	rm -f package/${PACKAGE}-*.tar.bz2
	mkdir -p ${PACKAGE}-${VERSION}
	cp -a ${SOURCES} ${PACKAGE}-${VERSION}/
	tar -cvjf package/${PACKAGE}-${VERSION}.tar.bz2 ${PACKAGE}-${VERSION}/
	rm -rf ${PACKAGE}-*
