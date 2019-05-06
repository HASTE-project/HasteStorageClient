import time
import datetime
from haste_storage_client.core import HasteStorageClient, OS_SWIFT_STORAGE, TRASH
from haste_storage_client.models.rest_interestingness_model import RestInterestingnessModel

haste_storage_client_config = {
    'haste_metadata_server': {
        # See: https://docs.mongodb.com/manual/reference/connection-string/
        # Note that the name of the database is fixed.
        # In later versions of MongoDB (3?), it needs to be specified in the connection string.
        'connection_string': 'mongodb://130.xxx.yy.zz:27017/streams'
    },
    # Optional, defaults to 'INFO'. See https://docs.python.org/3/library/logging.html#levels for possible values.
    "log_level": "DEBUG",
    # Note the structure changed here in January 2019:
    'targets': [
        {
            "id": "move-to-my-dir",
            "class": "haste_storage_client.storage.storage.MoveToDir",
            "config": {
                "source_dir": "/path/to/src/",
                "target_dir": "/path/to/dst/"
            }
        }

    ]
}

# Identifies both the experiment, and the session (ie. unique each time the stream starts),
# for example, this would be a good format - this needs to be generated at the stream edge.
initials = 'anna_exampleson'
stream_id = datetime.datetime.today().strftime('%Y_%m_%d__%H_%M_%S') + '_exp1_' + initials

print('stream ID is: %s' % stream_id)


client = HasteStorageClient(stream_id,
                            config=haste_storage_client_config,
                            interestingness_model=None, # make everything have interestingness 1.0
                            # save everything on disk.
                            storage_policy=[(0.0, 1.0, 'move-to-my-dir')],
                            )

blob_bytes = b'this is a binary blob eg. image data.\n'
timestamp_cloud_edge = time.time()
substream_id = 'B13'  # Group by microscopy well ID.

client.save(timestamp_cloud_edge,
            (12.34, 56.78), # location on the plate
            substream_id,
            bytearray(), # For the MoveToDir driver, its not necessary to specify the bytes here.
            {'image_height_pixels': 300,  # bag of extracted features here
             'image_width_pixels': 300,
             'number_of_green_pixels': 1234,
             'original_filename': 'foo.tiff'}) # the MoveToDir driver will read the filename from here, and combine it with the paths above.

client.close()
