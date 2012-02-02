
def patch538(options=None, buildout=None, env=None):
	"""
	Fix php Makefile by removing absolute /usr/lib paths, 
	for more info see: 
		https://bugs.php.net/bug.php?id=60268
	"""
	version = buildout["php"]["version"]
	src_path = buildout["php"]["location"] + "__compile__"+"/php-"+version+"/"
	
	print "Patching Makefile..."
	
	f1  = open(src_path+"Makefile", "r")
	src = f1.read()
	f1.close()
	
	#fix makefile
	f1 = open(src_path+"Makefile", "w")
	f1.write(src.replace("-L/usr/lib", ""))
	f1.close()
	
	
	


def main(options=None, buildout=None, env=None):
	"""
	This is called by buildout hook
	"""

	version = buildout["php"]["version"]

	if version == "5.3.8":
		patch538(options, buildout, env)
	
	return
	
	