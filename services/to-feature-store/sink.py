# import hopsworks
# from quixstreams.sinks.base import BatchingSink, SinkBackpressureError, SinkBatch


# class HopsworksFeatureStoreSink(BatchingSink):
#     """
#     Some sink writing data to a database
#     """

#     def __init__(
#         self,
#         api_key: str,
#         project_name: str,
#         feature_group_name: str,
#         feature_group_version: int,
#         feature_group_primary_key: list[str],
#         feature_group_event_time: str,
#     ):
#         """
#         Establishes a connection to the hopsworks feature store
#         """
#         self.feature_group_name = feature_group_name
#         self.feature_group_version = feature_group_version

#         # Establish a connection to the Hopsworks Feature Store
#         project = hopsworks.login(project=project_name, api_key=api_key)
#         self._fs = project.get_feature_store()

#         # Get the feature group
#         self._feature_group = self._fs.get_or_create_feature_group(
#             name=feature_group_name,
#             version=feature_group_version,
#             primary_key=feature_group_primary_key,
#             event_time=feature_group_event_time,
#             online_enabled=True,
#         )

#     def write(self, batch: SinkBatch):
#         # Simulate some DB connection here
#         data = [{'value': item.value} for item in batch]
#         try:
#         #     # Try to write data to the db
#         #     db_connection.write(data)
#         # except TimeoutError:
#             # In case of timeout, tell the app to wait for 30s
#             # and retry the writing later
#             raise SinkBackpressureError(
#                 retry_after=30.0,
#                 topic=batch.topic,
#                 partition=batch.partition,
#             )
