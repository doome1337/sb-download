.PHONY: install

install:
	cp sb-download.py /usr/local/bin/sb-download
	chmod a+x /usr/local/bin/sb-download
	cp sb-download.1 /usr/share/man/man1/sb-download.1
