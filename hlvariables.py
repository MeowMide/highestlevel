def var(linecode):
    line = list(linecode)
    line.pop()
    try:
        varname_list = line[:line.index('=')]
        varinfo_list = line[line.index('=') + 1:]
        varname = ''
        varinfo = ''
        for i in varname_list:
            varname += i
        for i in varinfo_list:
            varinfo += i
        return f'{varname} = {varinfo}'
    except:
        None