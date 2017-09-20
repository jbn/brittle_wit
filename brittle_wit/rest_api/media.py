###############################################################################
# THIS FILE WAS AUTO-GENERATED!
###############################################################################


from brittle_wit_core import TwitterRequest as _TwitterRequest
from brittle_wit_core import ELIDE as _ELIDE


def uploadSTATUS(command, media_id, media_key):
    """
    The

    :param command: Must be set to STATUS (case sensitive).

    :param media_id: The media_id returned from the INIT command. Either this
        or media_key needs to be provided.

    :param media_key: The media_key returned from the INIT command. Either this
        or media_id needs to be provided.
    """
    binding = {'command': command, 'media_id': media_id, 'media_key':
               media_key}
    url = 'https://upload.twitter.com/1.1/media/upload.json'
    return _TwitterRequest('GET',
                           url,
                           'rest:media',
                           'get-media-upload-status',
                           binding)


def metadata_create():
    """
    This endpoint can be used to provide additional information about the
    uploaded
    """
    binding = {}
    url = 'https://upload.twitter.com/1.1/media/metadata/create.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:media',
                           'post-media-metadata-create',
                           binding)


def upload(media, media_data, *, additional_owners=_ELIDE,
           media_category=_ELIDE):
    """
    Use this endpoint to upload images to Twitter. It returns a

    :param media: The raw binary file content being uploaded. Cannot be used
        with media_data.

    :param media_data: The base64-encoded file content being uploaded. Cannot
        be used with media.

    :param additional_owners: A comma-separated list of user IDs to set as
        additional owners allowed to use the returned media_id in Tweets or
        Cards. Up to 100 additional owners may be specified.

    :param media_category: A string enum value which identifies a media usecase
        (e.g. tweet_image, tweet_gif, tweet_video). If provided, media_key will
        be shown in the response.
    """
    binding = {'media': media, 'media_data': media_data, 'additional_owners':
               additional_owners, 'media_category': media_category}
    url = 'https://upload.twitter.com/1.1/media/upload.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:media',
                           'post-media-upload',
                           binding)


def uploadAPPEND(command, media_id, media_key, media, media_data,
                 segment_index):
    """
    The

    :param command: Must be set to APPEND (case sensitive).

    :param media_id: The media_id returned from the INIT command. Either this
        or media_key needs to be provided.

    :param media_key: The media_key returned from the INIT command. Either this
        or media_id needs to be provided.

    :param media: The raw binary file content being uploaded. It must be <= 5
        MB, and cannot be used with media_data.

    :param media_data: The base64-encoded chunk of media file. It must be <= 5
        MB and cannot be used with media. Use raw binary (media parameter) when
        possible.

    :param segment_index: An ordered index of file chunk. It must be between
        0-999 inclusive. The first segment has index 0, second segment has
        index 1, and so on.
    """
    binding = {'command': command, 'media_id': media_id, 'media_key':
               media_key, 'media': media, 'media_data': media_data,
               'segment_index': segment_index}
    url = 'https://upload.twitter.com/1.1/media/upload.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:media',
                           'post-media-upload-append',
                           binding)


def uploadFINALIZE(command, media_id, media_key):
    """
    The

    :param command: Must be set to FINALIZE (case sensitive).

    :param media_id: The media_id returned from the INIT command. Either this
        or media_key needd to be provided

    :param media_key: The media_key returned from the INIT command. Either this
        or media_id needs to be provided.
    """
    binding = {'command': command, 'media_id': media_id, 'media_key':
               media_key}
    url = 'https://upload.twitter.com/1.1/media/upload.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:media',
                           'post-media-upload-finalize',
                           binding)


def uploadINIT(command, total_bytes, media_type, *, media_category=_ELIDE,
               additional_owners=_ELIDE):
    """
    The

    :param command: Must be set to INIT (case sensitive).

    :param total_bytes: The size of the media being uploaded in bytes.

    :param media_type: The MIME type of the media being uploaded.

    :param media_category: A string enum value which identifies a media usecase
        (e.g. tweet_image, tweet_gif, tweet_video, amplify_video). This
        identifier is used to enforce usecase specific constraints (e.g.
        filesize, video duration) and enable advanced features.

    :param additional_owners: A comma-separated list of user IDs to set as
        additional owners allowed to use the returned media_id in Tweets or
        Cards. Up to 100 additional owners may be specified.
    """
    binding = {'command': command, 'total_bytes': total_bytes, 'media_type':
               media_type, 'media_category': media_category,
               'additional_owners': additional_owners}
    url = 'https://upload.twitter.com/1.1/media/upload.json'
    return _TwitterRequest('POST',
                           url,
                           'rest:media',
                           'post-media-upload-init',
                           binding)


_TwitterRequest.DOC_URLS['https://upload.twitter.com/1.1/media/upload.json'] = 'https://dev.twitter.com/rest/reference/get/media/upload-status'
_TwitterRequest.DOC_URLS['https://upload.twitter.com/1.1/media/metadata/create.json'] = 'https://dev.twitter.com/rest/reference/post/media/metadata/create'
_TwitterRequest.DOC_URLS['https://upload.twitter.com/1.1/media/upload.json'] = 'https://dev.twitter.com/rest/reference/post/media/upload'
_TwitterRequest.DOC_URLS['https://upload.twitter.com/1.1/media/upload.json'] = 'https://dev.twitter.com/rest/reference/post/media/upload-append'
_TwitterRequest.DOC_URLS['https://upload.twitter.com/1.1/media/upload.json'] = 'https://dev.twitter.com/rest/reference/post/media/upload-finalize'
_TwitterRequest.DOC_URLS['https://upload.twitter.com/1.1/media/upload.json'] = 'https://dev.twitter.com/rest/reference/post/media/upload-init'
