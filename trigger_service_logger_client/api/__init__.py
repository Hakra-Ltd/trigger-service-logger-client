# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from trigger_service_logger_client.api.event_api import EventApi
    from trigger_service_logger_client.api.job_api import JobApi
    from trigger_service_logger_client.api.stats_api import StatsApi
    from trigger_service_logger_client.api.default_api import DefaultApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from trigger_service_logger_client.api.event_api import EventApi
from trigger_service_logger_client.api.job_api import JobApi
from trigger_service_logger_client.api.stats_api import StatsApi
from trigger_service_logger_client.api.default_api import DefaultApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
