class RecordNotFound(Exception):
    pass


class DuplicateRecordError(Exception):
    pass


class RelatedRecordsError(Exception):
    pass


class ValidationError(Exception):
    pass