import base64

class Image:
    """
    A helper class to wrap an image
    """
    def __init__(self, blob=None):
        self._blob = blob
    
    @property
    def uri(self):
        """
        Returns the location of the placeholder if no image exists, or dynamically creates a URI for an uploaded image
        """
        # Placeholder default value
        uri = "/static/placeholder.png"
        if self.blob:
            # Convert image to uri
            uri = "data:;base64," + base64.b64encode(self.blob.read()).decode("utf-8")
            # Reset the stream to 0
            self._blob.seek(0)
        return uri

    @property
    def blob(self):
        """
        Returns the blob of the image
        """
        if self._blob:
            # Reset the stream to 0 just in case
            self._blob.seek(0)
        return self._blob
