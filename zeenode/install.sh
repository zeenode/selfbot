export p="$(command -v pip)"
if [ ! -f "$p" ]; then
    	echo "please install pip before running"
else
	$p install -r requirements.txt
fi

