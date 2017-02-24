import re

def get_video_id(url):
    shortcode = r"youtube:\/\/|https?:\/\/youtu\.be\/"

    if re.search(shortcode, url):
        shortcodeid = re.split(shortcode,url)[1];
        return stripParams(shortcodeid);

    inlinev = r"\/v\/|\/vi\/"

    if re.search(inlinev, url):
        inlineid = re.split(inlinev, url)[1];
        return stripParams(inlineid);

    parameterv = r"v=|vi="

    if re.search(parameterv, url):
        arr = re.split(parameterv, url);
        return stripParams(arr[1].split('&')[0]);

    embedreg = r"\/embed\/"

    if re.search(embedreg, url):
        embedid = re.split(embedreg, url)[1];
        return stripParams(embedid);

    userreg = r"\/user\/"

    if re.search(userreg, url):
        elements = url.split('/');
        return stripParams(elements.pop());

    attrreg = r"\/attribution_link\?.*v%3D([^%&]*)(%26|&|$)"

    if re.search(attrreg, url):
        return re.search(attrreg, url).group(1);

def stripParams(val):
    if '?' in val:
      return val.split('?')[0];
    return val;