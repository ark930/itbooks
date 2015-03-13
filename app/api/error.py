class ItbookBaseError(Exception):
    def __str__(self):
        return "%s: %s" % (self.status, self.reason)


class ItbookApiError(ItbookBaseError):
    def __init__(self, status):
        self.status = status
        self.reason = ''
        self.msg = ''


class ItbookHttpError(ItbookBaseError):

    def __init__(self, status, reason):
        self.status = status
        self.reason = reason
