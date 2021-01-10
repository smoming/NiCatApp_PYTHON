HTTP_GET = 'GET'
HTTP_POST = 'POST'
HTTP_PUT = 'PUT'
HTTP_DELETE = 'DELETE'


def is_Spec_Verb(spec_verb, source_verb):
    return spec_verb == source_verb


def isHTTP_GET(verb):
    return is_Spec_Verb(HTTP_GET, verb)


def isHTTP_POST(verb):
    return is_Spec_Verb(HTTP_POST, verb)


def isHTTP_PUT(verb):
    return is_Spec_Verb(HTTP_PUT, verb)


def isHTTP_DELETE(verb):
    return is_Spec_Verb(HTTP_DELETE, verb)
