def get_token(string, delim):
   
    tokens = string.split(delim)
    url = tokens[0]
    
    for token in tokens[1:]:
        token = token[:-1]
        if '/' in token : token = token[1:]
        if token in globals():
            if '=' in url:
                url = url + globals()[token]
            else:
                url = url + '/' + globals()[token]
        if ',' in token:
            token = token[1:]
            print(token)
            multitokens = token.split(',')
            for multitoken in multitokens:
                if multitoken in globals():
                    url =  url + '&' + multitoken + '=' + globals()[multitoken]
    return url