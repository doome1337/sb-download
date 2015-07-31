A program to download specific posts from Spacebattles.
This was designed with the Creative Writing boards in mind.

The proper format for use can be found in format.txt.

The usage syntax is as follows:

    python sb-download.py [-f] FILE

FILE must be a post collection datafile, as shown in format.txt.

OPTIONS:
    -f: By default, sb-download will only download new chapters,
        also refreshing the most recent one.
        It assumes that new chapters will only be added at the end of the file,
        and that the order of posts remains constant.
        More precisely, it downloads only chapters 
        for which the next chapter has not yet been downloaded.

        The -f flag forces sb-download to redownload every chapter,
        regardless of the current download state.
