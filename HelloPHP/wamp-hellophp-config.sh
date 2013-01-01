#!/bin/bash
# Proper header for a Bash script

# ------------------------------------------------------
# Set env vars
# ------------------------------------------------------
 
# document root for project
WORKSPACE_ROOT_SEDARG=c:/users/sanchezelton/workspace/CareerElement/public/

# document root for training 
WAMP_DEFAULT_ROOT_SEDARG=c:/wamp/www/

HTTPD_CONF=/cygdrive/c/wamp/bin/apache/Apache2.2.21/conf/httpd.conf
TEMP=$HTTPD_CONF.tmp

# ------------------------------------------------------
# backup old
# ------------------------------------------------------

cp $HTTPD_CONF $HTTPD_CONF.old

for file in $HTTPD_CONF
do
	# ------------
	# check file
	# ------------
	
	if [ ! -e "$file" ]
	then	
		echo "$file does not exist."; echo
		continue
	fi
	
	# ------------------------------------------------------
	# comment rewrite_module 
	# ------------------------------------------------------

	sed 's/LoadModule rewrite_module/#&/g' $HTTPD_CONF > $TEMP

	# ------------------------------------------------------
	# comment   WAMP Base Directory set to Eclipse workspace
	# decomment WAMP Base Directory set to default wamp/www  
	# ------------------------------------------------------

	sed 's@\(#\)\(DocumentRoot "$WAMP_DEFAULT_ROOT_SEDARG"\)@\2@g' $TEMP > $TEMP
	sed 's@DocumentRoot "$WORKSPACE_ROOT_SEDARG"@#&@g' $TEMP > $TEMP

	# ------------------------------------------------------
	# comment   base directory tag set to Eclipse workspace
	# decomment base directory tag set to default wamp/www
	# ------------------------------------------------------

	sed 's@\(#\)\(<Directory "$WAMP_DEFAULT_ROOT_SEDARG"\)@\2@g' $TEMP > $TEMP
	sed 's@<Directory "$WORKSPACE_ROOT_SEDARG"@#&@g' $TEMP > $HTTPD_CONF
done

# ------------------------------------------------------
# remove temp file
# ------------------------------------------------------

rm $TEMP
exit 0
