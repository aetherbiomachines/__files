from .entry import Query as EntryQuery
from .experiment import Query as ExperimentQuery


class Query(
    EntryQuery,
    ExperimentQuery,
):
    pass
