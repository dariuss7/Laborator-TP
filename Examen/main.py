from checker import build_url, is_https, show_response, check_site, scan_sites, check_headers, retry_check



# Partea 1: apeluri pentru build_url și is_https
build_url("https://example.com", "/path")
build_url("https://example.com", "path")

is_https("https://example.com")
is_https("http://example.com")


# Partea 2: apeluri pentru show_response
show_response("https://example.com")


# Partea 3: apeluri pentru check_site
check_site("https://example.com")


# Partea 4: apelul scan_sites()



# Partea 5: apeluri pentru check_headers
check_headers("https://example.com")


# Partea 6: apeluri pentru retry_check

retry_check("https://example.com", 5)


