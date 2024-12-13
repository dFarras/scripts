import os
import aemet.constants.aemet_constants as constants
import aemet.constants.aemet_alert_constants as alert_constants
from aemet.common.components.gtar_extractor import unpack_response
from aemet.common.components.gz_extractor import uncompress_response

#validate if it has been already extracted to not do so, maybe it is not a problem since the files will
#have the same name
#that target_base_path should be something like ...alerts/responses/date_n/
def extract_aemet_response(target_base_path):
    downloaded_response_path = os.path.join(
        target_base_path,
        constants.responses_downloaded_folder,
        alert_constants.alerts_response_file_name)
    unpacked_response_path = os.path.join(
        target_base_path,
        constants.responses_unpacked_folder)
    unpack_response(downloaded_response_path, unpacked_response_path)

    uncompressed_response_path = os.path.join(
        target_base_path,
        constants.responses_decompressed_folder
    )
    uncompress_response(unpacked_response_path, uncompressed_response_path)


