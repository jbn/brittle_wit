###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit import TwitterRequest


def upload (STATUS)(command, media_id):
    """
    The
    
    :param command: Must be set to STATUS (case sensitive). (True)
    
    :param media_id: The media_id returned from the INIT command. (True)
    """
    url = "https://upload.twitter.com/1.1/media/upload.json"
    return TwitterRequest('GET',
                          url,
                          'REST:MEDIA',
                          'GET-MEDIA-UPLOAD-STATUS',
                          command=command
                          media_id=media_id)


def metadata_create():
    """
    This endpoint can be used to provide additional information about the
    uploaded
    """
    url = "https://upload.twitter.com/1.1/media/metadata/create.json"
    return TwitterRequest('POST',
                          url,
                          'REST:MEDIA',
                          'POST-MEDIA-METADATA-CREATE')


def upload(media, media_data, *, additional_owners=IGNORE):
    """
    Use this endpoint to upload images to Twitter. It returns a
    
    :param media: The raw binary file content being uploaded. Cannot be used wi
        th media_data. (True)
    
    
    :param media_data: The base64-encoded file content being uploaded. Cannot b
        e used with media. (True)
    
    
    :param additional_owners: A comma-separated list of user IDs to set as addi
        tional owners allowed to use the returned media_id in Tweets or Cards.
        Up to 100 additional owners may be specified. (False)
    """
    url = "https://upload.twitter.com/1.1/media/upload.json"
    return TwitterRequest('POST',
                          url,
                          'REST:MEDIA',
                          'POST-MEDIA-UPLOAD',
                          media=media
                          media_data=media_data
                          additional_owners=additional_owners)


def upload (APPEND)(command, media_id, media, media_data, segment_index):
    """
    The
    
    :param command: Must be set to APPEND (case sensitive). (True)
    
    :param media_id: The media_id returned from the INIT command. (True)
    
    :param media: The raw binary file content being uploaded. It must be <= 5 M
        B, and cannot be used with media_data. (True)
    
    
    :param media_data: The base64-encoded chunk of media file. It must be <= 5 
        MB and cannot be used with media. Use raw binary (media parameter) when
        possible. (True)
    
    
    :param segment_index: An ordered index of file chunk. It must be between 0-
        999 inclusive. The first segment has index 0, second segment has index
        1, and so on. (True)
    """
    url = "https://upload.twitter.com/1.1/media/upload.json"
    return TwitterRequest('POST',
                          url,
                          'REST:MEDIA',
                          'POST-MEDIA-UPLOAD-APPEND',
                          command=command
                          media_id=media_id
                          media=media
                          media_data=media_data
                          segment_index=segment_index)


def upload (FINALIZE)(command, media_id):
    """
    The
    
    :param command: Must be set to FINALIZE (case sensitive). (True)
    
    :param media_id: The media_id returned from the INIT command. (True)
    """
    url = "https://upload.twitter.com/1.1/media/upload.json"
    return TwitterRequest('POST',
                          url,
                          'REST:MEDIA',
                          'POST-MEDIA-UPLOAD-FINALIZE',
                          command=command
                          media_id=media_id)


def upload (INIT)(command, total_bytes, media_type, *, media_category=IGNORE, additional_owners=IGNORE):
    """
    The
    
    :param command: Must be set to INIT (case sensitive). (True)
    
    :param total_bytes: The size of the media being uploaded in bytes. (True)
    
    :param media_type: The MIME type of the media being uploaded. (True)
    
    :param media_category: A string enum value which identifies a media usecase
        . This identifier is used to enforce usecase specific constraints (e.g.
        filesize, video duration) and enable advanced features. (False)
    
    
    :param additional_owners: A comma-separated list of user IDs to set as addi
        tional owners allowed to use the returned media_id in Tweets or Cards.
        Up to 100 additional owners may be specified. (False)
    """
    url = "https://upload.twitter.com/1.1/media/upload.json"
    return TwitterRequest('POST',
                          url,
                          'REST:MEDIA',
                          'POST-MEDIA-UPLOAD-INIT',
                          command=command
                          total_bytes=total_bytes
                          media_type=media_type
                          media_category=media_category
                          additional_owners=additional_owners)


