sed -E -n '/.*referer":"([^"]*)".*/{s//\1/; s/https?:\/\/([^/]*)\/.*/\1/g; p;}' | sort | uniq -c
